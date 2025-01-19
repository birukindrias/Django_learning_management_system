from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Correct indentation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs
    # path('', include('lms.urls')),
        path('', include('learning_management_system.urls')),
        
   # Update with the new app name
]
