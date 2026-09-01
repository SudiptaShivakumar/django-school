import { useState } from 'react';
import type { Student } from '../types';

export function StudentsTable({ students }: { students: Student[] }) {
  const [search, setSearch] = useState('');
  const [dept, setDept] = useState('');
  const [grade, setGrade] = useState('');

  const depts = [...new Set(students.map((s) => s.department_name))].sort();
  const grades = [...new Set(students.map((s) => s.grade))].sort();

  const rows = students.filter((s) => {
    const q = search.toLowerCase();
    return (
      (!q || s.name.toLowerCase().includes(q) || s.email.toLowerCase().includes(q) || s.roll_number.toLowerCase().includes(q)) &&
      (!dept || s.department_name === dept) &&
      (!grade || s.grade === grade)
    );
  });

  return (
    <section className="section">
      <h2 className="section-title">Students</h2>
      <div className="controls">
        <input className="search" placeholder="Search name, email, roll no…" value={search} onChange={(e) => setSearch(e.target.value)} />
        <select className="filter" value={dept} onChange={(e) => setDept(e.target.value)}>
          <option value="">All Departments</option>
          {depts.map((d) => <option key={d}>{d}</option>)}
        </select>
        <select className="filter" value={grade} onChange={(e) => setGrade(e.target.value)}>
          <option value="">All Grades</option>
          {grades.map((g) => <option key={g}>{g}</option>)}
        </select>
      </div>
      <div className="table-wrap">
        <table className="table">
          <thead><tr><th>Roll No.</th><th>Name</th><th>Email</th><th>Department</th><th>Grade</th><th>Enrolled</th></tr></thead>
          <tbody>
            {rows.length === 0
              ? <tr><td colSpan={6} className="empty">No students found</td></tr>
              : rows.map((s) => (
                <tr key={s.id}>
                  <td className="mono">{s.roll_number}</td>
                  <td className="bold">{s.name}</td>
                  <td>{s.email}</td>
                  <td><span className="badge green">{s.department_name}</span></td>
                  <td><span className="badge purple">{s.grade}</span></td>
                  <td>{s.enrollment_year}</td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
      <p className="count">Showing {rows.length} of {students.length}</p>
    </section>
  );
}
