from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentInformation, CourseEnrollment, ClassSchedule, GuardianInformation

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class StudentInformationForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = '__all__'  

class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = ['student_id', 'enrollment_id', 'semester', 'course_code', 'course_name']

class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['enrollment_id', 'professor_name', 'department', 'course_code', 'day', 'room_number']

class GuardianInformationForm(forms.ModelForm):
    class Meta:
        model = GuardianInformation
        fields = ['student_id', 'guardian_name', 'guardian_id', 'guardian_address', 'relationship']
