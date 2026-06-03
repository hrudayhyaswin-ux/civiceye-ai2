/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import ComplaintForm from "../components/ComplaintForm";

export default function SubmitComplaint({ language, onSuccess }) {
  return (
    <section className="workbench">
      <div className="panel">
        <h2>Signal a civic issue</h2>
        <p>Submit the problem once. CivicEye AI classifies it, assigns priority, and creates a public tracking ticket.</p>
        <ComplaintForm language={language} onSuccess={onSuccess} />
      </div>
      <aside className="side-rail">
        <div className="metric"><strong>47 sec</strong><span className="hint">average AI triage time</span></div>
        <div className="metric"><strong>6</strong><span className="hint">supported civic departments</span></div>
        <div className="metric"><strong>92%</strong><span className="hint">demo duplicate match precision target</span></div>
      </aside>
    </section>
  );
}

