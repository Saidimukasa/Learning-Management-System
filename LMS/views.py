from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from LMS.constants import SCHOOL_NAME
from account.models import Account
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
import sweetify
from django.contrib.auth import update_session_auth_hash


def signin(request):
    if request.method == 'GET':
      school_name = SCHOOL_NAME
      return render(request, 'login.html', {'school_name': school_name})
    else:
        email_ = request.POST.get("email")
        password_ = request.POST.get("password")
        user = authenticate(email = email_, password = password_)
        if user is not None:
            login(request, user)
            if request.user.is_manager:
                return redirect('manager_dashboard')
            elif request.user.is_teacher:
                return redirect('teacher_dashboard')
            elif request.user.is_student:
                return redirect('student_dashboard')
            else:
                messages.error(request, 'There was some problem. Please log in again')
                return redirect('signin')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('signin')


class PasswordChangeManager(View):
    template_name = 'change_password.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass1 = request.POST.get('new_password1')
        pass2 = request.POST.get('new_password2')

        if pass1 == pass2:
            user = Account.objects.get(id=request.user.id)
            user.password = make_password(pass1)
            user.is_firstLogin = False
            user.save()
            logout(request)
            messages.add_message(request, messages.SUCCESS,
                                 'Password Change Successfully')
            return redirect('signin')
        else:
            messages.add_message(request, messages.ERROR,
                                 'password does not match')
            return redirect(reverse_lazy('password_change'))


def change_password(request):
   template_name = 'student/profile-edit.html'
   if request.method == 'POST':
      form = PasswordChangeForm(request.user, request.POST)
      if form.is_valid():
         user = form.save()
         update_session_auth_hash(request, user)
         sweetify.success(request, 'Password changed successfully')
         return redirect('student_profile')
      else:
         sweetify.error(request, 'Password change failed')
         messages.error(request, form.errors)
         print(form.errors)
   else:
      form = PasswordChangeForm(request.user)
   return render(request, template_name, {'form': form})