from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from django.views import generic
from .forms import UserSignUp, UserLogin
from .models import UserProfile
from . import functions as user_func
import os


def index(request):
    user_form = UserSignUp()
    user_login_form = UserLogin()
    return render(request, 'arena/index.html', {'forms': user_form, 'login_form': user_login_form})


def contact(request):
    return render(request, 'arena/contact.html', {})


def process_user_signup(request):
    error_message = []
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        login_form = UserLogin()
        if form.is_valid():
            user_fname = form.cleaned_data.get('first_name')
            user_lname = form.cleaned_data.get('last_name')
            user_uname = form.cleaned_data.get('username')
            user_email = form.cleaned_data.get('email')
            user_pass = form.cleaned_data.get('password')
            user_repass = form.cleaned_data.get('password2')

            if user_pass == user_repass:
                enc_salt = os.urandom(10).hex()
                enc_password = user_func.hash_password(user_pass, enc_salt)
                try:
                    new_user = UserProfile.objects.get(username=user_uname)
                except UserProfile.DoesNotExist:
                    new_user_form = UserProfile.objects.create(
                        first_name=user_fname, last_name=user_lname, username=user_uname,
                        email=user_email
                    )
                    new_user_form.set_password(user_pass)
                    new_user_form.save()
                    user_log = authenticate(username=user_uname, password=user_pass)
                    # user_log = user_func.authenticate_user(username=user_uname, password=user_pass)
                    if user_log is not None:
                        login(request, user_log)
                        return redirect(reverse('arena:arena_dashboard:index'))
                else:
                    error_message.append('Username already exist')
                    return render(request, 'arena/base.html', {
                        'forms': form, 'login_form': login_form, 'error': error_message
                    })
            else:
                error_message.append('Passwords do not match')
        return render(request, 'arena/index.html', {'forms': form, 'login_form': login_form, 'error': error_message})

    return redirect(reverse('arena:index'))


def user_login(request):
    error_message = []
    user_signup_form = UserSignUp()
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        nextValue = request.POST.get('next')

        if form.is_valid():
            uname = form.cleaned_data['username']
            passcode = form.cleaned_data['password']

            # user = user_func.authenticate_user(username=uname, password=passcode)
            user = authenticate(username=uname, password=passcode)
            if user is not None:
                login(request, user)
                if user.username == 'shadownetz' and user.is_active and user.is_staff and user.is_superuser:
                    if nextValue == '/dashboard/su/':
                        return redirect(nextValue)
                    return redirect(reverse('arena:arena_dashboard:su'))
                if nextValue:
                    if nextValue == '/dashboard/su/':
                        return redirect(reverse('arena:arena_dashboard:index'))
                    return redirect(nextValue)
                else:
                    return redirect(reverse('arena:arena_dashboard:index'))
            else:
                error_message.append("Invalid Login Details")
        form = UserLogin()
    return render(request, 'arena/index.html', {'forms': user_signup_form, 'login_form': form, 'login_error': error_message})


def user_logout(request):
    logout(request)
    return redirect(reverse('arena:index'))


@login_required
def dash(request):
    return render(request, 'arena/dashboard.html', {})


def validate_username(request):
    username = request.GET.get('username')
    data = {
        'is_taken': UserProfile.objects.filter(username__iexact=username).exists(),
    }
    if data['is_taken']:
        data['error_message'] = 'username already exists'
    return JsonResponse(data=data)

