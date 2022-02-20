import os


def welcome():
    return f"Hello {os.environ.get('PRENAME')} {os.environ.get('SURNAME')}!"


if __name__ == "__main__":
    welcome()
