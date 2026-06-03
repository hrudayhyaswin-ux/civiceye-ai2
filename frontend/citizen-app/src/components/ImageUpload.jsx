/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { ImagePlus } from "lucide-react";

export default function ImageUpload({ files, onChange }) {
  return (
    <label className="upload-zone">
      <strong><ImagePlus size={18} /> Evidence images</strong>
      <span className="hint">{files.length ? `${files.length} file selected` : "Attach a photo or screenshot"}</span>
      <input type="file" accept="image/*" multiple onChange={(event) => onChange(Array.from(event.target.files || []).map((file) => file.name))} />
    </label>
  );
}

