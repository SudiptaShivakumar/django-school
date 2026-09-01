import { useState } from 'react';
import type { Teacher } from '../types';

export function TeachersTable({ teachers }: { teachers: Teacher[] }) {
  const [search, setSearch] = useState('');
  const [dept, setDept] = useState('');

  const depts = [...new Set(teachers.map((t) => t.department_name))].sort();

  const rows = teachers.filter((t) => {
    const q = search.toLowerCase();
    return (
      (!q || t.name.toLowerCase().includes(q) || t.email.toLowerCase().includes(q) || t.subject.toLowerCase().includes(q)) &&
      (!dept || t.department_name === dept)
    );
  });

  return (
    <section className="section">
      <h2 className="section-title">Teachers</h2>
      <div className="controls">
        <input className="search" placeholder="Search name, email, subject…" value={search} onChange={(e) => setSearch(e.target.value)} />
        <select className="filter" value={dept} onChange={(e) => setDept(e.target.value)}>
          <option value="">All Departments</option>
          {depts.map((d) => <option key={d}>{d}</option>)}
        </select>
      </div>
      <div className="table-wrap">
        <table className="table">
          <thead><tr><th>#</th><th>Name</th><th>Email</th><th>Phone</th><th>Department</th><th>Subject</th><th>Joined</th></tr></thead>
          <tbody>
            {rows.length === 0
              ? <tr><td colSpan={7} className="empty">No teachers found</td></tr>
              : rows.map((t) => (
                <tr key={t.id}>
                  <td>{t.id}</td>
                  <td className="bold">{t.name}</td>
                  <td>{t.email}</td>
                  <td>{t.phone}</td>
                  <td><span className="badge blue">{t.department_name}</span></td>
                  <td>{t.subject}</td>
                  <td>{t.joined_year}</td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
      <p className="count">Showing {rows.length} of {teachers.length}</p>
    </section>
  );
}
