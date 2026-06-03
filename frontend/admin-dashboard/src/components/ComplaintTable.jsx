/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import PriorityBadge from "./PriorityBadge";

export default function ComplaintTable({ complaints, selected, onSelect }) {
  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr><th>Ticket</th><th>Issue</th><th>Department</th><th>Priority</th><th>Status</th></tr>
        </thead>
        <tbody>
          {complaints.map((item) => (
            <tr key={item.ticket_id} className={selected?.ticket_id === item.ticket_id ? "selected" : ""} onClick={() => onSelect(item)}>
              <td className="ticket">{item.ticket_id}</td>
              <td>{item.title}<div className="muted">{item.location?.address || "Location pending"}</div></td>
              <td>{item.department}</td>
              <td><PriorityBadge value={item.priority} /></td>
              <td>{item.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

