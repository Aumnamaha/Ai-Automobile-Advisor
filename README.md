# 🚗 AI Automobile Advisor

> **Intelligent car-buying companion that provides personalized vehicle recommendations, price comparisons, and financing guidance powered by AI.**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://www.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 📋 Executive Summary

**AI Automobile Advisor** is an AI-powered web application that assists users in making informed car-buying decisions. It provides personalized vehicle recommendations based on budget, preferences, and usage patterns — complete with price comparisons, financing options, and detailed specifications from multiple sources including Gemini API and NVIDIA NIM.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **AI-Powered Recommendations** | Personalized car suggestions based on user preferences via Gemini API |
| 💰 **Price Comparison** | Compare prices across dealerships and online platforms |
| 📊 **Financing Guidance** | EMI calculators and loan comparison tools |
| 🔍 **Vehicle Search** | Advanced filtering by brand, type, price range, fuel type |
| ⚡ **Real-Time Data** | Live vehicle specs, ratings, and availability data |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│              Streamlit Web UI                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │ Car      │  │ Compare  │  │ Financing        │  │
│  │ Search   │  │ Prices   │  │ Calculator       │  │
│  └────┬─────┘  └────┬─────┘  └────────┬─────────┘  │
│       └─────────────┼──────────────────┘             │
│                     ▼                                │
│            ┌────────────────┐                        │
│            │ AI Engine      │                        │
│            │ (Gemini/NVIDIA)│                        │
│            └────────────────┘                        │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** installed on your system
- **Google Gemini API Key** or **NVIDIA NIM API Key** (at least one required)

### Installation

```powershell
# Step 1: Clone the repository
git clone https://github.com/Aumnamaha/Ai-Automobile-Advisor.git
cd Ai-Automobile-Advisor

# Step 2: Activate virtual environment
& "C:\Users\Aum Namaha\Documents\finalenv\Scripts\Activate.ps1"

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Configure API keys (optional — falls back gracefully)
$env:GEMINI_API_KEY = "your-gemini-key-here"
$env:NVIDIA_NIM_KEY = "your-nvidia-key-here"

# Step 5: Launch the application
streamlit run app.py
```

**Expected output:** Server starts on `http://localhost:8501` with the car advisor interface.

---

## 📁 Project Structure

```
Ai-Automobile-Advisor/
├── app.py                    # Main Streamlit application (embedded UI + AI proxy)
├── server.py                 # Starlette ASGI proxy service
├── requirements.txt          # Dependencies: streamlit, starlette, uvicorn
└── README.md                 # This file
```

---

## 🧪 Verification

```powershell
# Verify dependencies
pip check

# Launch and verify (no errors in terminal)
streamlit run app.py --server.headless true
```

Expected: Server starts successfully on `http://localhost:8501`.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| **Frontend** | Streamlit (embedded HTML/JS) |
| **AI/LLM** | Google Gemini API / NVIDIA NIM |
| **Web Server** | uvicorn + starlette (ASGI proxy) |

---

## 📸 Deployment

The application is deployed at: [AI Automobile Advisor on Streamlit](https://ai-automobile-advisor-eeefvkqvss4nuixkbox8fk.streamlit.app/)

---

## 👤 Author

**Maintained by [Thirunagari Aum Namaha](https://github.com/Aumnamaha)** • [LinkedIn](https://www.linkedin.com/in/aumnamaha-thirunagari-9214782bb/)

---

## 📜 License

This project is licensed under the MIT License.
