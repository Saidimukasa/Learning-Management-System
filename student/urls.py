from . import views
from django.urls import path
from .views import (StudentDashboard)


urlpatterns = [
    path('',StudentDashboard.as_view(),name='student_dashboard'),
    path('profile/',views.StudentProfile.as_view(),name='student_profile'),
    path('profile/edit/',views.student_edit_profile,name='student_edit_profile'),
    path('chat/',views.ChatRoom.as_view(),name='student_chat'),
    path('calendar/',views.StudentCalendar.as_view(),name='student_calendar'),
    path('resources/',views.StudentResources.as_view(),name='student_resources'),
    path('subject-registration/',views.StudentSubjectRegistration.as_view(),name='student_subject_registration'),
    path('subject-registration/register/',views.student_register_subject,name='student_register_subject'),
    path('subjects-enrolled',views.StudentSubjectsEnrolled.as_view(),name='student_subjects_enrolled'),
    path('timetable/',views.StudentTimetable.as_view(),name='student_timetable'),
    path('gradebook/',views.StudentGradebook.as_view(),name='student_gradebook'),
    path('assignments/',views.StudentAssignments.as_view(),name='student_assignments'),
    path('assignments/details/<int:id>',views.student_assignment_detail ,name='student_assignment_detail'),
    path('exams/',views.StudentExams.as_view(),name='student_exams'),
    path('exams/details/<int:id>',views.student_exam_detail,name='student_exam_detail'),
    path('results/',views.StudentResults.as_view(),name='student_results'),
    path('fees',views.StudentFees.as_view(),name='student_fees'),
    path('announcements/',views.StudentAnnouncements.as_view(),name='student_announcements'),
    
]
