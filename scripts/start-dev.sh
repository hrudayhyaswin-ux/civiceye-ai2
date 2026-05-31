#!/usr/bin/env bash
set -euo pipefail

echo "Start these in separate terminals:"
echo "1. cd backend && python run.py"
echo "2. cd ai-service && uvicorn main:app --reload --port 8001"
echo "3. cd frontend/citizen-app && npm install && npm run dev"
echo "4. cd frontend/admin-dashboard && npm install && npm run dev"

