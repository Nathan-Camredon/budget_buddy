import customtkinter as ctk
from src.frontend.InterfaceLogin import InterfaceLogin


def handle_login(username: str, password: str) -> None:
    """
    Callback triggered when the user clicks the login button.
    TODO: plug in backend verification logic here.
    """
    print(f"[Login] username={username!r}")


def main() -> None:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Budget Buddy")
    app.geometry("1920x1080")
    app.resizable(False, False)

    login_page = InterfaceLogin(master=app, on_login=handle_login)
    login_page.show()

    app.mainloop()


if __name__ == "__main__":
    main()
