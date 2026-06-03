import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:5001/api",
  timeout: 12000,
  headers: {
    "Bypass-Tunnel-Reminder": "true",
  }
});

