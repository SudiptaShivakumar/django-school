export interface Department {
  id: number;
  name: string;
  code: string;
  head_teacher_name: string;
  teacher_count: number;
  student_count: number;
}

export interface Teacher {
  id: number;
  name: string;
  email: string;
  phone: string;
  department: number;
  department_name: string;
  subject: string;
  joined_year: number;
}

export interface Student {
  id: number;
  name: string;
  email: string;
  roll_number: string;
  department: number;
  department_name: string;
  grade: string;
  enrollment_year: number;
}

export interface SchoolStats {
  totalDepartments: number;
  totalTeachers: number;
  totalStudents: number;
  ratio: number;
}
