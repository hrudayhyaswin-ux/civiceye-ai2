/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { api } from "./axios";

export async function submitComplaint(payload) {
  const { data } = await api.post("/complaints", payload);
  return data.data;
}

export async function trackComplaint(ticketId) {
  const { data } = await api.get(`/complaints/${ticketId}`);
  return data.data;
}

