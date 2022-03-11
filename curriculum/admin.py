from django.contrib import admin
from .models import Class, Curriculum, Subject, Resource

admin.site.register(Curriculum)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Resource)