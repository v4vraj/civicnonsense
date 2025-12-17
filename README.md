# 🛣️ PholKhol – AI-Powered Civic Issue Reporting Platform

PholKhol is a social media–style civic issue reporting platform that enables citizens to report local infrastructure problems such as potholes, water logging, damaged signs, and road hazards.  
The system uses **AI-powered workflows (Kestra)** to automatically analyze, prioritize, and escalate the most critical issues.

---

## 🚀 Features

- 📸 Citizens can post civic issues with images and descriptions
- 🧠 AI-based image classification & severity assessment
- ⚙️ Event-driven and scheduled workflows using **Kestra**
- 🗺️ Location-aware issue context (Mumbai-focused)
- 🐦 Automated generation of social-media–ready content for escalation
- 📦 Scalable backend with FastAPI, PostgreSQL, and MinIO

---

## 🧱 Tech Stack

### Frontend

- React
- Vite
- TypeScript
- Tailwind CSS

### Backend

- FastAPI
- PostgreSQL
- SQLAlchemy

### AI & Automation

- Kestra (workflow orchestration)
- Gemini (multimodal image + text analysis)
- Mistral (structured JSON extraction)

### Infrastructure

- Docker & Docker Compose
- MinIO (object storage)

---

## 📂 Project Structure

```text
pothole-hacks/
│
├── backend/
│   ├── app/
│   │   ├── auth.py
│   │   ├── db.py
│   │   ├── kestra_client.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── index.html
│   ├── vite.config.ts
│   └── package.json
│
├── kestra_flows/
│   ├── issue-recognition.yaml
│   └── top3Posts.yaml
│
├── docker-compose.yml
├── .gitignore
└── README.md

```

### Kestra Workflows

1️⃣ Issue Recognition Flow (issue-recognition.yaml)
Triggered whenever a user creates a post.

- Steps:

```
Fetch post data from PostgreSQL

Download image from MinIO

Classify issue using Gemini (category, severity, authenticity)

Extract structured JSON using Mistral

Update post with AI scores and status
```

### Daily Escalation Flow (top3Posts.yaml)

Runs daily via cron.

-Steps:

```
Fetch all analysed posts from the current day

Rank them by composite score

Select the most critical issue

Generate a social-media–ready post

Store the generated communication for escalation
```

### Note: Automatic posting to Facebook was planned but not implemented due to Facebook Page verification limitations.

### Running with Docker

```
docker-compose up -d
Services
Kestra → http://localhost:8080

MinIO Console → http://localhost:9001

PostgreSQL → localhost:5432
```

### Running Backend Locally

```
python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

### Running Frontend

```
cd frontend
npm install
npm run dev
```

### AI Agent Usage (Kestra)

-The project uses Kestra’s built-in AI capabilities to:

-Summarize multimodal data (image + text)

-Rank issues based on severity and authenticity

-Make decisions on which issue should be escalated

-This enables transparent, automated civic prioritization without manual intervention.
