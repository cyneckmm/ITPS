from django.contrib import admin
from .models import StudentInformation, CourseEnrollment, ClassSchedule, GuardianInformation

admin.site.register(StudentInformation)
admin.site.register(CourseEnrollment)
admin.site.register(ClassSchedule)
admin.site.register(GuardianInformation)

# Register your models here.
