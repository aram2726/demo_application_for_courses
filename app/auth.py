from hashlib import sha1

from .data import DB_DATA

PASSWORD_MIN_LENGTH = 7
PASSWORD_MAX_LENGTH = 12

USER = {
    "is_logged_in": False,
    "name": None
}


def validate_email(email):
    """
    Validate user email.
    None regex validation of email.

    :param email: User email.
    :type email: str

    :raises: Exception

    :rtype: NoneType
    :return: None
    """
    if email != email.replace(" ", ""):
        raise Exception("Invalid email address.")

    if "@" not in email:
        raise Exception("Invalid email address.")

    if "." not in email.split("@")[1]:
        raise Exception("Invalid email address.")

    # TODO: Complete the validation.


def validate_password(password):
    """
    Validate user password.

    :param password: User password.
    :type password: str

    :raises: Exception

    :rtype: NoneType
    :return: None
    """
    if password != password.replace(" ", "") or PASSWORD_MIN_LENGTH < len(password) < PASSWORD_MAX_LENGTH:
        raise Exception(
            "Invalid password. Please enter a password with min length {} and max length {}".format(
                PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH
            )
        )


def register_user(email, password):
    """
    Register user to temporary in memory database.

    :param email: Email.
    :type email: str

    :param password: User password.
    :type password: str

    :rtype: NoneType
    :return: None
    """
    # TODO: Catch the exceptions.
    validate_email(email)
    validate_password(password)

    DB_DATA["users"].append(
        {
            "username": email.split("@")[0],
            "email": email,
            "password": sha1(password.encode("utf-8")).hexdigest()
        }
    )


def login(email, password):
    """
    Authenticate user.

    :param email: Email.
    :type email: str

    :param password: User password.
    :type password: str

    :raises: Exception

    :rtype: dict
    :return: User data.
    """
    if DB_DATA:
        for user in DB_DATA["users"]:
            if user["email"] == email and sha1(password.encode("utf-8")).hexdigest() == user["password"]:
                global USER
                USER["is_logged_in"] = True
                USER["name"] = user["username"]
                return user
    raise Exception("User not found.")


def is_authenticated():
    global USER
    print("Is authenticated: {}, name: {}".format(USER["is_logged_in"], USER["name"]))
