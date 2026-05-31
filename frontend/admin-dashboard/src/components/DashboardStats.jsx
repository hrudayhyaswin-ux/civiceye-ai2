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

