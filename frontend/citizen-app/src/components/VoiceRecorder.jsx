/*
 * Copyright (C) 2026 Swecha
 * Licensed under the GNU Affero General Public License v3.0
 * See LICENSE file in the project root for full license information.
 */

import { useEffect, useState } from "react";
import { Mic, Square, Loader2 } from "lucide-react";
import useVoiceRecorder from "../hooks/useVoiceRecorder";

export default function VoiceRecorder({ onTranscript, language }) {
  const { isRecording, audioBlob, toggleRecording } = useVoiceRecorder();
  const [isProcessing, setIsProcessing] = useState(false);
  const [transcript, setTranscript] = useState("");

  useEffect(() => {
    if (audioBlob) {
      handleTranscription(audioBlob);
    }
  }, [audioBlob]);

  const handleTranscription = async (blob) => {
    setIsProcessing(true);
    setTranscript("Processing voice...");
    
    try {
      // In a real app, we'd upload this to the backend.
      // For now, let's prepare the form to handle the blob.
      onTranscript(blob); 
      setTranscript("Voice note attached");
    } catch (err) {
      console.error("Transcription error:", err);
      setTranscript("Transcription failed");
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="recorder">
      <div>
        <strong>{isRecording ? "Listening..." : "Voice note"}</strong>
        <div className="hint">
          {isRecording ? "Recording your issue..." : (isProcessing ? "Analyzing audio..." : transcript || "Optional voice context")}
        </div>
      </div>
      {isRecording && <span className="recording-dot" />}
      <button 
        className={`icon-btn ${isRecording ? 'recording' : ''}`} 
        type="button" 
        onClick={toggleRecording} 
        disabled={isProcessing}
        aria-label={isRecording ? "Stop recording" : "Start recording"}
      >
        {isProcessing ? <Loader2 size={18} className="animate-spin" /> : (isRecording ? <Square size={18} /> : <Mic size={18} />)}
      </button>
    </div>
  );
}
