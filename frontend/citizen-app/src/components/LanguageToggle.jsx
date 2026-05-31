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

