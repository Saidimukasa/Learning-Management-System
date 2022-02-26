from django.db import models
from account.models import Account

class Student(models.Model):
   name = models.CharField(max_length=100)
   contact_no = models.CharField(max_length=20,default='2547xxxxxxx')
   profile = models.ImageField(blank=True,null=True,upload_to='profile/')
   user = models.OneToOneField(Account,on_delete=models.CASCADE)

   def __str__(self):
      return self.name
   

class Result(models.Model):
   student = models.ForeignKey(Student,on_delete=models.CASCADE)
   subject = models.CharField(max_length=100)
   score = models.IntegerField()
   total = models.IntegerField()
   grade = models.CharField(max_length=10)

   def __str__(self):
      return self.student.name + ' ' + self.subject


