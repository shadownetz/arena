# Encrypt password
def hash_password(password, salt):
    import hashlib
    import binascii
    u_password = str(password).encode()
    u_salt = str(salt).encode()
    hashed = hashlib.pbkdf2_hmac('sha1', password=u_password, salt=u_salt, iterations=100000, dklen=40)
    return binascii.hexlify(hashed).decode()


def generate_random_value(length):
    """
    Generate random value based on a given length
    :param length:
    :return:string
    """
    import os
    import binascii

    value_length = length
    tmp_value = os.urandom(value_length)
    result = binascii.hexlify(tmp_value).decode()
    return result
