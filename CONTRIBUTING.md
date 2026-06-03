# Contributing to CivicEye

First off, thank you for considering contributing to CivicEye 🎉

CivicEye aims to improve civic issue reporting and resolution through AI-powered workflows, and contributions from the community help make the platform better, more reliable, and more impactful.

---

# Table of Contents

* Getting Started
* Project Setup
* How to Contribute
* Development Guidelines
* Commit Guidelines
* Reporting Issues
* Pull Request Process
* Code of Conduct

---

# Getting Started

Before contributing, ensure you have:

* Git installed
* Python 3.10+ installed
* Node.js and npm installed
* Basic understanding of the project architecture

---

# Project Setup

## 1. Clone Repository

```bash
git clone https://code.swecha.org/hruday25/civicaiv2.git
cd civicaiv2
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

Install both Backend and AI service dependencies:

```bash
pip install -r backend/requirements.txt -r ai-service/requirements.txt -r requirements-dev.txt
```

## 4. Install Frontend Dependencies

```bash
cd frontend/citizen-app && npm install
cd ../admin-dashboard && npm install
```

## 5. Run Development Environment

Backend:

```bash
cd backend
python run.py
```

AI Service:

```bash
cd ai-service
uvicorn main:app --reload --port 8001
```

Frontend:

```bash
cd frontend/citizen-app
npm run dev
```

---

# How to Contribute

1. Fork the repository (if applicable)

2. Create a new branch

```bash
git checkout -b feat/your-feature-name
```

3. Make your changes

4. Commit your changes

```bash
git commit -m "Add: meaningful description"
```

5. Push changes

```bash
git push origin feature/your-feature-name
```

6. Open a Pull Request

---

# Development Guidelines

## Code Quality

* Follow PEP 8 for Python code
* Write clean, modular code
* Maintain consistent naming conventions
* Keep functions small and reusable
* Add comments where necessary

## Frontend Guidelines

* Keep components reusable
* Follow existing folder structure
* Use Tailwind utility classes consistently

## Backend Guidelines

* Keep APIs RESTful
* Validate all inputs
* Handle errors properly
* Write reusable services

## AI Guidelines

* Maintain structured outputs
* Document prompt changes
* Ensure fallback mechanisms work correctly

---

# Commit Guidelines

Use clear commit messages.

Examples:

```text
feat: add complaint classification endpoint

fix: resolve duplicate complaint detection bug

docs: update setup instructions
```

Avoid:

```text
update stuff

changes

fixed issue
```

---

# Reporting Issues

When creating issues:

* Provide clear descriptions
* Include reproduction steps
* Mention expected behavior
* Mention actual behavior
* Add screenshots/logs when helpful

---

# Pull Request Process

Before submitting:

* Ensure code builds successfully
* Test your changes
* Update documentation if required
* Resolve merge conflicts

Pull Requests should include:

* Description of changes
* Screenshots (if UI changes)
* Testing details

---

# Security Guidelines

Please do not commit:

* API keys
* Secrets
* Environment files
* Credentials

Use:

```text
.env
.env.local
.env.production
```

inside `.gitignore`

---

# Code of Conduct

Please maintain a respectful environment.

* Be professional
* Be constructive
* Respect differing opinions
* Avoid harassment or abusive behavior

---

Thank you for contributing to CivicEye Technical Project🚀



