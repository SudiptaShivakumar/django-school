import type { Department } from '../types';

export function DepartmentCards({ departments }: { departments: Department[] }) {
  return (
    <section className="section">
      <h2 className="section-title">Departments</h2>
      <div className="dept-grid">
        {departments.map((d) => (
          <div key={d.id} className="dept-card">
            <div className="dept-top">
              <span className="dept-code">{d.code}</span>
              <span className="dept-name">{d.name}</span>
            </div>
            <p className="dept-head">Head: {d.head_teacher_name || '—'}</p>
            <div className="dept-counts">
              <div className="dept-count">
                <span className="count-val">{d.teacher_count}</span>
                <span className="count-lbl">Teachers</span>
              </div>
              <div className="dept-count">
                <span className="count-val">{d.student_count}</span>
                <span className="count-lbl">Students</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
