from django.db import models
from teacher.models import Teacher


DAYS = (
      ('Monday', 'Monday'),
      ('Tuesday', 'Tuesday'),
      ('Wednesday', 'Wednesday'),
      ('Thursday', 'Thursday'),
      ('Friday', 'Friday'),
      ('Saturday', 'Saturday'),
      ('Sunday', 'Sunday'),
)
   
class Curriculum(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(max_length=500)
   status = models.BooleanField(default=True)
   
   def __str__(self):
      return self.name
   
class Class(models.Model):
   name = models.CharField(max_length=100)
   curriculum = models.ForeignKey(Curriculum,on_delete=models.CASCADE)
   code = models.CharField(max_length=10,unique=True)
   plural = 'Classes'

   def __str__(self):
      return self.name
   
class Subject(models.Model):
   name = models.CharField(max_length=100)
   c_class = models.ForeignKey(Class,on_delete=models.CASCADE)
   code = models.CharField(max_length=10,unique=True)
   
   def __str__(self):
      return self.name
   
   
class Resource(models.Model):
   name = models.CharField(max_length=100)
   file = models.FileField(upload_to='resources/')
   date_created = models.DateTimeField(auto_now_add=True)
   date_edited = models.DateTimeField(auto_now=True)
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   status = models.BooleanField(default=True)
   
   def __str__(self):
      return self.name
   
class TimeTable(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
   day = models.CharField(max_length=10,choices=DAYS)
   start_time = models.TimeField()
   end_time = models.TimeField()
   link = models.CharField(max_length=100, blank=True, null=True)
   
   def __str__(self):
      return self.subject.name


class Assignment(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   instructions = models.TextField(max_length=500)
   file = models.FileField(upload_to='assignments/', blank=True, null=True)
   date_created = models.DateTimeField(auto_now_add=True)
   date_due = models.DateTimeField()
   returned = models.BooleanField(default=False)
   status = models.BooleanField(default=True)
   
   
   def __str__(self):
      return self.name
   

class StudentAnnouncement(models.Model):
   title = models.CharField(max_length=100)
   target = models.CharField(max_length=100)
   detail = models.TextField(max_length=500)
   date_created = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=True)
   
   
   def __str__(self):
      return self.title
   

class TeacherAnnouncement(models.Model):
   title = models.CharField(max_length=100)
   detail = models.TextField(max_length=500)
   date_created = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=True)
   
   
   def __str__(self):
      return self.title
   
class Exam(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   exam_date = models.DateTimeField()
   duration = models.IntegerField(default=0)
   date_created = models.DateTimeField(auto_now_add=True)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
   no_of_questions = models.IntegerField(default=0)
   total_marks = models.IntegerField(default=0)
   status = models.BooleanField(default=True)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
   
   def __str__(self):
      return self.subject.name
   
class Question(models.Model):
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=0)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
    answer = models.CharField(max_length=1, choices=choose)

    def __str__(self):
        return str(self.question)