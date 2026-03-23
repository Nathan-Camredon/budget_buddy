import customtkinter as ctk
from src.frontend.InterfaceLogin import InterfaceLogin
from src.frontend.InterfaceAdmin import InterfaceAdmin
from src.frontend.InterfaceUser import InterfaceUser

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main window configuration
        self.title("Budget Buddy")
        self.geometry("1280x720")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Page initialization
        self.login_page = InterfaceLogin(master=self, controller=self)
        self.admin_page = InterfaceAdmin(master=self, controller=self)
        self.user_page = InterfaceUser(master=self, controller=self)
        
        self.current_user = None

        # Display the login page by default
        self.show_login()

    def show_login(self):
        self.admin_page.hide()
        self.user_page.hide()
        self.login_page.show()

    def show_admin(self):
        self.login_page.hide()
        self.user_page.hide()
        self.admin_page.show()

    def show_user(self):
        self.login_page.hide()
        self.admin_page.hide()
        self.user_page.show()
