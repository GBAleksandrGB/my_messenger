from PyQt6.QtWidgets import QDialog, QMainWindow

from client.ui.login import Ui_Login_Dialog as login_ui_class
from client.ui.contacts import Ui_ContactsWindow as contacts_ui_class


class LoginWindow(QDialog):
    """Login Window (user interface)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = login_ui_class()
        self.ui.setupUi(self)


class ContactsWindow(QMainWindow):
    """Contacts Window (user interface)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = contacts_ui_class()
        self.ui.setupUi(self)
