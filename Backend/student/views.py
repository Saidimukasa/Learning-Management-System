from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Student
from LMS import constants

def getLogedInStudentId(user_id):
    s = Student.objects.get(user_id=user_id)
    return s.id

class StudentDashboard(View):
   template_name = 'student/index.html'
   
   @method_decorator(login_required, 'signin')
   def get(self, request):
      user_id = request.user.id
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
      }
      return render(request, self.template_name, context)
   
class StudentProfile(View):
   template_name = 'student/profile.html'
   
   @method_decorator(login_required, 'signin')
   def get(self, request):
      user_id = request.user.id
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
      }
      return render(request, self.template_name, context)
   
   

 
