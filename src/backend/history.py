from src.database.database import Database

class History:
    @staticmethod
    def get_history_by_account(account_id):
        """
        Récupère l'historique des transactions pour un compte donné.
        """
        db = Database()
        query = """
            SELECT date, transaction_type, amount, category, description 
            FROM history 
            WHERE account_id = ?
            ORDER BY date DESC
        """
        try:
            results = db.fetch_all(query, (account_id,))
            return results
        except Exception as e:
            print(f"Erreur lors de la récupération de l'historique : {e}")
            return []
        finally:
            db.close()
