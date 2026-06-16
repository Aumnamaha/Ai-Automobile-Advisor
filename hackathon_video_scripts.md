# Hackathon Video Submission Scripts
## AI Automobile Advisor — i18n/l10n Enabled

**Title Format:** `HACKATHON-16062026-[TeamName]-[CollegeName]`

---

## Video 1: Tech Stack (~1 minute)

**Description (3 points):**

1. **Technologies used:** Frontend built with vanilla HTML5, CSS3, and JavaScript — no framework overhead, ensuring lightweight offline performance. AI powered by Claude (Anthropic) via REST API, with a local-first architecture using in-browser state management. i18n/l10n handled through a custom JS translation engine supporting 4 locales (en, hi, mr, ja) with locale-specific number formatting.

2. **Why this stack:** We chose vanilla JS over React/Vue to minimize bundle size and maximize offline compatibility — critical for local AI inference on low-end devices. Streamlit was replaced with a pure HTML app for full control over i18n rendering, especially Devanagari and Japanese scripts which need careful font loading and RTL/LTR handling.

3. **Most interesting technical component:** The l10n number formatting engine — it converts budgets into culturally correct formats: "₹5 Lakh" in English, "₹5 लाख" in Hindi/Marathi, and "₹5L (≈85万円)" with approximate yen conversion for Japanese users. This is true localization (l10n), not just translation (i18n).

---

## Video 2: Target Users & Value Proposition (~1 minute)

**Description (3 points):**

1. **Target users:** First-time car buyers in India — especially Tier 2 and Tier 3 city residents who are more comfortable in Hindi or Marathi than English. Also targeting the Indian diaspora in Japan who need bilingual advice. Users range from 22-45, budget-conscious, digitally semi-literate, often consulting family for big purchases.

2. **Problems solved:** Car buying in India is overwhelming — 200+ models, hidden costs, dealer pressure, and almost all comparison sites only in English. Non-English speakers are underserved and often make poor decisions due to language barriers. Existing apps lack true localization (they machine-translate English UI, which breaks cultural context like number formats and honorifics).

3. **How our solution helps:** Users interact with the AI in their native language — Hindi, Marathi, or Japanese — and receive culturally adapted responses. Budget is displayed as "₹5 लाख" not "$6,000". The AI understands Indian road conditions, CNG infrastructure, and regional service networks. Local AI mode ensures privacy — no data leaves the device, critical for users wary of data privacy.

---

## Video 3: Collaboration Opportunities (~1 minute)

**Description (3 points):**

1. **Related hackathon projects:** Projects involving financial advisory (for EMI/loan integration), insurance tech (for embedded car insurance quotes), and EV charging network maps (for EV recommendation routing) are natural partners. Any project building multilingual user interfaces would also benefit from our i18n/l10n engine.

2. **Integration possibilities:** Our AI advisor could embed into a fintech project's loan calculator — when a user picks a car, the fintech app auto-populates EMI options in their language. With an EV charging network project, we could show "nearest charger" data alongside EV recommendations. The i18n engine itself is modular and could be shared as an open-source utility.

3. **Combined value:** A combined Auto-Finance-Insurance-EV stack would create a full "car ownership journey" app — from discovery (our AI) to financing (fintech partner) to insurance (insurtech partner) to charging (EV partner) — all in the user's native language, end-to-end. This addresses a ₹3.5 lakh crore Indian automobile market that is currently fragmented across dozens of apps.

---

## Video 4: Use of GenAI During Development (~1 minute)

**Description (3 points):**

1. **How GenAI helped:** Claude AI was used for the entire development process — generating the initial app architecture, writing the i18n translation engine, creating all 4 locale translation objects (English, Hindi, Marathi, Japanese), debugging CSS theme issues in the preferences panel, and writing the car recommendation filtering logic.

2. **AI tools/models used:** Claude Sonnet 4.6 (Anthropic) was the primary tool — used both as a coding assistant during development and as the embedded AI engine inside the app itself. The app's chat feature calls the Claude API in real-time to provide multilingual car advice.

3. **Biggest improvement:** The i18n/l10n system that would have taken 2–3 days to research and implement manually was produced in under 2 hours using Claude. Particularly impressive was generating accurate Hindi and Marathi translations for UI strings with correct Devanagari typography, and the Japanese locale with culturally appropriate honorifics and number formatting — tasks that would normally require native-speaker consultants.

---

## Video 5: Learnings & Accessibility Experience (~1 minute)

**Description (3 points):**

1. **i18n/l10n and multilingual implementation:** We implemented true i18n (internationalization) — the app's architecture enables any locale — and l10n (localization) — culturally adapted content for each. As Mozilla's L10n blog explains, i18n "enables" l10n: our JS translation engine (i18n layer) enables locale-specific adaptations like number formatting, currency display, and tone (l10n layer). Four languages supported: English, हिंदी (Hindi), मराठी (Marathi), 日本語 (Japanese) — with font loading for Devanagari and CJK scripts via Google Fonts' Noto family.

2. **Offline-first and local AI:** The app is built as a single HTML file with no build step — it can run entirely from disk with no server. The "Local AI" mode routes queries to an on-device-compatible AI endpoint, and all user preferences are stored in browser memory (not localStorage, ensuring compatibility across environments). The AI model toggle lets users choose between local inference (private, offline-capable) and cloud inference (more powerful).

3. **Key learnings and challenges:** The hardest challenge was making Devanagari script render correctly in CSS — font stacking and line-height need special handling compared to Latin scripts. We also learned that "translation" ≠ "localization": translating "₹5 Lakh" as "50,000 INR" for Japanese users is technically correct but culturally wrong — they need "₹5L (≈85万円)" to make sense of it. The biggest learning: design for localization from day one, not as an afterthought, because retrofitting i18n into an existing layout breaks spacing, UI flow, and font rendering.

---

## Submission Checklist
- [ ] Record 5 videos, ~1 minute each
- [ ] Clear audio (use earphones mic if possible)
- [ ] Show app demo while talking (screen recording recommended)
- [ ] Upload with title: `HACKATHON-16062026-[TeamName]-[CollegeName]`
- [ ] Add 2-3 line description for each of the 3 points per video in the upload description field
