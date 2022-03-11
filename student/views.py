from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from curriculum.models import Class, Curriculum, Resource, Subject
from .forms import StudentForm
from .models import Student
from LMS import constants
from django.views.generic.edit import FormView
from django.contrib import messages
import sweetify

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

# class StudentEditProfile(FormView):
#    template_name = 'student/profile-edit.html'
#    form_class = StudentForm
#    success_url = reverse_lazy('student:student_profile')
   
#    def form_valid(self, form):
#       user_id = self.request.user.id
#       student_id = getLogedInStudentId(user_id)
#       student = Student.objects.get(id=student_id)
#       student.first_name = form.cleaned_data['first_name']
#       student.last_name = form.cleaned_data['last_name']
#       # student.email = form.cleaned_data['email']
#       student.contact_no = form.cleaned_data['contact_no']
#       student.save()
#       return super(StudentEditProfile, self).form_valid(form)
   
   
   # @method_decorator(login_required, 'signin')
   # def get(self, request):
   #    user_id = request.user.id
   #    student_id = getLogedInStudentId(user_id)
   #    student = Student.objects.get(id=student_id)
   #    school_name = constants.SCHOOL_NAME
   #    if request.method == 'POST':
   #       form = StudentForm(request.POST, instance = Student.objects.get(id=student_id))
   #       if form.is_valid():
   #          form.save()
   #          return redirect('student_profile')
   #       else:
   #          print(form.errors)
   #    else:
   #       form = StudentForm()
   #    return render(request, self.template_name, {'form': form, 'school_name': school_name, 'student': student})
         
      
   
   
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
      context = {
         'student': student,
         'school_name': constants.SCHOOL_NAME,
         'curriculums': curriculums,
         'subjects': subjects,
         'classes': classes,
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
      print(student.subject.all())
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

class StudentExamDetail(View):
   template_name = 'student/exam-details.html'
   
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
