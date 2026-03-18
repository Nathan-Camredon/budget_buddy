import customtkinter as ctk
from src.frontend.InterfaceLogin import InterfaceLogin


def main() -> None:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Budget Buddy")
    app.geometry("1920x1080")
    app.resizable(False, False)

    # L'InterfaceLogin gère maintenant sa propre logique de connexion
    login_page = InterfaceLogin(master=app)
    login_page.show()

    app.mainloop()


if __name__ == "__main__":
    main()
