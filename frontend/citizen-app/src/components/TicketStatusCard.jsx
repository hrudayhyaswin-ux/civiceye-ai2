import { prettyDate } from "../utils/helpers";

export default function TicketStatusCard({ complaint }) {
  if (!complaint) return null;

  return (
    <article className="status-card">
      <span className={`badge ${complaint.priority?.toLowerCase()}`}>{complaint.priority}</span>
      <h3>{complaint.title}</h3>
      <div className="status-row"><span>Status</span><strong>{complaint.status}</strong></div>
      <div className="status-row"><span>Department</span><strong>{complaint.department}</strong></div>
      <div className="status-row"><span>Ticket</span><strong>{complaint.ticket_id}</strong></div>
      <p>{complaint.summary}</p>
      <div className="timeline">
        {(complaint.timeline || []).map((item) => (
          <div key={item.at}>{prettyDate(item.at)} - {item.label}</div>
        ))}
      </div>
    </article>
  );
}

