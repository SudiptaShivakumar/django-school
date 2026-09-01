import type { Department, Student, Teacher } from '../types';

const BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

async function get<T>(path: string, params?: Record<string, string>): Promise<T> {
  const url = new URL(`${BASE}${path}`);
  if (params) Object.entries(params).forEach(([k, v]) => v && url.searchParams.set(k, v));
  const res = await fetch(url.toString());
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json() as Promise<T>;
}

export const api = {
  getDepartments: () => get<Department[]>('/departments/'),
  getTeachers: (params?: Record<string, string>) => get<Teacher[]>('/teachers/', params),
  getStudents: (params?: Record<string, string>) => get<Student[]>('/students/', params),
};
