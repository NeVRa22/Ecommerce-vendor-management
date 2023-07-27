from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self, username):
        super().__init__(username)
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        self.username = username
        if self.username in self.vendor_session.login(username):
            print('User ', self.username, 'logged in successfully!')
            return True

        else:
            print('Invalid username or password.')
            return False

        # Add you code here after verifying the vendor data exists in the dictionary 

    def logout(self, username):
        self.username = username
        if username in VendorSessionModel.vendor_session_db:
            del VendorSessionModel.vendor_session_db[username]
        print('User', self.username, 'logged out successfully!')
        return True
        # Add your code here to log out the current vendor
