/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { useState } from "react";
import { Send } from "lucide-react";
import { submitComplaint } from "../api/complaintApi";
import { issueTypes } from "../utils/constants";
import ImageUpload from "./ImageUpload";
import LocationPicker from "./LocationPicker";
import VoiceRecorder from "./VoiceRecorder";

const emptyLocation = { address: "", lat: "", lng: "" };

export default function ComplaintForm({ language, onSuccess }) {
  const [form, setForm] = useState({ title: "", description: "", category_hint: "Road Damage", citizen_name: "", phone: "" });
  const [location, setLocation] = useState(emptyLocation);
  const [files, setFiles] = useState([]);
  const [voiceBlob, setVoiceBlob] = useState(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  const update = (key, value) => setForm((current) => ({ ...current, [key]: value }));

  const handleSubmit = async (event) => {
    event.preventDefault();
    setBusy(true);
    setError("");
    try {
      const formData = new FormData();
      formData.append("title", form.title);
      formData.append("description", form.description);
      formData.append("category_hint", form.category_hint);
      formData.append("citizen_name", form.citizen_name);
      formData.append("phone", form.phone);
      formData.append("language", language);
      formData.append("location", JSON.stringify(location));
      
      files.forEach((file, index) => {
        formData.append(`attachment_${index}`, file);
      });

      if (voiceBlob) {
        formData.append("voice_note", voiceBlob, "voice_note.webm");
      }

      const result = await submitComplaint(formData);
      onSuccess(result.ticket_id);
    } catch (err) {
      console.error("Submission error:", err);
      let msg = err.response?.data?.message || `Unable to submit (${err.message}).`;
      if (err.message === "Network Error") {
        msg = "Network Error: Please click 'Click to Continue' at https://civiceye-india-server.loca.lt first, then try again.";
      }
      setError(msg);
    } finally {
      setBusy(false);
    }
  };

  return (
    <form className="complaint-form" onSubmit={handleSubmit}>
      <div className="grid-2">
        <label className="field">
          Issue type
          <select value={form.category_hint} onChange={(event) => update("category_hint", event.target.value)}>
            {issueTypes.map((type) => <option key={type}>{type}</option>)}
          </select>
        </label>
        <label className="field">
          Title
          <input required value={form.title} onChange={(event) => update("title", event.target.value)} placeholder="Open manhole near bus stop" />
        </label>
      </div>
      <label className="field">
        Description
        <textarea required={!voiceBlob} value={form.description} onChange={(event) => update("description", event.target.value)} placeholder="Describe what happened, who is affected, and how urgent it is." />
      </label>
      <div className="grid-2">
        <label className="field">
          Name
          <input value={form.citizen_name} onChange={(event) => update("citizen_name", event.target.value)} placeholder="Optional" />
        </label>
        <label className="field">
          Phone
          <input value={form.phone} onChange={(event) => update("phone", event.target.value)} placeholder="Optional" />
        </label>
      </div>
      <LocationPicker value={location} onChange={setLocation} />
      <div className="grid-2">
        <VoiceRecorder onTranscript={setVoiceBlob} language={language} />
        <ImageUpload files={files} onChange={setFiles} />
      </div>
      {error && <div className="hint">{error}</div>}
      <button className="primary-btn" type="submit" disabled={busy}>
        <Send size={18} /> {busy ? "Routing" : "Submit complaint"}
      </button>
    </form>
  );
}

