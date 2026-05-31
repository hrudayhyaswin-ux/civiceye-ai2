import ComplaintDetailsDrawer from "../components/ComplaintDetailsDrawer";

export default function ComplaintView({ complaint }) {
  return <ComplaintDetailsDrawer complaint={complaint} onStatusChange={() => {}} />;
}

