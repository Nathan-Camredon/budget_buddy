import customtkinter as ctk
from src.frontend.Abstract.Interface import Interface
from src.frontend.Abstract.Button import Button

class InterfaceUser(Interface):
    def __init__(self, master, controller, **kwargs):
        self.controller = controller
        super().__init__(master, title="Tableau de Bord - Budget Buddy", **kwargs)

    def _build_ui(self) -> None:
        self.configure(fg_color="#121212")  # Dark background matching the screenshot

        # Main Layout: 2 Columns
        self.grid_columnconfigure(0, weight=0, minsize=250) # Sidebar
        self.grid_columnconfigure(1, weight=1)              # Content
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar (Left) ---
        self.sidebar = ctk.CTkFrame(self, fg_color="transparent", width=250)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Account Info (Top Left)
        self.info_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.info_frame.pack(fill="x", pady=(0, 40))

        self.name_label = ctk.CTkLabel(
            self.info_frame, 
            text="Nom du compte", 
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w",
            text_color="#3498db" # Blue-ish like the screenshot links
        )
        self.name_label.pack(fill="x")

        self.id_label = ctk.CTkLabel(
            self.info_frame, 
            text="N° du compte", 
            font=ctk.CTkFont(size=14),
            anchor="w",
            text_color="white"
        )
        self.id_label.pack(fill="x")

        # Sidebar Buttons
        button_font = ctk.CTkFont(size=14, weight="bold")
        button_colors = {"fg_color": "#2c3e50", "hover_color": "#34495e"}

        self.btn_transactions = Button(
            self.sidebar, text="Transactions", command=self.open_transfer_popup, 
            font=button_font, height=45, **button_colors
        )
        self.btn_transactions.pack(fill="x", pady=10)

        self.btn_depots = Button(
            self.sidebar, text="Depots", command=self.open_transfer_popup, 
            font=button_font, height=45, **button_colors
        )
        self.btn_depots.pack(fill="x", pady=10)

        self.btn_retrait = Button(
            self.sidebar, text="Retrait", command=self.open_transfer_popup, 
            font=button_font, height=45, **button_colors
        )
        self.btn_retrait.pack(fill="x", pady=10)

        self.btn_versement = Button(
            self.sidebar, text="Versement", command=self.open_transfer_popup, 
            font=button_font, height=45, **button_colors
        )
        self.btn_versement.pack(fill="x", pady=10)

        # --- Content Area (Right) ---
        self.content_area = ctk.CTkFrame(self, fg_color="transparent")
        self.content_area.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Balance Display (Top Right area)
        self.balance_frame = ctk.CTkFrame(
            self.content_area, 
            fg_color="#dbf3e1", # Light green like the screenshot
            corner_radius=4,
            border_width=1,
            border_color="gray",
            height=60
        )
        self.balance_frame.place(relx=0.5, rely=0.1, anchor="center", relwidth=0.4)

        self.balance_label = ctk.CTkLabel(
            self.balance_frame,
            text="Solde : 0,00€",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="black"
        )
        self.balance_label.pack(expand=True)

        # Main Display Frame (Center) - Now Scrollable for History
        self.display_frame = ctk.CTkScrollableFrame(
            self.content_area, 
            fg_color="#cfcfcf", # Lighter gray for the display area
            corner_radius=0,
            border_width=2,
            border_color="#1a1a1a",
            label_text="Historique des Transactions",
            label_font=ctk.CTkFont(size=16, weight="bold"),
            label_text_color="black"
        )
        self.display_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.6)

        # Logout Button (Bottom Right)
        self.btn_logout = Button(
            self.content_area, 
            text="Quitter", 
            command=self.controller.show_login,
            fg_color="#7f1d1d", # Dark red
            hover_color="#991b1b",
            width=120,
            height=40
        )
        self.btn_logout.place(relx=1.0, rely=1.0, anchor="se")

    def refresh_data(self) -> None:
        """Update the UI with current user data from the controller."""
        user = self.controller.current_user # (id, login, last_name, first_name, email, is_admin, account_type, pay, account_id)
        if user:
            self.name_label.configure(text=f"{user[3]} {user[2]}")
            self.id_label.configure(text=f"N° {user[0]}")
            balance = user[7] if user[7] is not None else 0.0
            self.balance_label.configure(text=f"Solde : {balance:,.2f}€".replace(",", " ").replace(".", ","))
            
            # Load history
            account_id = user[8]
            if account_id:
                self.load_history(account_id)

    def load_history(self, account_id) -> None:
        """Fetch and display transaction history."""
        from src.backend.history_service import HistoryService
        service = HistoryService()
        transactions = service.get_history_by_date_desc(account_id, None) # date param is ignored by the service method implementation but required by signature
        
        # Clear existing items
        for child in self.display_frame.winfo_children():
            child.destroy()
            
        if not transactions:
            ctk.CTkLabel(self.display_frame, text="Aucune transaction trouvée.", text_color="black").pack(pady=20)
            return

        # Header for columns
        header_row = ctk.CTkFrame(self.display_frame, fg_color="gray70", height=30)
        header_row.pack(fill="x", padx=5, pady=2)
        
        headers = ["Date", "Type", "Montant", "Catégorie", "Description"]
        widths = [150, 80, 80, 100, 200]
        
        for i, h in enumerate(headers):
            ctk.CTkLabel(header_row, text=h, width=widths[i], font=ctk.CTkFont(weight="bold"), text_color="black").pack(side="left", padx=5)

        # Data rows
        for t in transactions:
            # HistoryService.get_all_history returns SELECT * (id, account_id, target, type, amount, cat, desc, date)
            # Indices: 7: date, 3: type, 4: amount, 5: category, 6: description
            row = ctk.CTkFrame(self.display_frame, fg_color="transparent")
            row.pack(fill="x", pady=2)
            
            color = "#27ae60" if t[3] == 'depot' else "#c0392b"
            
            ctk.CTkLabel(row, text=str(t[7]), width=widths[0], text_color="black").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=str(t[3]).capitalize(), width=widths[1], text_color=color, font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
            ctk.CTkLabel(row, text=f"{t[4]:.2f}€", width=widths[2], text_color="black").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=str(t[5]), width=widths[3], text_color="black").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=str(t[6]) if t[6] else "", width=widths[4], text_color="black", anchor="w").pack(side="left", padx=5)

    def open_transfer_popup(self):
        user = self.controller.current_user
        if not user:
            return
        account_id = user[8]
        login = user[1]
        
        from src.frontend.transferui import TransferPopup
        popup = TransferPopup(self, account_id=account_id, login=login)
        self.wait_window(popup)
        # Refresh data after popup closes
        self.refresh_data()
