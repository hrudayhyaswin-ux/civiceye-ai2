export default function PriorityBadge({ value }) {
  return <span className={`badge ${value?.toLowerCase()}`}>{value}</span>;
}

