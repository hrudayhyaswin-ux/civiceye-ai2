/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { departments, priorities, statuses } from "../utils/constants";

export default function ComplaintFilters({ filters, onChange }) {
  const update = (key, value) => onChange({ ...filters, [key]: value });
  return (
    <section className="filters">
      <input value={filters.q} onChange={(event) => update("q", event.target.value)} placeholder="Search ticket, title, ward" />
      <select value={filters.status} onChange={(event) => update("status", event.target.value)}>{statuses.map((item) => <option key={item}>{item}</option>)}</select>
      <select value={filters.priority} onChange={(event) => update("priority", event.target.value)}>{priorities.map((item) => <option key={item}>{item}</option>)}</select>
      <select value={filters.department} onChange={(event) => update("department", event.target.value)}>{departments.map((item) => <option key={item}>{item}</option>)}</select>
    </section>
  );
}

