/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "https://civiceye-india-server.loca.lt/api",
  timeout: 12000,
  headers: {
    "Bypass-Tunnel-Reminder": "true",
    "Accept": "application/json",
  }
});

export async function getComplaints(filters = {}) {
  const { data } = await api.get("/admin/complaints", { params: filters });
  return data.data;
}

export async function getStats() {
  const { data } = await api.get("/admin/stats");
  return data.data;
}

export async function updateComplaintStatus(ticketId, status) {
  const { data } = await api.patch(`/admin/complaints/${ticketId}`, { status });
  return data.data;
}

