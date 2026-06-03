/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

export default function DashboardStats({ stats }) {
  const items = [
    ["Open", stats.open],
    ["High Priority", stats.high_priority],
    ["Resolved", stats.resolved],
    ["Duplicate Risk", `${stats.duplicate_risk}%`],
  ];
  return (
    <section className="stats">
      {items.map(([label, value]) => (
        <article className="metric" key={label}>
          <span>{label}</span>
          <strong>{value ?? 0}</strong>
        </article>
      ))}
    </section>
  );
}

