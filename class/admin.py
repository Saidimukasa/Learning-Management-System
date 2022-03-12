from django.contrib import admin
from .models import Class,ClassJoined,Comment,Stream

admin.site.register([Class,Comment,Stream,ClassJoined])
