from django.db import models
from account.models import Account



class Teacher(models.Model):
    username = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20,default='2547xxxxxxxx')
    profile = models.ImageField(blank=True,null=True,upload_to='profile/')
    user = models.OneToOneField(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.username

