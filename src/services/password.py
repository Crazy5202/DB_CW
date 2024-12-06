import bcrypt
from repositories.adm_users import get_user_pwd

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
    return hashed_password

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

def check_wrapper(username, password):
    result = get_user_pwd(username)
    if result and check_password(password, result[0]):
        return result[1]
    else:
        return 0