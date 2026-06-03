/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

export function formatTicket(ticketId) {
  return ticketId || "CE-000000";
}

export function prettyDate(value) {
  return new Intl.DateTimeFormat(undefined, { dateStyle: "medium", timeStyle: "short" }).format(new Date(value));
}

