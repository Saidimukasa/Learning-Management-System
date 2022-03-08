from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from curriculum.models import Curriculum, Subject
from .forms import StudentForm
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


class StudentEditProfile(View):
   template_name = 'student/profile-edit.html'
   
   @method_decorator(login_required, 'signin')
   def get(self, request):
      user_id = request.user.id
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      school_name = constants.SCHOOL_NAME
      if request.method == 'POST':
         form = StudentForm(request.POST, instance = Student.objects.get(id=student_id))
         if form.is_valid():
            form.save()
            return redirect('student_profile')
         else:
            print(form.errors)
      else:
         form = StudentForm()
      return render(request, self.template_name, {'form': form, 'school_name': school_name, 'student': student})
         
      
   
   
class ChatRoom(View):
   template_name = 'student/chat.html'
   
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
   

class StudentCalendar(View):
   template_name = 'student/calendar.html'
   
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
   
class StudentResources(View):
   template_name = 'student/resources.html'
   
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
   

class StudentCourseRegistration(View):
   template_name = 'student/course_registration.html'
   
   @method_decorator(login_required, 'signin')
   def get(self, request):
      user_id = request.user.id
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      curriculums = Curriculum.objects.filter(status=True)
      subjects = Subject.objects.filter(curriculum__status=True)
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'curriculums': curriculums,
         'subjects': subjects,
      }
      return render(request, self.template_name, context)
   

class StudentSubjectsEnrolled(View):
   template_name = 'student/subjects-enrolled.html'
   
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
   
class StudentTimetable(View):
   template_name = 'student/timetable.html'
   
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

class StudentGradebook(View):
   template_name = 'student/gradebook.html'
   
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

class StudentAssignments(View):
   template_name = 'student/assignments.html'
   
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

class StudentExams(View):
   template_name = 'student/exams.html'
   
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
   

class StudentResults(View):
   template_name = 'student/results.html'
   
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
   
class StudentFees(View):
   template_name = 'student/fees.html'
   
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

class StudentAnnouncements(View):
   template_name = 'student/announcements.html'
   
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
