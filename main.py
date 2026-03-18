import customtkinter as ctk
from src.frontend.InterfaceLogin import InterfaceLogin
from src.backend.Verification import Verify


def main() -> None:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Budget Buddy")
    app.geometry("1920x1080")
    app.resizable(False, False)

    def handle_login(username: str, password: str) -> None:
        """
        Callback déclenché quand l'utilisateur clique sur le bouton de connexion.
        """
        print(f"Tentative de connexion avec {username}...")
        
        # On crée une instance de ta classe Verify
        verifier = Verify(username, password)
        
        # On vérifie les identifiants
        if verifier.verify():
            print("Connexion réussie !")
            login_page._clear_error()
            # TODO : Cacher la page de login et afficher la page de l'utilisateur
            # login_page.pack_forget() 
            # user_page.show()
        else:
            print("Échec de la connexion.")
            login_page._show_error("Identifiant ou mot de passe incorrect.")

    login_page = InterfaceLogin(master=app, on_login=handle_login)
    login_page.show()

    app.mainloop()


if __name__ == "__main__":
    main()
