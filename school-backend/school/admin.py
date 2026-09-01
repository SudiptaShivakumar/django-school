from django.contrib import admin

from .models import Department, Student, Teacher


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'head_teacher_name', 'created_at']
    search_fields = ['name', 'code']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'department', 'subject', 'joined_year']
    list_filter = ['department']
    search_fields = ['name', 'email', 'subject']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll_number', 'name', 'email', 'department', 'grade', 'enrollment_year']
    list_filter = ['department', 'grade']
    search_fields = ['name', 'email', 'roll_number']
