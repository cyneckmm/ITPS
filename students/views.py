from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import (
    SignUpForm, StudentInformationForm, CourseEnrollmentForm,
    ClassScheduleForm, GuardianInformationForm
)
from .models import StudentInformation, CourseEnrollment

from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard_view(request):
    try:
        student_info = StudentInformation.objects.get(user=request.user)
    except StudentInformation.DoesNotExist:
        student_info = None

    return render(request, 'dashboard.html', {'student_info': student_info})

@login_required
def enrollee_view(request):
    if request.method == 'POST':
        s_form = StudentInformationForm(request.POST)
        c_form = CourseEnrollmentForm(request.POST)
        cls_form = ClassScheduleForm(request.POST)
        g_form = GuardianInformationForm(request.POST)

        if all([s_form.is_valid(), c_form.is_valid(), cls_form.is_valid(), g_form.is_valid()]):
            student_info = s_form.save(commit=False)
            student_info.user = request.user
            student_info.save()

            course = c_form.save(commit=False)
            course.student = student_info
            course.save()

            class_s = cls_form.save(commit=False)
            class_s.course = course
            class_s.save()

            guardian = g_form.save(commit=False)
            guardian.student = student_info
            guardian.save()

            name = request.user.username
            logout(request)
            return redirect('logged_out_with_name', name=name)
    else:
        s_form = StudentInformationForm()
        c_form = CourseEnrollmentForm()
        cls_form = ClassScheduleForm()
        g_form = GuardianInformationForm()

    return render(request, 'enrollee.html', {
        's_form': s_form,
        'c_form': c_form,
        'cls_form': cls_form,
        'g_form': g_form,
    })

def logged_out_view(request):
    return render(request, 'logged_out.html', {'name': None})

def logged_out_with_name(request, name):
    return render(request, 'logged_out.html', {'name': name})

@login_required
def view_information(request):
    try:
        student_info = StudentInformation.objects.get(user=request.user)
    except StudentInformation.DoesNotExist:
        student_info = None
    return render(request, 'view_info.html', {'student_info': student_info})

# Create your views here.
