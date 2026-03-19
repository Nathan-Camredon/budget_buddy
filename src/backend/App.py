import customtkinter as ctk
from src.frontend.InterfaceLogin import InterfaceLogin
from src.frontend.InterfaceAdmin import InterfaceAdmin
from src.frontend.InterfaceUser import InterfaceUser

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Budget Buddy")
        self.geometry("1920x1080")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialisation des pages
        self.login_page = InterfaceLogin(master=self, controller=self)
        self.admin_page = InterfaceAdmin(master=self, controller=self)
        self.user_page = InterfaceUser(master=self, controller=self)

        # Affichage de la page de connexion par défaut
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
