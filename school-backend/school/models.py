from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    head_teacher_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.code} — {self.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    subject = models.CharField(max_length=100)
    joined_year = models.PositiveIntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.department.code})'


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    grade = models.CharField(max_length=20)
    enrollment_year = models.PositiveIntegerField()

    class Meta:
        ordering = ['roll_number']

    def __str__(self):
        return f'{self.roll_number} — {self.name}'
