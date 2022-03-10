from django import forms
from django.db.models import fields
from .models import Student


class StudentForm(forms.ModelForm):
   class Meta:
      model = Student
      fields = ['first_name', 'last_name', 'contact_no', 'parent_name', 'parent_phone_no', 'city', 'country', 'about', 'profile']
      
   def __init__(self, *args, **kwargs):
      super(StudentForm, self).__init__(*args, **kwargs)
      for visible in self.visible_fields():
         visible.field.widget.attrs['class'] = 'form-control'
         visible.field.widget.attrs['placeholder'] = visible.field.label
         