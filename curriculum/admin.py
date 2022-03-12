from django.contrib import admin
from .models import Class, Curriculum, Subject, Resource, TimeTable, StudentAnnouncement, TeacherAnnouncement, Assignment, Exam, Question

admin.site.register(Curriculum)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Resource)
admin.site.register(TimeTable)
admin.site.register(StudentAnnouncement)
admin.site.register(TeacherAnnouncement)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(Question)