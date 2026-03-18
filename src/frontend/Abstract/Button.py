import customtkinter as ctk
from typing import Callable, Any, Optional

class Button:
    """
    A reusable Button component encapsulating a customtkinter.CTkButton.
    Used to configure buttons consistently across the application.
    """
    def __init__(self, master: Any, text: str, command: Optional[Callable] = None, **kwargs):
        self._text: str = text
        self._command: Optional[Callable] = command
        
        # We can pass any CustomTkinter Button configurations through kwargs
        # such as width, height, font, fg_color, hover_color, etc.
        self._widget: ctk.CTkButton = ctk.CTkButton(
            master=master, 
            text=self._text, 
            command=self.click, 
            **kwargs
        )

    def click(self, *args, **kwargs) -> None:
        """
        Method called when the button is clicked. 
        It triggers the command passed during initialization if it exists.
        """
        if self._command is not None:
            self._command(*args, **kwargs)

    def get_widget(self) -> ctk.CTkButton:
        """Returns the underlying CTkButton widget."""
        return self._widget

    def configure(self, **kwargs) -> None:
        if 'text' in kwargs:
            self._text = kwargs['text']
        if 'command' in kwargs:
            self._command = kwargs.pop('command')
        self._widget.configure(**kwargs)

    # Layout management methods mimicking Tkinter widgets
    def pack(self, **kwargs) -> None:
        self._widget.pack(**kwargs)

    def grid(self, **kwargs) -> None:
        self._widget.grid(**kwargs)

    def place(self, **kwargs) -> None:
        self._widget.place(**kwargs)
