import { useEffect, useMemo, useState } from "react";
import { getComplaints, getStats, updateComplaintStatus } from "../api/adminApi";
import ComplaintDetailsDrawer from "../components/ComplaintDetailsDrawer";
import ComplaintFilters from "../components/ComplaintFilters";
import ComplaintTable from "../components/ComplaintTable";
import DashboardStats from "../components/DashboardStats";

const initialFilters = { q: "", status: "All", priority: "All", department: "All" };

export default function Dashboard() {
  const [filters, setFilters] = useState(initialFilters);
  const [complaints, setComplaints] = useState([]);
  const [stats, setStats] = useState({});
  const [selected, setSelected] = useState(null);

  const params = useMemo(() => Object.fromEntries(Object.entries(filters).filter(([, value]) => value && value !== "All")), [filters]);

  useEffect(() => {
    getComplaints(params).then((items) => {
      setComplaints(items);
      setSelected((current) => current || items[0] || null);
    }).catch(() => setComplaints([]));
    getStats().then(setStats).catch(() => setStats({}));
  }, [params]);

  const changeStatus = async (status) => {
    const updated = await updateComplaintStatus(selected.ticket_id, status);
    setSelected(updated);
    setComplaints((items) => items.map((item) => item.ticket_id === updated.ticket_id ? updated : item));
    setStats(await getStats());
  };

  return (
    <>
      <header className="page-head">
        <div><h1>Operations dashboard</h1><p>Live AI triage stream for civic response teams.</p></div>
      </header>
      <DashboardStats stats={stats} />
      <ComplaintFilters filters={filters} onChange={setFilters} />
      <section className="content-grid">
        <ComplaintTable complaints={complaints} selected={selected} onSelect={setSelected} />
        <ComplaintDetailsDrawer complaint={selected} onStatusChange={changeStatus} />
      </section>
    </>
  );
}

