import { useEffect, useState } from 'react';
import { api } from '../api/schoolApi';
import type { Department, SchoolStats, Student, Teacher } from '../types';

interface SchoolData {
  departments: Department[];
  teachers: Teacher[];
  students: Student[];
  stats: SchoolStats;
  loading: boolean;
  error: string | null;
  refetch: () => void;
}

export function useSchoolData(): SchoolData {
  const [departments, setDepartments] = useState<Department[]>([]);
  const [teachers, setTeachers] = useState<Teacher[]>([]);
  const [students, setStudents] = useState<Student[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [tick, setTick] = useState(0);

  useEffect(() => {
    setLoading(true);
    setError(null);
    Promise.all([api.getDepartments(), api.getTeachers(), api.getStudents()])
      .then(([deps, tchs, stds]) => {
        setDepartments(deps);
        setTeachers(tchs);
        setStudents(stds);
      })
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false));
  }, [tick]);

  const stats: SchoolStats = {
    totalDepartments: departments.length,
    totalTeachers: teachers.length,
    totalStudents: students.length,
    ratio: teachers.length ? Math.round(students.length / teachers.length) : 0,
  };

  return { departments, teachers, students, stats, loading, error, refetch: () => setTick((t) => t + 1) };
}
