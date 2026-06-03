import { useState, useRef } from "react";

export default function useVoiceRecorder() {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);

  const startRecording = async () => {
    // SECURITY CHECK: Browsers only allow mic on localhost or https
    if (!window.isSecureContext) {
      const msg = "Microphone blocked for security.\n\n" +
                  "To fix this on Mac or Windows:\n" +
                  "1. Go to: chrome://flags/#unsafely-treat-insecure-origin-as-secure\n" +
                  "2. Set it to 'Enabled'\n" +
                  "3. Add 'http://192.168.106.63:5173' to the list\n" +
                  "4. Relaunch your browser.";
      alert(msg);
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      chunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          chunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: "audio/webm" });
        setAudioBlob(blob);
        stream.getTracks().forEach((track) => track.stop());
      };

      mediaRecorder.start();
      setIsRecording(true);
      setAudioBlob(null);
    } catch (err) {
      console.error("Error accessing microphone:", err);
      if (err.name === 'NotAllowedError') {
        alert("Permission denied. Please allow microphone access in your browser settings.");
      } else {
        alert("Could not access microphone. Please check your device settings.");
      }
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }
  };

  const toggleRecording = () => {
    if (isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  return { isRecording, audioBlob, toggleRecording };
}
