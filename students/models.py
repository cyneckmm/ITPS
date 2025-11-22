from django.db import models
from django.contrib.auth.models import User

class StudentInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        null=True,      
        blank=True      
    )
    student_id = models.CharField(max_length=50, unique=True) 
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    permanent_address = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=100, blank=True)
    barangay = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.full_name


class CourseEnrollment(models.Model):
    student_id = models.CharField(max_length=50)   
    enrollment_id = models.CharField(max_length=50, blank=True)

    semester = models.CharField(max_length=50, blank=True)
    course_code = models.CharField(max_length=50, blank=True)
    course_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.course_name} - {self.student_id}"


class ClassSchedule(models.Model):
    enrollment_id = models.CharField(max_length=50) 
    professor_name = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    course_code = models.CharField(max_length=50, blank=True)
    day = models.CharField(max_length=50, blank=True)
    room_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Schedule for {self.enrollment_id}"


class GuardianInformation(models.Model):
    student_id = models.CharField(max_length=50) 
    guardian_name = models.CharField(max_length=100)
    guardian_id = models.CharField(max_length=50, blank=True)
    guardian_address = models.CharField(max_length=200, blank=True)
    relationship = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.guardian_name

# Create your views here.

