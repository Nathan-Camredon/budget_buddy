import customtkinter as ctk
from src.frontend.Abstract.Interface import Interface

class InterfaceUser(Interface):
    def __init__(self, master, controller, **kwargs):
        self.controller = controller
        super().__init__(master, title="Compte Utilisateur", **kwargs)

    def _build_ui(self) -> None:
        self.configure(fg_color="transparent")
        
        ctk.CTkLabel(
            self, 
            text="Interface Client", 
            font=ctk.CTkFont(size=30, weight="bold")
        ).pack(pady=50)

        ctk.CTkButton(
            self, 
            text="Se déconnecter", 
            command=self.controller.show_login
        ).pack(pady=20)
