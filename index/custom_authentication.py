from django.conf import settings
from django.contrib.auth.hashers import check_password
from .functions import hash_password
# from django.contrib.auth.models import User
from django.conf import settings
from .models import UserProfile as User


class SettingsBackend:
    """
    Authenticate
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        else:
            tmp_salt = user.salt
            tmp_pass = hash_password(password, tmp_salt)
            if tmp_pass == user.password:
                return user
            else:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
