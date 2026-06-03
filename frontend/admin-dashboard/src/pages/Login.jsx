import { useState } from "react";
import { api } from "../api/adminApi";

export default function Login({ onLogin }) {
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setBusy(true);
    setError("");
    console.log("Attempting login with API:", api.defaults.baseURL);
    try {
      const { data } = await api.post("/auth/login", { password });
      if (data.success) {
        localStorage.setItem("admin_token", data.data.token);
        onLogin();
      }
    } catch (err) {
      setError("Login failed. Check backend connection.");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="login-screen" style={{
      height: "100vh", display: "flex", alignItems: "center", justifyContent: "center",
      background: "linear-gradient(135deg, #071115, #0e171e)"
    }}>
      <form onSubmit={handleSubmit} className="metric" style={{ padding: "40px", width: "100%", maxWidth: "400px" }}>
        <h1 style={{ marginTop: 0, fontSize: "24px" }}>CivicEye Admin</h1>
        <p className="muted">Authorized personnel only.</p>
        <div className="filters" style={{ gridTemplateColumns: "1fr", padding: 0, marginTop: "24px" }}>
          <input 
            type="password" 
            placeholder="Enter admin password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
            autoFocus
          />
        </div>
        {error && <p style={{ color: "var(--coral)", fontSize: "14px", marginTop: "12px" }}>{error}</p>}
        <button className="primary-btn" type="submit" disabled={busy} style={{ width: "100%", marginTop: "20px" }}>
          {busy ? "Authenticating..." : "Login to Command"}
        </button>
      </form>
    </div>
  );
}
