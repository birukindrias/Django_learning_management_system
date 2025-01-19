from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
     path('list', views.course_list, name='course_list'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),  
]
