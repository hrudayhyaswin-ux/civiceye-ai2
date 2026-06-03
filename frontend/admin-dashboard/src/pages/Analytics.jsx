/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

export default function Analytics() {
  const rows = [
    ["Roads", 82], ["Sanitation", 64], ["Utilities", 47], ["Water", 38], ["Public Safety", 24],
  ];
  return (
    <>
      <header className="page-head">
        <div><h1>Analytics</h1><p>Department load and routing confidence for the current demo window.</p></div>
      </header>
      <section className="chart-grid">
        <article className="chart-panel">
          <h2>Department load</h2>
          {rows.map(([label, value]) => <div key={label} className="bar" style={{ width: `${value}%` }}>{label} {value}</div>)}
        </article>
        <article className="chart-panel">
          <h2>AI routing health</h2>
          <div className="metric"><span>Confidence</span><strong>88%</strong></div>
          <div className="metric"><span>Median response target</span><strong>4h</strong></div>
        </article>
      </section>
    </>
  );
}

