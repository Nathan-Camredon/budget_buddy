import customtkinter as ctk
from src.frontend.Abstract.Interface import Interface
from src.frontend.Abstract.Button import Button
from src.frontend.Abstract.Input import Input
from src.backend.allaccount import AllAccount
from src.backend.createaccount import CreateAccount
from tkinter import messagebox

class InterfaceAdmin(Interface):
    def __init__(self, master, controller, **kwargs):
        self.controller = controller
        super().__init__(master, title="Administration", **kwargs)

    def _build_ui(self) -> None:
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Left Side: Account List ---
        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ctk.CTkLabel(
            self.list_frame, 
            text="Liste des Comptes", 
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=10)

        # Headers
        header_frame = ctk.CTkFrame(self.list_frame, fg_color="gray30")
        header_frame.pack(fill="x", padx=5, pady=2)
        headers = ["ID", "Login", "Nom", "Prénom", "Email", "Admin", "Type", "Solde"]
        widths = [40, 100, 100, 100, 150, 60, 80, 80]
        for i, header in enumerate(headers):
            lbl = ctk.CTkLabel(header_frame, text=header, width=widths[i], anchor="w")
            lbl.pack(side="left", padx=5)

        self.scrollable_list = ctk.CTkScrollableFrame(self.list_frame)
        self.scrollable_list.pack(fill="both", expand=True, padx=5, pady=5)

        # --- Right Side: Create Account Form ---
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            self.form_frame, 
            text="Créer un Compte", 
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=10)

        self.inputs = {}
        fields = [
            ("Login", "login"),
            ("Mot de Passe", "password"),
            ("Nom", "name"),
            ("Prénom", "first_name"),
            ("Email", "email")
        ]

        for label_text, key in fields:
            ctk.CTkLabel(self.form_frame, text=label_text).pack(pady=(5, 0))
            inp = Input(
                self.form_frame, 
                placeholder=label_text, 
                show="*" if key == "password" else ""
            )
            inp.pack(pady=5, padx=10, fill="x")
            self.inputs[key] = inp

        self.is_admin_var = ctk.BooleanVar(value=False)
        self.admin_check = ctk.CTkCheckBox(self.form_frame, text="Administrateur", variable=self.is_admin_var)
        self.admin_check.pack(pady=10)

        Button(
            self.form_frame, 
            text="Créer le compte", 
            command=self.on_create_account
        ).pack(pady=10, padx=10, fill="x")

        Button(
            self.form_frame, 
            text="Actualiser", 
            command=self.load_accounts
        ).pack(pady=5, padx=10, fill="x")

        Button(
            self.form_frame, 
            text="Se déconnecter", 
            fg_color="transparent",
            border_width=2,
            command=self.controller.show_login
        ).pack(pady=20, padx=10, fill="x", side="bottom")

        # Initial Load
        self.load_accounts()

    def load_accounts(self):
        # Clear current list
        for child in self.scrollable_list.winfo_children():
            child.destroy()

        accounts = AllAccount.get_all()
        widths = [40, 100, 100, 100, 150, 60, 80, 80]

        for acc in accounts:
            row = ctk.CTkFrame(self.scrollable_list, fg_color="transparent")
            row.pack(fill="x", pady=2)
            
            # Fields: id, login, name, first_name, email, is_admin, account_type, pay
            is_admin_str = "Oui" if acc[5] else "Non"
            type_str = acc[6] if acc[6] else "N/A"
            balance_str = f"{acc[7]} €" if acc[7] is not None else "N/A"
            
            data = [acc[0], acc[1], acc[2], acc[3], acc[4], is_admin_str, type_str, balance_str]
            for i, val in enumerate(data):
                lbl = ctk.CTkLabel(row, text=str(val), width=widths[i], anchor="w")
                lbl.pack(side="left", padx=5)

    def on_create_account(self):
        data = {key: inp.getText() for key, inp in self.inputs.items()}
        data['is_admin'] = 1 if self.is_admin_var.get() else 0

        # Basic validation
        if not all([data['login'], data['password'], data['name'], data['first_name'], data['email']]):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        creator = CreateAccount(**data)
        if creator.save():
            messagebox.showinfo("Succès", "Compte créé avec succès !")
            # Clear inputs
            for inp in self.inputs.values():
                # Manually clear the widget text as Input class doesn't have clear method
                inp.get_widget().delete(0, 'end')
            self.is_admin_var.set(False)
            self.load_accounts()
        else:
            messagebox.showerror("Erreur", "Échec de la création du compte (l'email est peut-être déjà utilisé).")