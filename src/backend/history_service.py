from src.database.database import Database



class HistoryService:
    def __init__(self):
        self.db = Database()



    # Get all history
    def get_all_history(self, account_id):
        """ Recupère tout l'historique des transactions d'un compte
        
        Args: account_id (int): ID du compte.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by date
    def get_history_by_date_desc(self, account_id, date):
        """ Recupère l'historique des transactions d'un compte par date
        
        Args: account_id (int): ID du compte.
            date (str): Date de la transaction.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY date DESC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by date
    def get_history_by_date_asc(self, account_id, date):
        """ Recupère l'historique des transactions d'un compte par date
        
        Args: account_id (int): ID du compte.
            date (str): Date de la transaction.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY date ASC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by amount
    def get_history_by_amount_desc(self, account_id, amount):
        """ Recupère l'historique des transactions d'un compte par montant
        
        Args: account_id (int): ID du compte.
            amount (float): Montant de la transaction.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY amount DESC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by amount
    def get_history_by_amount_asc(self, account_id, amount):
        """ Recupère l'historique des transactions d'un compte par montant
        
        Args: account_id (int): ID du compte.
            amount (float): Montant de la transaction.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY amount ASC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by category
    def get_history_by_category(self, account_id, category):
        """ Recupère l'historique des transactions d'un compte par catégorie
        
        Args: account_id (int): ID du compte.
            category (str): Catégorie de la transaction.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? AND category = ? '''
        self.db.cursor.execute(request, (account_id, category))
        return self.db.cursor.fetchall()


    # Get history by type
    def get_history_by_type(self, account_id, transaction_type):
        """ Recupère l'historique des transactions d'un compte par type
        
        Args: account_id (int): ID du compte.
            transaction_type (str): Type de la transaction.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? AND transaction_type = ? '''
        self.db.cursor.execute(request, (account_id, transaction_type))
        return self.db.cursor.fetchall()


    # Get history between two dates
    def get_history_between_dates(self, account_id, start_date, end_date):
        """ Recupère l'historique entre deux dates précise (format YYYY-MM-DD) """
        request = ''' SELECT * FROM history WHERE account_id = ? AND date BETWEEN ? AND ? ORDER BY date DESC '''
        self.db.cursor.execute(request, (account_id, start_date, end_date))
        return self.db.cursor.fetchall()


    # Get history by month
    def get_history_by_month(self, account_id, month, year):
        """ 
        Recupère l'historique pour un mois donné.
        month: format '01', '02'...
        year: format '2024'
        """
        # On utilise strftime pour extraire le mois et l'année de la colonne date de SQLite
        request = ''' 
            SELECT * FROM history 
            WHERE account_id = ? 
            AND strftime('%m', date) = ? 
            AND strftime('%Y', date) = ? 
            ORDER BY date DESC 
        '''
        self.db.cursor.execute(request, (account_id, month, year))
        return self.db.cursor.fetchall()