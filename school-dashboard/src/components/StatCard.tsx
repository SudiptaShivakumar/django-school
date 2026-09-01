interface Props {
  label: string;
  value: number | string;
  icon: string;
  color: string;
}

export function StatCard({ label, value, icon, color }: Props) {
  return (
    <div className={`stat-card ${color}`}>
      <span className="stat-icon">{icon}</span>
      <div>
        <div className="stat-value">{value}</div>
        <div className="stat-label">{label}</div>
      </div>
    </div>
  );
}
