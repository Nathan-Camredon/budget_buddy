from src.database.database import Database

class CreateAccount:
    def __init__(self, login, password, name, first_name, email, is_admin=0):
        self.login = login
        self.password = password
        self.name = name
        self.first_name = first_name
        self.email = email
        self.is_admin = is_admin
        self.db = Database()

    def save(self):
        query_customer = """
            INSERT INTO customer (login, password, name, first_name, email, is_admin)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        params_customer = (self.login, self.password, self.name, self.first_name, self.email, self.is_admin)
        
        try:
            # Create Customer
            customer_id = self.db.execute_query(query_customer, params_customer)
            
            # Create Default Bank Account (if not admin)
            if self.is_admin == 0:
                query_account = """
                    INSERT INTO account (customer_id, account_type, pay)
                    VALUES (?, ?, ?)
                """
                params_account = (customer_id, "Courant", 0.0)
                self.db.execute_query(query_account, params_account)
            
            print(f"Compte pour {self.login} créé avec succès.")
            return True
        except Exception as e:
            print(f"Erreur lors de la création du compte : {e}")
            return False
        finally:
            self.db.close()
