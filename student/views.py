from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from curriculum.models import Assignment, Class, Curriculum, Exam, Resource, StudentAnnouncement, Subject, TimeTable
from .forms import StudentForm
from .models import RegistrationDeadline, Student
from LMS import constants
from django.views.generic.edit import FormView
from django.contrib import messages
import sweetify
from datetime import datetime, timedelta

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


def student_edit_profile(request):
   template_name = 'student/profile-edit.html'
   if request.method == 'POST':
      form = StudentForm(request.POST, request.FILES, instance = request.user.student)
      if form.is_valid():
         form.save()
         sweetify.success(request, 'Success', text='Profile updated successfully')
         return redirect('student_profile')
      else:
         print(form.errors)
         sweetify.error(request, 'Error', text='Error updating profile')
   else:
      form = StudentForm(instance = request.user.student)
   return render(request, template_name, {'form': form})
 
   
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
      resources = Resource.objects.all()
      user = request.user
      
      # this_resource = Resource.objects.filter(subject__in=student_subject_resources)
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'user': user,
         'resources': resources,
      }
      print(resources)
      # print(this_resource)
      return render(request, self.template_name, context)
   

class StudentSubjectRegistration(View):
   template_name = 'student/subject-registration.html'
   
   @method_decorator(login_required, 'signin')
   def get(self, request):
      user_id = request.user.id
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      curriculums = Curriculum.objects.filter(status=True)
      subjects = Subject.objects.all()
      classes = Class.objects.all()
      registration_deadlines = RegistrationDeadline.objects.all()
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'curriculums': curriculums,
         'subjects': subjects,
         'classes': classes,
         'registration_deadlines': registration_deadlines,
      }
      return render(request, self.template_name, context)
   
def student_class(request, id):
   template_name = 'student/class.html'
   get_class = Class.objects.get(id=id)
   context = {'class': get_class}
   
   return render(request, template_name, context)

def student_register_subject(request):
   if request.method == 'POST':
      user_id = request.user.id
      subjects = request.POST.get('subjects_selected')
      print(subjects)
      subjects = str(subjects)
      reg_subjects = subjects.rstrip(',').split(',')
      print("Reg SUbjects >>>>>>>> ", reg_subjects)
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      print(student)
      for i in reg_subjects:
         student.subject.add(i)
         student.save()
      sweetify.success(request, 'Success', text='Subjects registered successfully')
      return redirect('student_subject_registration')
   
         
      


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
      print(student.subject.all())
      return render(request, self.template_name, context)
   
   
class StudentTimetable(View):
   template_name = 'student/timetable.html'
   
   @method_decorator(login_required, 'signin')
   def get(self, request):
      user_id = request.user.id
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      timetables = TimeTable.objects.all()
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'timetables': timetables,
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
      assignments = Assignment.objects.filter(subject__in=student.subject.all())
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'assignments': assignments,
      }
      return render(request, self.template_name, context)


class StudentAssignmentDetail(View):
   template_name = 'student/assignment-details.html'
   
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


def student_assignment_detail(request, id):
   template_name = 'student/assignment-details.html'
   user_id = request.user.id
   student_id = getLogedInStudentId(user_id)
   student = Student.objects.get(id=student_id)
   assignment = Assignment.objects.get(id=id)
   print(assignment)
   context = {
      'student': student,
      'school_name': constants.SCHOOL_NAME,
      'assignment': assignment,
   }
   return render(request, template_name, context)
   
 

class StudentExams(View):
   template_name = 'student/exams.html'
   
   @method_decorator(login_required, 'signin')
   def get(self, request):
      user_id = request.user.id
      student_id = getLogedInStudentId(user_id)
      student = Student.objects.get(id=student_id)
      exams = Exam.objects.filter(subject__in = student.subject.all())
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'exams': exams,
      }
      return render(request, self.template_name, context)

   

def student_exam_detail(request, id):
   template_name = 'student/exam-details.html'
   
   user_id = request.user.id
   student_id = getLogedInStudentId(user_id)
   student = Student.objects.get(id=student_id)
   exam = Exam.objects.get(id=id)
   context = {
      'student': student,
      'school_name': constants.SCHOOL_NAME,
      'exam': exam,
   }
   return render(request, template_name, context)

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
      announcements = StudentAnnouncement.objects.filter(status = True)
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'announcements': announcements,
      }
      return render(request, self.template_name, context)
