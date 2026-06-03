/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { ArrowRight, Satellite } from "lucide-react";

export default function Home({ onStart }) {
  return (
    <section className="hero">
      <div className="hero-copy">
        <h1>CivicEye AI</h1>
        <p>Report city issues with rich context, live location signals, and AI-assisted routing that moves complaints to the right department faster.</p>
        <div className="hero-actions">
          <button className="primary-btn" onClick={onStart}><Satellite size={18} /> Report issue</button>
          <button className="ghost-btn" onClick={() => window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" })}>View trust layer <ArrowRight size={18} /></button>
        </div>
      </div>
      <div className="city-scan" aria-label="City intelligence visual">
        <span className="tower t1" /><span className="tower t2" /><span className="tower t3" /><span className="tower t4" /><span className="tower t5" />
        <span className="pulse p1" /><span className="pulse p2" /><span className="pulse p3" />
      </div>
    </section>
  );
}

