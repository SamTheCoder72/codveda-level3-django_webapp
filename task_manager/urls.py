from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views

urlpatterns = [
    path('my-tasks/', task_views.my_tasks, name='my_tasks'),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login'), name='home'),
    # User Authentication URLs
    path('register/', task_views.register, name='register'),
    path('', include('django.contrib.auth.urls')), # This automatically adds login/logout URLs!
    
    # The Main Dashboard
    path('dashboard/', task_views.dashboard, name='dashboard'),
]