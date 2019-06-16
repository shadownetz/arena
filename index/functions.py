from .models import UserProfile


# Encrypt password
def hash_password(password, salt):
    import hashlib
    import binascii
    u_password = str(password).encode()
    u_salt = str(salt).encode()
    hashed = hashlib.pbkdf2_hmac('sha1', password=u_password, salt=u_salt, iterations=100000, dklen=40)
    return binascii.hexlify(hashed).decode()


def authenticate_user(username, password):
    try:
        user = UserProfile.objects.get(username=username)

    except UserProfile.DoesNotExist:
        return None
    else:
        tmp_salt = user.salt
        tmp_password = hash_password(password, tmp_salt)
        if tmp_password == user.password:
            return user
    return None
