import customtkinter as ctk

from src.frontend.Abstract.Popup import Popup
from src.frontend.Abstract.Button import Button
from src.database.database import Database
from src.backend.deal import Deal

class CustomWithdrawalDialog(ctk.CTkToplevel):
    def __init__(self, master, title="Retrait"):
        super().__init__(master)
        self.title(title)
        self.geometry("350x250")
        self.resizable(False, False)
        
        # Center the dialog
        self.update_idletasks()
        try:
            px = master.winfo_x() + (master.winfo_width() // 2) - (self.winfo_width() // 2)
            py = master.winfo_y() + (master.winfo_height() // 2) - (self.winfo_height() // 2)
            self.geometry(f"+{px}+{py}")
        except Exception:
            pass
            
        self.grab_set()
        
        self.amount = None
        self.payment_type = None
        
        # Setup UI
        ctk.CTkLabel(self, text="Montant du retrait (€) :").pack(pady=(20, 5))
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Ex: 50.00")
        self.amount_entry.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self, text="Type de paiement :").pack(pady=(10, 5))
        self.type_combo = ctk.CTkComboBox(self, values=["Carte Bancaire", "Espèces", "Virement", "Chèque"])
        self.type_combo.pack(pady=5, padx=20, fill="x")
        self.type_combo.set("Carte Bancaire")
        
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=20, fill="x")
        
        ctk.CTkButton(btn_frame, text="Annuler", fg_color="gray", command=self.cancel).pack(side="left", padx=20, expand=True)
        ctk.CTkButton(btn_frame, text="Valider", command=self.confirm).pack(side="right", padx=20, expand=True)
        
    def confirm(self):
        val = self.amount_entry.get()
        if val:
            self.amount = val
            self.payment_type = self.type_combo.get()
            self.destroy()
            
    def cancel(self):
        self.destroy()
        
    def get_amount(self):
        return self.amount
        
    def get_payment_type(self):
        return self.payment_type


