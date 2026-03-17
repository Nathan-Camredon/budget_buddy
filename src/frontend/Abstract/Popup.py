import customtkinter as ctk
from abc import ABC, abstractmethod
from typing import Any


class Popup(ctk.CTkToplevel, ABC):
    """
    Base class for all popup windows in the application.
    Each popup must inherit from this class and implement _build_ui().
    """

    def __init__(self, master: Any, title: str = "", width: int = 400, height: int = 300, **kwargs):
        super().__init__(master, **kwargs)
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)

        # Center the popup over its parent window
        self._center(master)

        # Prevent interaction with the parent window while popup is open
        self.grab_set()

        self._build_ui()

    def _center(self, master: Any) -> None:
        """Centers the popup relative to its parent window."""
        self.update_idletasks()
        try:
            px = master.winfo_x() + (master.winfo_width() // 2) - (self.winfo_width() // 2)
            py = master.winfo_y() + (master.winfo_height() // 2) - (self.winfo_height() // 2)
            self.geometry(f"+{px}+{py}")
        except Exception:
            pass

    @abstractmethod
    def _build_ui(self) -> None:
        """Required method: each popup must build its own UI here."""
        pass

    def close(self) -> None:
        """Close the popup window."""
        self.grab_release()
        self.destroy()
