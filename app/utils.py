from .data import DB_DATA
from .auth import USER


def help_text():
    print("""
    To register as a user please type `register`.
    To login into system please type `login`.
    To get help please type `help` or `-h`.
    To exit the application type `exit` or `q`.
    To get information about session type `whoami`.
    To get data accessible to authenticated users type `data`.
    """)


def get_data():
    """
    Return data.

    :rtype: str
    :return: Some protected data.
    """
    if USER["is_logged_in"]:
        print(DB_DATA["protected_data"])
