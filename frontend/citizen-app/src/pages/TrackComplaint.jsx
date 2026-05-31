import { useState } from "react";
import { Search } from "lucide-react";
import { trackComplaint } from "../api/complaintApi";
import TicketStatusCard from "../components/TicketStatusCard";

export default function TrackComplaint({ initialTicket = "" }) {
  const [ticketId, setTicketId] = useState(initialTicket);
  const [complaint, setComplaint] = useState(null);
  const [error, setError] = useState("");

  const handleTrack = async (event) => {
    event.preventDefault();
    setError("");
    try {
      setComplaint(await trackComplaint(ticketId));
    } catch (err) {
      setError(err.response?.data?.message || "Ticket not found");
      setComplaint(null);
    }
  };

  return (
    <section className="workbench">
      <div className="panel">
        <h2>Track ticket</h2>
        <p>Enter a CivicEye public ticket ID to view routing and current status.</p>
        <form className="complaint-form" onSubmit={handleTrack}>
          <label className="field">
            Ticket ID
            <input required value={ticketId} onChange={(event) => setTicketId(event.target.value.toUpperCase())} placeholder="CE-123456" />
          </label>
          {error && <div className="hint">{error}</div>}
          <button className="primary-btn"><Search size={18} /> Track</button>
        </form>
      </div>
      <div className="side-rail">
        <TicketStatusCard complaint={complaint} />
      </div>
    </section>
  );
}

