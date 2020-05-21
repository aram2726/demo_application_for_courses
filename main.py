from getpass import getpass

from app.auth import login, register_user, is_authenticated
from app.utils import help_text, get_data

auth_actions = {
    "login": login,
    "register": register_user,
}

helper_actions = {
    "help": help_text,
    "-h": help_text,
    "q": exit,
    "exit": exit,
    "data": get_data,
    "whoami": is_authenticated,
}


def main():
    """
    The main entry point of a demo application.

    :rtype: NoneType
    :return: None
    """

    while True:

        action = str(input("enter action: "))

        if action in auth_actions:
            email = str(input("email: "))
            password = str(getpass("password: "))

            # Note that `auth_actions[action]` is a function.
            # So it is a callable object.
            auth_actions[action](email, password)

        if action in helper_actions:
            helper_actions[action]()


if __name__ == "__main__":
    main()
