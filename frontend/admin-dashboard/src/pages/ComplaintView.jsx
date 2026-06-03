/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import ComplaintDetailsDrawer from "../components/ComplaintDetailsDrawer";

export default function ComplaintView({ complaint }) {
  return <ComplaintDetailsDrawer complaint={complaint} onStatusChange={() => {}} />;
}

