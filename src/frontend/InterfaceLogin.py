import customtkinter as ctk
from typing import Any, Optional, Callable

from src.frontend.Abstract.Interface import Interface
from src.frontend.Abstract.Input import Input
from src.frontend.Abstract.Button import Button


class InterfaceLogin(Interface):
    """
    Login page of the application.
    Inherits from Interface (CTkFrame + ABC).
    Displays a username/password form and a login button.
    """

    def __init__(self, master: Any, on_login: Optional[Callable[[str, str], None]] = None, **kwargs):
        """
        Parameters
        ----------
        master : Any
            The parent widget.
        on_login : Callable[[str, str], None], optional
            Callback called with (username, password) when the user clicks the login button.
        """
        self._on_login = on_login
        super().__init__(master, title="Connexion", **kwargs)

    # ------------------------------------------------------------------
    # Interface contract
    # ------------------------------------------------------------------

    def _build_ui(self) -> None:
        """Build and layout all login UI components."""

        # ── Container card ────────────────────────────────────────────
        self.configure(fg_color="transparent")

        card = ctk.CTkFrame(self, corner_radius=16)
        card.pack(expand=True)

        # ── Title ─────────────────────────────────────────────────────
        ctk.CTkLabel(
            card,
            text="Budget Buddy",
            font=ctk.CTkFont(size=28, weight="bold"),
        ).pack(pady=(32, 4))

        ctk.CTkLabel(
            card,
            text="Connectez-vous à votre espace",
            font=ctk.CTkFont(size=13),
            text_color="gray",
        ).pack(pady=(0, 24))

        # ── Username field ────────────────────────────────────────────
        self._username_input = Input(
            card,
            placeholder="Nom d'utilisateur",
            width=300,
            height=42,
        )
        self._username_input.pack(padx=32, pady=(0, 12))

        # ── Password field ────────────────────────────────────────────
        self._password_input = Input(
            card,
            placeholder="Mot de passe",
            width=300,
            height=42,
            show="●",
        )
        self._password_input.pack(padx=32, pady=(0, 8))

        # ── Error label (hidden by default) ───────────────────────────
        self._error_label = ctk.CTkLabel(
            card,
            text="",
            text_color="#e05252",
            font=ctk.CTkFont(size=12),
        )
        self._error_label.pack(pady=(0, 8))

        # ── Login button ──────────────────────────────────────────────
        self._login_button = Button(
            card,
            text="Se connecter",
            command=self._handle_login,
            width=300,
            height=42,
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self._login_button.pack(padx=32, pady=(0, 32))

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _handle_login(self) -> None:
        """Validate inputs and trigger the on_login callback."""
        username = self._username_input.getText().strip()
        password = self._password_input.getText()

        if not username or not password:
            self._show_error("Veuillez remplir tous les champs.")
            return

        self._clear_error()

        if self._on_login:
            self._on_login(username, password)

    def _show_error(self, message: str) -> None:
        """Display an error message below the password field."""
        self._error_label.configure(text=message)

    def _clear_error(self) -> None:
        """Clear the error message."""
        self._error_label.configure(text="")
