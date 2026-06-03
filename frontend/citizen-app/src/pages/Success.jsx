/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { Plus, Search } from "lucide-react";

export default function Success({ ticketId, onTrack, onNew }) {
  return (
    <section className="success panel">
      <h2>Complaint routed</h2>
      <p>Your ticket has been created and sent into the triage stream.</p>
      <div className="success-code">{ticketId}</div>
      <div className="hero-actions" style={{ justifyContent: "center" }}>
        <button className="primary-btn" onClick={onTrack}><Search size={18} /> Track status</button>
        <button className="ghost-btn" onClick={onNew}><Plus size={18} /> New report</button>
      </div>
    </section>
  );
}

