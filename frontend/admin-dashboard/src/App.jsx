import { useState } from "react";
import { BarChart3, LayoutDashboard, RadioTower } from "lucide-react";
import Dashboard from "./pages/Dashboard.jsx";
import Analytics from "./pages/Analytics.jsx";

export default function App() {
  const [page, setPage] = useState("dashboard");

  return (
    <div className="admin-shell">
      <aside className="sidebar">
        <div className="brand"><RadioTower size={28} /><span>CivicEye Command</span></div>
        <button className={page === "dashboard" ? "active" : ""} onClick={() => setPage("dashboard")}><LayoutDashboard size={18} /> Dashboard</button>
        <button className={page === "analytics" ? "active" : ""} onClick={() => setPage("analytics")}><BarChart3 size={18} /> Analytics</button>
      </aside>
      <main>
        {page === "dashboard" ? <Dashboard /> : <Analytics />}
      </main>
    </div>
  );
}

