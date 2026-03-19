from src.database.database import Database

class AllAccount:
    @staticmethod
    def get_all():
        db = Database()
        query = """
            SELECT c.id, c.login, c.last_name, c.first_name, c.email, c.is_admin, a.account_type, a.pay 
            FROM customer c 
            LEFT JOIN account a ON c.id = a.customer_id
        """
        try:
            results = db.fetch_all(query)
            return results
        except Exception as e:
            print(f"Erreur lors de la récupération des comptes : {e}")
            return []
        finally:
            db.close()
