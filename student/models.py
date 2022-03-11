from django.db import models
from account.models import Account
from curriculum.models import Subject

class Student(models.Model):
   username = models.CharField(max_length=50, unique=True)
   contact_no = models.CharField(max_length=20,default='2547xxxxxxx')
   parent_name = models.CharField(max_length=100)
   parent_phone_no = models.CharField(max_length=20,default='2547xxxxxxx')
   city = models.CharField(max_length=100,default='Nairobi')
   country = models.CharField(max_length=100,default='Kenya')
   profile = models.ImageField(blank=True,null=True,upload_to='profile/')
   user = models.OneToOneField(Account,on_delete=models.CASCADE)
   about = models.TextField(max_length=500,blank=True,null=True)
   subject = models.ManyToManyField(Subject, blank=True)
   

   def __str__(self):
      return self.username
   

class Result(models.Model):
   student = models.ForeignKey(Student,on_delete=models.CASCADE)
   subject = models.CharField(max_length=100)
   score = models.IntegerField()
   total = models.IntegerField()
   grade = models.CharField(max_length=10)

   def __str__(self):
      return self.student.name + ' ' + self.subject


