export function formatTicket(ticketId) {
  return ticketId || "CE-000000";
}

export function prettyDate(value) {
  return new Intl.DateTimeFormat(undefined, { dateStyle: "medium", timeStyle: "short" }).format(new Date(value));
}

