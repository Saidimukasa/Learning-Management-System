from django.db import models
from teacher.models import Teacher

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
   status = models.BooleanField(default=True)
   date_created = models.DateTimeField(auto_now_add=True)
   date_edited = models.DateTimeField(auto_now=True)
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   
   def __str__(self):
      return self.name

