/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { languages } from "../utils/constants";

export default function LanguageToggle({ value, onChange }) {
  return (
    <div className="language-toggle" aria-label="Language">
      {languages.map((language) => (
        <button key={language.code} className={value === language.code ? "active" : ""} onClick={() => onChange(language.code)}>
          {language.label}
        </button>
      ))}
    </div>
  );
}

