from . import views
from django.urls import path
from .views import (StudentDashboard)


urlpatterns = [
    path('',StudentDashboard.as_view(),name='student_dashboard'),
    path('profile/',views.StudentProfile.as_view(),name='student_profile'),
]
