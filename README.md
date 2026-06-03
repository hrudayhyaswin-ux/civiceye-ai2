# 🏙️ CivicEye — Citizen Issue Reporting Platform

[![License: AGPLv3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

CivicEye empowers citizens to report civic issues — potholes, broken streetlights, garbage overflow, and more — directly to local authorities. Built to bridge the gap between residents and government, it makes civic participation fast, transparent, and accountable.

---

# Deployment Links

### Citizen Portal (Version 2 — Current)

https://civiceye-citizen.vercel.app

### Citizen Portal (Version 1)

https://citizen-app-olive.vercel.app

---

# Focus Area

**National Level — India**

India already operates large-scale grievance systems and is actively moving toward multilingual and multimodal citizen services. CivicEye AI is designed as an intelligent grievance enhancement layer supporting this transition.

---

# Problem Statement

Despite existing grievance systems, many citizens still face challenges:

* Difficulty selecting the correct department
* Language barriers
* Low digital literacy
* Poorly structured complaints
* Duplicate complaints
* Large complaint volumes causing slower processing

These challenges become more significant because of India's linguistic diversity and scale.

---

# Proposed Solution

CivicEye AI serves as an intelligent civic grievance management platform.

Citizens can file complaints using the following methods:

• Voice inputs
• Text-based reports
• Image uploads
• GPS/Location data
• Support for multiple Indian languages

The system automatically performs:

• Speech-to-text transcription
• Complaint standardization and cleaning
• Issue categorization
• Automated department assignment
• Severity and priority assessment
• Duplicate complaint identification

The objective is not to replace existing government grievance systems, but to enhance complaint accuracy, streamline processing, and improve response efficiency.


# Unique Features

## Voice First Filing

Supports complaint filing using Telugu, Hindi, English, and mixed languages.

## AI Department Mapping

Suggests appropriate departments automatically.

## Complaint Summarization

Converts lengthy complaints into operational summaries.

## Duplicate Detection

Groups similar complaints into broader incidents.

## Priority Scoring

Highlights urgent public issues faster.

## National Analytics

Enables complaint pattern analysis across departments and regions.

---

✨ Features

📍 Interactive Location-Based Reporting — Citizens can mark and report issues directly on a digital map

📸 Evidence Upload Support — Submit photos to provide visual proof of reported problems

🔔 Real-Time Complaint Monitoring — Track complaint progress from registration to closure

🏛️ Administrative Management Dashboard — Authorities can review, assign, prioritize, and resolve grievances efficiently

🔐 Role-Based Secure Access — JWT-powered authentication system for both citizens and government officials

---

## 🧱 Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Frontend  | React, Tailwind CSS                 |
| Backend   | Python (FastAPI / Django)           |
| Database  | PostgreSQL                          |
| Auth      | JWT                                 |
| Hosting   | Vercel (frontend), Render (backend) |

---

## 🚀 Getting Started

### Prerequisites

- Node.js ≥ 18
- Python ≥ 3.10
- PostgreSQL

### 1. Clone the repo

```bash
git clone https://github.com/<your-org>/civiceye.git
cd civiceye
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # Fill in your values
python manage.py migrate        # or: uvicorn main:app --reload
```

### 3. Set up the frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🗂️ Project Structure

```
civiceye/
├── backend/          # Python API (FastAPI/Django)
│   ├── app/
│   ├── requirements.txt
│   └── .env.example
├── frontend/         # React application
│   ├── src/
│   ├── public/
│   └── .env.example
├── docs/
│   ├── USER_MANUAL.md
│   └── AGENTS.md
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
└── Dockerfile
```

---

## 🛡️ Security & Audits

We take security seriously. The following audits are integrated into our development workflow:

- **Python Audit**: `pip-audit` and `uv audit` check for known vulnerabilities in backend and AI service dependencies.
- **Node.js Audit**: `npm audit` scans frontend dependencies for security risks.
- **Secret Scanning**: `gitleaks` and `trufflehog` prevent accidental exposure of secrets and API keys.
- **SAST**: `bandit` and `semgrep` perform static analysis to find security flaws in the code.

To run audits locally:

```bash
# Python
pip-audit -r backend/requirements.txt -r ai-service/requirements.txt

# Frontend
cd frontend/citizen-app && npm audit
cd ../admin-dashboard && npm audit
```

---

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

## 🔒 Security

To report a vulnerability, see [SECURITY.md](SECURITY.md).

---

## 📄 License

This project is licensed under the **GNU Affero General Public License v3.0**. See [LICENSE](LICENSE) for details.

---

## 👥 Team

Built with ❤️ by a student team passionate about civic technology.

