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
      {complaint.voice_note_path && (
        <div style={{ marginTop: "16px", padding: "12px", background: "rgba(255,255,255,.05)", borderRadius: "8px" }}>
          <span style={{ display: "block", marginBottom: "8px", fontSize: "13px", color: "var(--muted)" }}>Voice recording</span>
          <audio controls src={`${import.meta.env.VITE_API_BASE_URL}/uploads/media/${complaint.voice_note_path}`} style={{ width: "100%" }} />
        </div>
      )}
      {complaint.attachments?.length > 0 && (
        <div style={{ marginTop: "16px" }}>
          <span style={{ display: "block", marginBottom: "8px", fontSize: "13px", color: "var(--muted)" }}>Attachments</span>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(2, 1fr)", gap: "8px" }}>
            {complaint.attachments.map((file, i) => (
              <a key={i} href={`${import.meta.env.VITE_API_BASE_URL}/uploads/media/${file}`} target="_blank" rel="noreferrer">
                <img 
                  src={`${import.meta.env.VITE_API_BASE_URL}/uploads/media/${file}`} 
                  alt="attachment" 
                  style={{ width: "100%", height: "100px", objectFit: "cover", borderRadius: "4px", border: "1px solid var(--line)" }} 
                />
              </a>
            ))}
          </div>
        </div>
      )}
      <div className="hero-actions">
        <button className="primary-btn" onClick={() => onStatusChange("Assigned")}><Send size={18} /> Assign</button>
        <button className="ghost-btn" onClick={() => onStatusChange("Resolved")}><CheckCircle2 size={18} /> Resolve</button>
      </div>
    </aside>
  );
}

