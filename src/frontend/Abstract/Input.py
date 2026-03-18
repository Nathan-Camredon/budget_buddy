import customtkinter as ctk
from typing import Any

class Input:
    """
    A reusable Input component encapsulating a customtkinter.CTkEntry.
    Used to configure text input fields consistently across the application.
    """
    def __init__(self, master: Any, placeholder: str = "", **kwargs):
        self._placeholder: str = placeholder
        
        # We can pass any CustomTkinter Entry configurations through kwargs
        # such as width, height, font, fg_color, text_color, show (for passwords), etc.
        self._widget: ctk.CTkEntry = ctk.CTkEntry(
            master=master, 
            placeholder_text=self._placeholder, 
            **kwargs
        )

    def getText(self) -> str:
        """
        Retrieves the current text entered in the input field.
        """
        return self._widget.get()

    def get_widget(self) -> ctk.CTkEntry:
        """Returns the underlying CTkEntry widget."""
        return self._widget

    def configure(self, **kwargs) -> None:
        if 'placeholder' in kwargs:
            self._placeholder = kwargs.pop('placeholder')
            kwargs['placeholder_text'] = self._placeholder
        self._widget.configure(**kwargs)

    # Layout management methods mimicking Tkinter widgets
    def pack(self, **kwargs) -> None:
        self._widget.pack(**kwargs)

    def grid(self, **kwargs) -> None:
        self._widget.grid(**kwargs)

    def place(self, **kwargs) -> None:
        self._widget.place(**kwargs)