class TransferPopup(Popup):
    """
    Popup interface for banking transactions.
    Inherits from the abstract Popup class and links to the database.
    """

    def __init__(self, master, account_id: int = None, login: str = None, **kwargs):
        self.db = Database()
        
        # If login is provided, find the associated account_id
        if login and not account_id:
            account_id = self._get_account_id_from_login(login)
        
        self.account_id = account_id or 1 # Fallback to 1 for safety
        
        # Default size inspired by the image aspect ratio
        super().__init__(master, title="Transactions", width=1100, height=750, **kwargs)
        self._load_data()

    def _build_ui(self) -> None:
        """Construct the UI elements for the transaction interface."""
        # Main background color
        self.configure(fg_color="#1a1a1a")

        # --- Layout structure ---
        # Sidebar for navigation
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="transparent")
        sidebar.pack(side="left", fill="y", padx=30, pady=40)

        # Header Section (Title + Balance)
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self._build_sidebar(sidebar)
        self._build_header(main_container)
        self._build_content(main_container)
        self._build_footer(main_container)

    def _build_sidebar(self, parent):
        """Build the left sidebar with action buttons."""
        buttons = [
            ("Transactions", self._load_data),
            ("Depots", self._deposit),
            ("Retrait", self._withdraw),
            ("Versement", self._transfer)
        ]

        for text, cmd in buttons:
            btn = Button(
                master=parent, 
                text=text, 
                command=cmd,
                width=200,
                height=55,
                font=ctk.CTkFont(size=22, weight="bold"),
                fg_color="#3d4450",  # Metallic grey/blue appearance
                hover_color="#5a6270",
                corner_radius=5
            )
            btn.pack(pady=20)

    def _build_header(self, parent):
        """Build the top header with title and balance."""
        header_frame = ctk.CTkFrame(parent, fg_color="transparent")
        header_frame.pack(fill="x", pady=(10, 20))

        title_label = ctk.CTkLabel(
            header_frame, 
            text="TRANSACTIONS", 
            font=ctk.CTkFont(size=50, weight="bold"),  # Use default bold for better compatibility
            text_color="white"
        )
        title_label.pack(pady=(0, 20))

        # Solde display box
        balance_frame = ctk.CTkFrame(header_frame, fg_color="#d8ead3", corner_radius=5)
        balance_frame.pack(anchor="e", padx=50)  # Align to the right side like in the image

        self.balance_label = ctk.CTkLabel(
            balance_frame, 
            text="Solde : ---€", 
            font=ctk.CTkFont(family="Inter", size=32, weight="bold"),
            text_color="black",
            padx=30,
            pady=15
        )
        self.balance_label.pack()

    def _build_content(self, parent):
        """Build the main content area (grey gradient-like box)."""
        content_box = ctk.CTkFrame(
            parent, 
            fg_color="#616161", 
            border_width=2, 
            border_color="#424242",
            corner_radius=10
        )
        content_box.pack(fill="both", expand=True, padx=10, pady=20)
        
        # Add a controls bar for sorting
        controls_bar = ctk.CTkFrame(content_box, fg_color="transparent")
        controls_bar.pack(fill="x", side="top", padx=10, pady=5)
        
        self.sort_var = ctk.StringVar(value="Date (Plus récent)")
        self.sort_combo = ctk.CTkComboBox(
            controls_bar, 
            variable=self.sort_var,
            values=["Date (Plus récent)", "Date (Plus ancien)", "Montant (Croissant)", "Montant (Décroissant)"],
            command=self._on_sort_change,
            width=180
        )
        self.sort_combo.pack(side="right", padx=5)
        ctk.CTkLabel(controls_bar, text="Trier par :").pack(side="right", padx=5)
        
        # Internal header bar in the box (mimicking the image)
        header_bar = ctk.CTkFrame(content_box, height=40, fg_color="#424242", corner_radius=0)
        header_bar.pack(fill="x", side="top")
        
        # Add labels for columns (placeholders)
        columns = ["Date", "Description", "Montant", "Type"]
        for col in columns:
            lbl = ctk.CTkLabel(header_bar, text=col, font=ctk.CTkFont(weight="bold"))
            lbl.pack(side="left", expand=True)

        # Container for entries (Scrollable if needed, but here simple frame)
        self.entries_container = ctk.CTkScrollableFrame(content_box, fg_color="transparent")
        self.entries_container.pack(fill="both", expand=True, padx=5, pady=5)

    def _on_sort_change(self, choice):
        """Callback for the sort combobox."""
        self._load_data()

    def _build_footer(self, parent):
        """Build the footer with graph and close button."""
        footer_frame = ctk.CTkFrame(parent, fg_color="transparent")
        footer_frame.pack(fill="x", side="bottom")

        # Mock Graph drawing using Canvas
        graph_canvas = ctk.CTkCanvas(
            footer_frame, 
            width=300, 
            height=120, 
            bg="#1a1a1a", 
            highlightthickness=0
        )
        graph_canvas.pack(pady=10)

        # Draw axis
        graph_canvas.create_line(10, 110, 290, 110, fill="grey")  # X
        graph_canvas.create_line(10, 10, 10, 110, fill="grey")   # Y
        
        # Add labels for axes
        graph_canvas.create_text(15, 10, text="Montant", fill="grey", anchor="w", font=ctk.CTkFont(size=10))
        graph_canvas.create_text(290, 120, text="Temps", fill="grey", anchor="se", font=ctk.CTkFont(size=10))

        # Add scale markers (Montants clés)
        # 0€ at the bottom
        graph_canvas.create_text(5, 110, text="0€", fill="grey", anchor="e", font=ctk.CTkFont(size=9))
        # 500€ in the middle
        graph_canvas.create_text(5, 60, text="500€", fill="grey", anchor="e", font=ctk.CTkFont(size=9))
        graph_canvas.create_line(10, 60, 290, 60, fill="#333333", dash=(2, 4))
        # 1000€ at the top
        graph_canvas.create_text(5, 15, text="1000€", fill="grey", anchor="e", font=ctk.CTkFont(size=9))
        graph_canvas.create_line(10, 15, 290, 15, fill="#333333", dash=(2, 4))

        # Draw decorative lines
        points_red = [(10, 100), (50, 80), (100, 90), (150, 40), (200, 70), (250, 30), (290, 20)]
        points_grey = [(10, 95), (50, 85), (100, 80), (150, 60), (200, 50), (250, 40), (290, 35)]
        
        for i in range(len(points_red)-1):
            graph_canvas.create_line(points_red[i], points_red[i+1], fill="#e57373", width=2)
            graph_canvas.create_line(points_grey[i], points_grey[i+1], fill="#bdbdbd", width=2, dash=(2, 2))

        # Small red logout square at bottom-right
        btn_close = Button(
            footer_frame, 
            text="Retour", 
            command=self.close,
            width=120,
            height=35,
            fg_color="#8b0000",
            hover_color="#a00000",
            corner_radius=5
        )
        btn_close.pack(side="right", padx=20, pady=10)

    def _load_data(self):
        """Fetch real data from the database and update the UI."""
        if not self.account_id:
            return

        # 1. Update Balance
        try:
            query_balance = "SELECT pay FROM account WHERE id = ?"
            result = self.db.fetch_all(query_balance, (self.account_id,))
            if result:
                balance = result[0][0]
                self.balance_label.configure(text=f"Solde : {balance:.2f}€")
        except Exception as e:
            print(f"Erreur chargement solde: {e}")

        # 2. Update Transactions
        try:
            order_clause = "ORDER BY date DESC"
            if hasattr(self, 'sort_var'):
                sort_val = self.sort_var.get()
                if sort_val == "Date (Plus ancien)":
                    order_clause = "ORDER BY date ASC"
                elif sort_val == "Montant (Croissant)":
                    order_clause = "ORDER BY amount ASC"
                elif sort_val == "Montant (Décroissant)":
                    order_clause = "ORDER BY amount DESC"

            query_history = f"""
                SELECT date, description, amount, transaction_type 
                FROM history 
                WHERE account_id = ? 
                {order_clause} 
                LIMIT 10
            """
            history = self.db.fetch_all(query_history, (self.account_id,))
            
            # Clear previous items if any
            for child in self.entries_container.winfo_children():
                child.destroy()
                
            for row in history:
                row_frame = ctk.CTkFrame(self.entries_container, fg_color="transparent")
                row_frame.pack(fill="x", pady=2)
                
                # Format: Date | Desc | Amount | Type
                date_str = row[0].split(" ")[0] if row[0] else ""
                ctk.CTkLabel(row_frame, text=date_str, width=150).pack(side="left", padx=10)
                ctk.CTkLabel(row_frame, text=row[1] or "---", width=250).pack(side="left", padx=10)
                
                color = "#81c784" if row[3] == "depot" else "#e57373"
                prefix = "+" if row[3] == "depot" else "-"
                ctk.CTkLabel(row_frame, text=f"{prefix}{row[2]:.2f}€", text_color=color, width=100, font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10)
                ctk.CTkLabel(row_frame, text=row[3], width=100).pack(side="left", padx=10)

        except Exception as e:
            print(f"Erreur chargement historique: {e}")

    # --- Backend Actions ---
    def _deposit(self):
        """Open a dialog to add a deposit."""
        dialog = ctk.CTkInputDialog(text="Entrez le montant du dépôt (€):", title="Dépôt")
        amount = dialog.get_input()
        if amount:
            try:
                val = float(amount)
                deal = Deal()
                success, msg = deal.add_deal(self.account_id, val, "Dépôt", "Dépôt via UI")
                if success:
                    self._load_data()
            except ValueError:
                pass

    def _withdraw(self):
        """Open a custom dialog to make a withdrawal with payment type."""
        dialog = CustomWithdrawalDialog(self, title="Retrait")
        self.wait_window(dialog)
        
        amount = dialog.get_amount()
        payment_type = dialog.get_payment_type()
        
        if amount and payment_type:
            try:
                val = float(amount)
                deal = Deal()
                # Use payment_type as the category
                success, msg = deal.remove_deal(self.account_id, val, payment_type, f"Retrait par {payment_type}")
                if success:
                    self._load_data()
            except ValueError:
                pass

    def _transfer(self):
        """Open a dialog for a transfer (Virement)."""
        # Simplified for now: ask for target ID and amount
        dialog_id = ctk.CTkInputDialog(text="ID du compte destinataire:", title="Virement")
        target_id = dialog_id.get_input()
        if target_id:
            dialog_amt = ctk.CTkInputDialog(text="Montant du virement (€):", title="Virement")
            amount = dialog_amt.get_input()
            if amount:
                try:
                    val = float(amount)
                    deal = Deal()
                    success, msg = deal.transfer_deal(self.account_id, int(target_id), val, "Virement", "Virement via UI")
                    if success:
                        self._load_data()
                except (ValueError, TypeError):
                    pass

    def _get_account_id_from_login(self, login: str) -> int:
        """Find the first account ID associated with a login or email."""
        try:
            query = """
                SELECT a.id 
                FROM account a 
                JOIN customer c ON a.customer_id = c.id 
                WHERE c.email = ? OR c.login = ? 
                LIMIT 1
            """
            result = self.db.fetch_all(query, (login, login))
            return result[0][0] if result else 1
        except Exception:
            return 1
