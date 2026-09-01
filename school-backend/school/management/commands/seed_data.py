from django.core.management.base import BaseCommand

from school.models import Department, Student, Teacher

DEPARTMENTS = [
    {'name': 'Mathematics', 'code': 'MATH', 'head_teacher_name': 'Alice Johnson'},
    {'name': 'Science', 'code': 'SCI', 'head_teacher_name': 'Carol White'},
    {'name': 'English', 'code': 'ENG', 'head_teacher_name': 'Eva Green'},
    {'name': 'History', 'code': 'HIST', 'head_teacher_name': 'Grace Kim'},
    {'name': 'Computer Science', 'code': 'CS', 'head_teacher_name': 'Iris Chen'},
]

TEACHERS = [
    {'name': 'Alice Johnson', 'email': 'alice@school.edu', 'phone': '555-0101', 'dept_code': 'MATH', 'subject': 'Algebra', 'joined_year': 2015},
    {'name': 'Bob Smith', 'email': 'bob@school.edu', 'phone': '555-0102', 'dept_code': 'MATH', 'subject': 'Calculus', 'joined_year': 2018},
    {'name': 'Carol White', 'email': 'carol@school.edu', 'phone': '555-0103', 'dept_code': 'SCI', 'subject': 'Physics', 'joined_year': 2012},
    {'name': 'David Brown', 'email': 'david@school.edu', 'phone': '555-0104', 'dept_code': 'SCI', 'subject': 'Chemistry', 'joined_year': 2019},
    {'name': 'Eva Green', 'email': 'eva@school.edu', 'phone': '555-0105', 'dept_code': 'ENG', 'subject': 'Literature', 'joined_year': 2016},
    {'name': 'Frank Lee', 'email': 'frank@school.edu', 'phone': '555-0106', 'dept_code': 'ENG', 'subject': 'Grammar', 'joined_year': 2020},
    {'name': 'Grace Kim', 'email': 'grace@school.edu', 'phone': '555-0107', 'dept_code': 'HIST', 'subject': 'World History', 'joined_year': 2014},
    {'name': 'Henry Park', 'email': 'henry@school.edu', 'phone': '555-0108', 'dept_code': 'HIST', 'subject': 'Civics', 'joined_year': 2021},
    {'name': 'Iris Chen', 'email': 'iris@school.edu', 'phone': '555-0109', 'dept_code': 'CS', 'subject': 'Algorithms', 'joined_year': 2017},
    {'name': 'Jack Turner', 'email': 'jack@school.edu', 'phone': '555-0110', 'dept_code': 'CS', 'subject': 'Web Development', 'joined_year': 2022},
]

STUDENTS = [
    {'name': 'Liam Adams', 'email': 'liam.a@student.edu', 'roll': 'S001', 'dept_code': 'MATH', 'grade': '10th', 'year': 2023},
    {'name': 'Mia Baker', 'email': 'mia.b@student.edu', 'roll': 'S002', 'dept_code': 'MATH', 'grade': '11th', 'year': 2022},
    {'name': 'Noah Clark', 'email': 'noah.c@student.edu', 'roll': 'S003', 'dept_code': 'SCI', 'grade': '10th', 'year': 2023},
    {'name': 'Olivia Davis', 'email': 'olivia.d@student.edu', 'roll': 'S004', 'dept_code': 'SCI', 'grade': '12th', 'year': 2021},
    {'name': 'Paul Evans', 'email': 'paul.e@student.edu', 'roll': 'S005', 'dept_code': 'ENG', 'grade': '9th', 'year': 2024},
    {'name': 'Quinn Foster', 'email': 'quinn.f@student.edu', 'roll': 'S006', 'dept_code': 'ENG', 'grade': '11th', 'year': 2022},
    {'name': 'Ruby Garcia', 'email': 'ruby.g@student.edu', 'roll': 'S007', 'dept_code': 'HIST', 'grade': '10th', 'year': 2023},
    {'name': 'Sam Harris', 'email': 'sam.h@student.edu', 'roll': 'S008', 'dept_code': 'CS', 'grade': '12th', 'year': 2021},
    {'name': 'Tara Irving', 'email': 'tara.i@student.edu', 'roll': 'S009', 'dept_code': 'CS', 'grade': '11th', 'year': 2022},
    {'name': 'Uma Jackson', 'email': 'uma.j@student.edu', 'roll': 'S010', 'dept_code': 'SCI', 'grade': '9th', 'year': 2024},
    {'name': 'Victor King', 'email': 'victor.k@student.edu', 'roll': 'S011', 'dept_code': 'MATH', 'grade': '12th', 'year': 2021},
    {'name': 'Wendy Lane', 'email': 'wendy.l@student.edu', 'roll': 'S012', 'dept_code': 'SCI', 'grade': '11th', 'year': 2022},
    {'name': 'Xander Moore', 'email': 'xander.m@student.edu', 'roll': 'S013', 'dept_code': 'HIST', 'grade': '9th', 'year': 2024},
    {'name': 'Yara Nolan', 'email': 'yara.n@student.edu', 'roll': 'S014', 'dept_code': 'CS', 'grade': '10th', 'year': 2023},
    {'name': 'Zane Owen', 'email': 'zane.o@student.edu', 'roll': 'S015', 'dept_code': 'ENG', 'grade': '12th', 'year': 2021},
]


class Command(BaseCommand):
    help = 'Seed the database with sample school data'

    def handle(self, *args, **options):
        dept_map = {}
        for d in DEPARTMENTS:
            obj, created = Department.objects.get_or_create(
                code=d['code'],
                defaults={'name': d['name'], 'head_teacher_name': d['head_teacher_name']},
            )
            dept_map[d['code']] = obj
            self.stdout.write(f"  {'Created' if created else 'Exists'} department: {obj}")

        for t in TEACHERS:
            obj, created = Teacher.objects.get_or_create(
                email=t['email'],
                defaults={
                    'name': t['name'],
                    'phone': t['phone'],
                    'department': dept_map[t['dept_code']],
                    'subject': t['subject'],
                    'joined_year': t['joined_year'],
                },
            )
            self.stdout.write(f"  {'Created' if created else 'Exists'} teacher: {obj}")

        for s in STUDENTS:
            obj, created = Student.objects.get_or_create(
                roll_number=s['roll'],
                defaults={
                    'name': s['name'],
                    'email': s['email'],
                    'department': dept_map[s['dept_code']],
                    'grade': s['grade'],
                    'enrollment_year': s['year'],
                },
            )
            self.stdout.write(f"  {'Created' if created else 'Exists'} student: {obj}")

        self.stdout.write(self.style.SUCCESS(
            f'\nDone: {Department.objects.count()} departments, '
            f'{Teacher.objects.count()} teachers, '
            f'{Student.objects.count()} students.'
        ))
