import customtkinter as ctk
from abc import ABC, abstractmethod

class Interface(ctk.CTkFrame, ABC):
    """
    Abstract base class for all application interfaces.
    Inherits from CTkFrame and ABC to define a required interface.
    """

    def __init__(self, master, title="Interface", **kwargs):
        super().__init__(master, **kwargs)
        self.title = title
        self._build_ui()

    @abstractmethod
    def _build_ui(self) -> None:
        """
        Abstract method to build the UI components.
        Must be implemented by subclasses.
        """
        pass

    def show(self) -> None:
        """Show the interface."""
        self.pack(fill="both", expand=True)

    def hide(self) -> None:
        """Hide the interface."""
        self.pack_forget()
