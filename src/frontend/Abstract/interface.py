import customtkinter as ctk
from abc import ABC, abstractmethod
from typing import Any


class Interface(ctk.CTkFrame, ABC):
    """
    Base class for all application pages.
    Each page must inherit from this class and implement _build_ui().
    """

    def __init__(self, master: Any, title: str = "", **kwargs):
        super().__init__(master, **kwargs)
        self.title = title
        self._build_ui()

    @abstractmethod
    def _build_ui(self) -> None:
        """Required method: each page must build its own UI here."""
        pass

    def show(self) -> None:
        """Display the page."""
        self.pack(fill="both", expand=True)

    def hide(self) -> None:
        """Hide the page."""
        self.pack_forget()
