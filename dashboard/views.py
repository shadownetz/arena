from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile, UserProfile
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm

def get_user_profile_info(request):
    user_a = get_object_or_404(UserProfile, pk=request.user.id)
    user_a1 = get_object_or_404(Profile, user=user_a.profile.user)
    return user_a1


@login_required
def index(request):
    if request.user.username == 'shadownetz' and request.user.id == 1:
        return redirect(reverse('arena:arena_dashboard:su'))
    return render(request, "arena/dashboard.html", {})


@login_required
def user_profile(request):
    if request.user.username == 'shadownetz' and request.user.id == 1:
        return redirect(reverse('arena:arena_dashboard:su'))
    user_info = get_user_profile_info(request=request)
    return render(request, "arena/profile-contacts.html", {'dashboard': user_info})


@login_required
def su_user_profile(request):
    if not (request.user.username == 'shadownetz' and request.user.id == 1):
        return redirect(reverse('arena:arena_dashboard:index'))
    user_info = get_user_profile_info(request=request)
    return render(request, "arena/superuser/profile-contacts.html", {'dashboard': user_info})


@login_required
def su_index(request):
    if not (request.user.username == 'shadownetz' and request.user.id == 1):
        logout(request)
        return redirect(reverse('arena:index'))
    return render(request, 'arena/superuser/19992403.html', {})


def update_profile(request):
    """
    Updates Profile data according to values in request object from ajax
    :param request:
    :return: object
    """
    update_form = UserUpdateForm(request.POST, instance=UserProfile)
    data_object = request.POST('data_object')
    fname, lname, uname, passcode, pnumber, about, pub_id = '', '', '', '', '', '', ''
    re_data = {
        'success_msg': 'Updated Successfully'
    }
    if update_form.is_valid():
        try:
            fname = data_object['first_name']
            lname = data_object['last_name']
            uname = data_object['username']
            passcode = data_object['passcode']
            pnumber = data_object['phone_number']
            about = data_object['about']
            pub_id = data_object['pub_id']
        except KeyError:
            pass

    # Updating full name
    if (len(fname) or len(lname)) > 0:
        if request.user.is_authenticated:
            # user = get_object_or_404(UserProfile, pk=request.user.id)
            # if len(fname) > 0:
            #     user.first_name = fname
            # if len(lname) > 0:
            #     user.last_name = lname
            # user.save()
            update_form.save()
            update_session_auth_hash(request, user=request.user)
            return JsonResponse(data=re_data)
        return redirect(reverse('arena:index'))
    # Updating Username
    elif len(uname) > 0:
        if request.user.is_authenticated:
            user = get_object_or_404(UserProfile, pk=request.user.id)
            user.username = uname
            user.save()
            update_session_auth_hash(request, user=user)
            return JsonResponse(data=re_data)
    # Updating phone number
    elif len(pnumber) > 0:
        if request.user.is_authenticated:
            user = get_object_or_404(UserProfile, pk=request.user.id)
            user.profile.phone_number = pnumber
            user.save()
            update_session_auth_hash(request, user=user)
            return JsonResponse(data=re_data)
    # Updating about
    elif len(about) > 0:
        if request.user.is_authenticated:
            user = get_object_or_404(UserProfile, pk=request.user.id)
            user.profile.about = about
            user.save()
            update_session_auth_hash(request, user=user)
            return JsonResponse(data=re_data)
    # Updating public id
    elif len(pub_id) > 0:
        if request.user.is_authenticated:
            user = get_object_or_404(UserProfile, pk=request.user.id)
            user.profile.nick_name = pub_id
            user.save()
            update_session_auth_hash(request, user=user)
            return JsonResponse(data=re_data)
    # Updating password
    elif len(passcode) > 0:
        if request.user.is_authenticated:
            user = get_object_or_404(UserProfile, pk=request.user.id)
            user.set_password(passcode)
            user.save()
            update_session_auth_hash(request, user=user)
            return JsonResponse(data=re_data)
    return JsonResponse(data='', safe=False)


def profile_data_request(request):
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, pk=request.user.id)
        data_object = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'phone_number': user.profile.phone_number,
            'about': user.profile.about,
            'pub_id': user.profile.nick_name
        }
        return JsonResponse(data=data_object)
    request.session.clear()
    return redirect(reverse('arena:index'))
