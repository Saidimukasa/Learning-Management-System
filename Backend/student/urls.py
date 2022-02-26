from . import views
from django.urls import path
from .views import (StudentView,searchclass,classJoin)


urlpatterns = [
    path('dashboard/',StudentView.as_view(),name='student_dashboard'),
    path('search/',searchclass,name='search'),
    path('classjoined/<int:class_id>',classJoin,name='class_join')
]
