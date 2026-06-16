import http.server
import socketserver
import urllib.request
import urllib.error
import json
import os

PORT = 8000

# =========================================================================
# SECURE BACKEND API KEYS
# Paste your keys here. Because this script runs on the server side,
# these keys are completely hidden from the browser and the network tab.
# =========================================================================
GEMINI_API_KEY = "AQ.Ab8RN6KrVPeTlRJOypVaqq3HsbPuVCk8su3QHOb_QNVCsK4jdQ"      # Paste your free Gemini key here (https://aistudio.google.com/)
NVIDIA_NIM_KEY = "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"      # Paste your Nvidia NIM key here (https://build.nvidia.com/)
CUSTOM_API_KEY = ""      # Optional key for custom OpenAI-compatible API

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.path = "/ai_automobile_advisor.html"
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/chat" or self.path == "/api/test":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            req_data = json.loads(post_data.decode('utf-8'))
            
            provider = req_data.get('provider')
            base_url = req_data.get('baseUrl')
            api_key = req_data.get('apiKey')
            model = req_data.get('model')
            
            # Backend secure keys fallback
            if not api_key:
                if provider == 'gemini':
                    api_key = GEMINI_API_KEY
                elif provider == 'nvidia':
                    api_key = NVIDIA_NIM_KEY
                elif provider == 'custom':
                    api_key = CUSTOM_API_KEY
            
            is_test = self.path == "/api/test"
            
            # Use native Gemini generateContent API to support Google Search Grounding
            if provider == 'gemini' and not is_test:
                gemini_model = model
                if gemini_model.startswith('models/'):
                    gemini_model = gemini_model[7:]
                if gemini_model == 'gemini-1.5-flash':
                    gemini_model = 'gemini-2.5-flash-lite'
                dest_url = f"https://generativelanguage.googleapis.com/v1beta/models/{gemini_model}:generateContent"
                if api_key:
                    dest_url += f"?key={api_key}"
                method = 'POST'
                
                # Convert OpenAI messages to Gemini native contents & systemInstruction
                messages = req_data.get('messages', [])
                contents = []
                system_instruction = None
                for msg in messages:
                    role = msg.get('role')
                    content = msg.get('content')
                    if role == 'system':
                        system_instruction = {
                            "parts": [{"text": content}]
                        }
                    else:
                        contents.append({
                            "role": 'user' if role == 'user' else 'model',
                            "parts": [{"text": content}]
                        })
                
                req_body = json.dumps({
                    "contents": contents,
                    "systemInstruction": system_instruction,
                    "tools": [{"google_search": {}}],
                    "generationConfig": {
                        "maxOutputTokens": req_data.get('max_tokens', 1000),
                        "temperature": req_data.get('temperature', 0.7)
                    }
                }).encode('utf-8')
            else:
                # Standard OpenAI-compatible proxy logic
                if is_test:
                    dest_url = f"{base_url}/models"
                    if provider == 'gemini' and api_key:
                        dest_url += f"?key={api_key}"
                    method = 'GET'
                    req_body = None
                else:
                    dest_url = f"{base_url}/chat/completions"
                    if provider == 'gemini' and api_key:
                        dest_url += f"?key={api_key}"
                    method = 'POST'
                    req_body = json.dumps({
                        "model": model,
                        "messages": req_data.get('messages', []),
                        "max_tokens": req_data.get('max_tokens', 1000),
                        "temperature": req_data.get('temperature', 0.7)
                    }).encode('utf-8')

            # Create request
            req = urllib.request.Request(dest_url, data=req_body, method=method)
            req.add_header('Content-Type', 'application/json')
            if api_key and not (provider == 'gemini' and not is_test):
                req.add_header('Authorization', f'Bearer {api_key}')
                
            try:
                with urllib.request.urlopen(req) as response:
                    res_data = response.read()
                    
                    # Convert response back to OpenAI format if using native Gemini API
                    if provider == 'gemini' and not is_test:
                        try:
                            gemini_res = json.loads(res_data.decode('utf-8'))
                            text = gemini_res['candidates'][0]['content']['parts'][0]['text']
                            openai_res = {
                                "choices": [
                                    {
                                        "message": {
                                            "role": "assistant",
                                            "content": text
                                        }
                                    }
                                ]
                            }
                            res_data = json.dumps(openai_res).encode('utf-8')
                        except Exception as e:
                            openai_res = {
                                "choices": [
                                    {
                                        "message": {
                                            "role": "assistant",
                                            "content": f"Error parsing response: {str(e)}"
                                        }
                                    }
                                ]
                            }
                            res_data = json.dumps(openai_res).encode('utf-8')
                            
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(res_data)
            except urllib.error.HTTPError as e:
                # Connection test fallback for models list
                if is_test and e.code in [404, 405]:
                    try:
                        dest_url = f"{base_url}/chat/completions"
                        if provider == 'gemini' and api_key:
                            dest_url += f"?key={api_key}"
                        req_body = json.dumps({
                            "model": model,
                            "messages": [{"role": "user", "content": "ping"}],
                            "max_tokens": 1
                        }).encode('utf-8')
                        req2 = urllib.request.Request(dest_url, data=req_body, method='POST')
                        req2.add_header('Content-Type', 'application/json')
                        if api_key:
                            req2.add_header('Authorization', f'Bearer {api_key}')
                        with urllib.request.urlopen(req2) as response2:
                            res_data2 = response2.read()
                            self.send_response(200)
                            self.send_header('Content-Type', 'application/json')
                            self.send_header('Access-Control-Allow-Origin', '*')
                            self.end_headers()
                            self.wfile.write(res_data2)
                            return
                    except Exception as e2:
                        e = e2
                
                err_content = e.read() if hasattr(e, 'read') else str(e).encode('utf-8')
                self.send_response(e.code if hasattr(e, 'code') else 500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(err_content)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"error": {"message": str(e)}}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), ProxyHandler) as httpd:
    print(f"Server successfully launched on http://localhost:{PORT}")
    print(f"Open http://localhost:{PORT}/ in your web browser!")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping proxy server...")
