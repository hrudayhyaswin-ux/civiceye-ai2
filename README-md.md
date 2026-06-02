# CivicEye AI India

AI-powered multilingual civic grievance intake and resolution support platform designed for national-scale civic complaint management in India.

CivicEye AI enables citizens to submit complaints through voice, text, images, and location data, transforming raw complaints into structured, actionable grievance tickets using AI.

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

CivicEye AI acts as an intelligent civic complaint layer.

Citizens can file complaints using:

* Voice
* Text
* Images
* Location information
* Multiple Indian languages

The platform performs:

* Speech-to-text conversion
* Complaint normalization
* Classification
* Department routing
* Priority scoring
* Duplicate detection

The goal is not replacing existing systems but improving complaint quality and processing.

---

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

# Tech Stack

| Layer           | Technology                   |
| --------------- | ---------------------------- |
| Citizen Portal  | React, Vite, Tailwind CSS    |
| Admin Dashboard | React, Vite, Tailwind CSS    |
| Backend API     | Flask / Django REST          |
| Database        | MongoDB / PostgreSQL / MySQL |
| AI Backbone     | OpenRouter                   |
| Speech Support  | AssemblyAI Fallback          |
| Maps            | Google Maps / OpenStreetMap  |
| File Uploads    | Cloudinary                   |
| Deployment      | Vercel, Render, Railway      |
| Collaboration   | GitHub, Postman, Figma       |

---

# Architecture

```text
Citizen Input
(Voice / Text / Image / Location)

        ↓

Speech-to-Text / Translation

        ↓

AI Complaint Analysis

        ↓

Category + Department + Priority

        ↓

Backend Ticket Creation

        ↓

Admin Dashboard

        ↓

Tracking + Analytics
```

---

# Team Structure

### Product Lead / Presenter

Problem framing, pitch, demo, documentation

### Frontend Developer 1

Citizen Portal

### Frontend Developer 2

Admin Dashboard

### Backend Developer

APIs, Database, Ticket Logic

### AI/ML Engineer

Speech, Classification, Routing, Duplicate Detection

---

# Running the Project

## Automated Setup

```bash
bash scripts/setup.sh
```

## Docker Setup

```bash
docker-compose up --build
```

## Local Development

### Backend

```bash
cd backend
python run.py
```

Backend:

```text
http://localhost:5000
```

### AI Service

```bash
cd ai-service

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 8000
```

AI Service:

```text
http://localhost:8000
```

### Frontend

```bash
cd frontend/citizen-app

npm install

npm run dev
```

App:

```text
http://localhost:5173
```

---

# Demo Credentials

Citizen Login:

```text
No password required
```

Admin Login:

```text
Password: admin123
```

---

# API Health Check

```bash
curl http://localhost:5000/api/health
```

---

# AI Service Test

```bash
curl -X POST http://localhost:8000/ai/classify \
-H "Content-Type: application/json" \
-d '{"text":"మా వీధిలో డ్రైనేజ్ బ్లాక్ అయింది వెంటనే పరిష్కరించండి","language":"auto"}'
```

---

# Notes

### Backend Resilience

Works even when AI services fail using fallback routing.

### AI Enhancement Layer

Provides:

* Classification
* Priority
* Department Mapping
* Language Detection
* Summaries
* Confidence Scores

### Frontend Features

* Authentication
* Complaint Tracking
* Admin Workflows
* Filtering
* Status Management
* Role-based Access

---

# Project Pitch Summary

CivicEye AI strengthens existing grievance systems by making complaints:

* Easier to file
* Easier to understand
* Easier to route
* Easier to resolve

through multilingual voice input, AI structuring, smart routing, and intelligent admin workflows.
