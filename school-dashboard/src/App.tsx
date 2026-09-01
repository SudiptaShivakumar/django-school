import { useState } from 'react';
import './App.css';
import { DepartmentCards } from './components/DepartmentCards';
import { StatCard } from './components/StatCard';
import { StudentsTable } from './components/StudentsTable';
import { TeachersTable } from './components/TeachersTable';
import { useSchoolData } from './hooks/useSchoolData';

type Tab = 'overview' | 'teachers' | 'students';

export default function App() {
  const { departments, teachers, students, stats, loading, error, refetch } = useSchoolData();
  const [tab, setTab] = useState<Tab>('overview');

  return (
    <div className="app">
      <header className="header">
        <div className="header-inner">
          <div className="brand">
            <span className="brand-icon">🏫</span>
            <div>
              <h1 className="brand-title">School Dashboard</h1>
              <p className="brand-sub">Departments · Teachers · Students</p>
            </div>
          </div>
          <div className="header-actions">
            <a href="http://localhost:8000/api/" target="_blank" rel="noreferrer" className="btn-link">API ↗</a>
            <a href="http://localhost:8000/admin/" target="_blank" rel="noreferrer" className="btn-link">Admin ↗</a>
            <button className="btn-refresh" onClick={refetch} disabled={loading}>
              {loading ? 'Loading…' : '↻ Refresh'}
            </button>
          </div>
        </div>
      </header>

      <main className="main">
        {error && (
          <div className="error-bar">
            ⚠ Could not reach API: {error}
            <button onClick={refetch} className="btn-retry">Retry</button>
          </div>
        )}

        <div className="stats-row">
          <StatCard label="Departments" value={stats.totalDepartments} icon="🏢" color="c-blue" />
          <StatCard label="Teachers" value={stats.totalTeachers} icon="👩‍🏫" color="c-green" />
          <StatCard label="Students" value={stats.totalStudents} icon="🎒" color="c-purple" />
          <StatCard label="Student : Teacher" value={`${stats.ratio} : 1`} icon="📊" color="c-orange" />
        </div>

        <nav className="tabs">
          {(['overview', 'teachers', 'students'] as Tab[]).map((t) => (
            <button key={t} className={`tab ${tab === t ? 'tab-active' : ''}`} onClick={() => setTab(t)}>
              {t.charAt(0).toUpperCase() + t.slice(1)}
            </button>
          ))}
        </nav>

        {loading ? (
          <div className="loading">
            <div className="spinner" />
            <p>Fetching data from Django API…</p>
          </div>
        ) : (
          <>
            {tab === 'overview' && <DepartmentCards departments={departments} />}
            {tab === 'teachers' && <TeachersTable teachers={teachers} />}
            {tab === 'students' && <StudentsTable students={students} />}
          </>
        )}
      </main>
    </div>
  );
}
