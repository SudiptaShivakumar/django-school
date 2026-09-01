from rest_framework import serializers

from .models import Department, Student, Teacher


class DepartmentSerializer(serializers.ModelSerializer):
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'code', 'head_teacher_name', 'created_at', 'teacher_count', 'student_count']

    def get_teacher_count(self, obj):
        return obj.teachers.count()

    def get_student_count(self, obj):
        return obj.students.count()


class TeacherSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'phone', 'department', 'department_name', 'subject', 'joined_year']


class StudentSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'roll_number', 'department', 'department_name', 'grade', 'enrollment_year']
