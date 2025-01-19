from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Lesson Model
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

# Progress Model
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.progress_percentage}%"






class Assignment(models.Model):
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)




# Student Model
class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# Enrollment Model
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.user.username} enrolled in {self.course.name}'
