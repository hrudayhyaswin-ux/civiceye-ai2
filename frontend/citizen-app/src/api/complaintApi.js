import { api } from "./axios";

export async function submitComplaint(payload) {
  const config = {};
  if (payload instanceof FormData) {
    config.headers = { "Content-Type": "multipart/form-data" };
  }
  const { data } = await api.post("/complaints", payload, config);
  return data.data;
}

export async function trackComplaint(ticketId) {
  const { data } = await api.get(`/complaints/${ticketId}`);
  return data.data;
}

