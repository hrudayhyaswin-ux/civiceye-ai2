import { CheckCircle2, Send } from "lucide-react";
import PriorityBadge from "./PriorityBadge";

export default function ComplaintDetailsDrawer({ complaint, onStatusChange }) {
  if (!complaint) {
    return <aside className="drawer"><h2>Complaint details</h2><p className="muted">Select a ticket from the stream.</p></aside>;
  }
  return (
    <aside className="drawer">
      <PriorityBadge value={complaint.priority} />
      <h2>{complaint.title}</h2>
      <p className="muted">{complaint.summary}</p>
      <div className="detail-row"><span>Ticket</span><strong>{complaint.ticket_id}</strong></div>
      <div className="detail-row"><span>Status</span><strong>{complaint.status}</strong></div>
      <div className="detail-row"><span>Department</span><strong>{complaint.department}</strong></div>
      <div className="detail-row"><span>Duplicate</span><strong>{complaint.duplicate_confidence}%</strong></div>
      <div className="detail-row"><span>Address</span><strong>{complaint.location?.address || "Pending"}</strong></div>
      <div className="hero-actions">
        <button className="primary-btn" onClick={() => onStatusChange("Assigned")}><Send size={18} /> Assign</button>
        <button className="ghost-btn" onClick={() => onStatusChange("Resolved")}><CheckCircle2 size={18} /> Resolve</button>
      </div>
    </aside>
  );
}

