from django.shortcuts import render, get_object_or_404
from .models import Course

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Home page view
def home(request):
    return render(request, 'home.html')

# Courses list view
def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': all_courses})

# Course detail view
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
