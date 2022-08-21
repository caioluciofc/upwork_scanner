class WrongUsernamePassword(Exception):
    def __init__(self):
        super().__init__("Username or Password used is wrong")
