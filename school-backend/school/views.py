from rest_framework import viewsets

from .models import Department, Student, Teacher
from .serializers import DepartmentSerializer, StudentSerializer, TeacherSerializer


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    search_fields = ['name', 'code', 'head_teacher_name']
    ordering_fields = ['name', 'code']


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related('department').all()
    serializer_class = TeacherSerializer
    filterset_fields = ['department']
    search_fields = ['name', 'email', 'subject']
    ordering_fields = ['name', 'joined_year']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('department').all()
    serializer_class = StudentSerializer
    filterset_fields = ['department', 'grade']
    search_fields = ['name', 'email', 'roll_number']
    ordering_fields = ['name', 'roll_number', 'enrollment_year']
