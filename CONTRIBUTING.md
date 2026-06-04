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

* Adhere to PEP 8 coding standards for Python.
* Write maintainable and well-structured code.
* Use clear and consistent naming patterns.
* Design functions to be concise and reusable.
* Include meaningful comments and documentation where required.

## Frontend Guidelines

* Build reusable and scalable UI components.
* Follow the established project directory structure.
* Apply Tailwind CSS utility classes consistently across the application.
* Ensure responsiveness and maintain a clean user interface.

## Backend Guidelines

* Develop APIs following RESTful design principles.
* Perform proper validation for all incoming requests.
* Implement robust error handling and logging.
* Create reusable business logic and service layers.
* **API Testing:** We use [Bruno](https://www.usebruno.com/) for API testing and documentation. You can find the collection in the `bruno/` directory.

---

# API Testing with Bruno

We use Bruno, an open-source, Git-friendly API client, to share and test our API endpoints.

1.  **Download Bruno:** Get it from [usebruno.com](https://www.usebruno.com/downloads).
2.  **Open Collection:** In Bruno, select "Open Collection" and choose the `bruno/` folder in the project root.
3.  **Select Environment:** Use the "Local" environment from the environment selector in the top-right corner.
4.  **Run Requests:** You can now run health checks, login, and test complaint submissions locally.

## AI Guidelines

* Ensure AI responses follow a consistent structured format.
* Keep prompt updates and modifications properly documented.
* Implement reliable fallback and recovery mechanisms.
* Monitor output quality and maintain response accuracy.


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



