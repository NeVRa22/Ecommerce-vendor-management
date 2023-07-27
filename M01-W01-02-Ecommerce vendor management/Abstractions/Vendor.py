class Vendor:
    login_credentials = dict()

    def __init__(self, username):
        self.username = username

    def login(self, username, password):
        self.login_credentials[username] = {"Username": username,
                                            "password": password,
                                            }
        Vendor.login_credentials[username] = True
        return True
    """This method will be used to login an existing Vendor."""

    def logout(self, username):
        self.username = username
        if username in Vendor.login_credentials:
            del Vendor.login_credentials[username]
            return True

    """This method will be used to logout an existing Vendor."""
