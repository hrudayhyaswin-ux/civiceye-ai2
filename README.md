# 🏙️ CivicEye — Citizen Issue Reporting Platform

[![License: AGPLv3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

CivicEye empowers citizens to report civic issues — potholes, broken streetlights, garbage overflow, and more — directly to local authorities. Built to bridge the gap between residents and government, it makes civic participation fast, transparent, and accountable.

---

## ✨ Features

- 📍 **Geotagged Issue Reporting** — Citizens pin issues on a live map
- 📸 **Photo Uploads** — Attach images as evidence
- 🔔 **Status Tracking** — Follow your report from submission to resolution
- 🏛️ **Authority Dashboard** — Officials view, prioritize, and resolve complaints
- 🔐 **Secure Auth** — JWT-based authentication for citizens and admins

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
