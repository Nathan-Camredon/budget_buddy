from src.database.database import Database



class HistoryService:
    def __init__(self):
        self.db = Database()



    # Get all history
    def get_all_history(self, account_id):
        """ retrieves the entire transaction history of an account
        
        Args: account_id (int): Account ID.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by date
    def get_history_by_date_desc(self, account_id, date):
        """ Retrieves the transaction history of an account by date (descending)
        
        Args: account_id (int): Account ID.
            date (str): Transaction date.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY date DESC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by date
    def get_history_by_date_asc(self, account_id, date):
        """ Retrieves the transaction history of an account by date (ascending)
        
        Args: account_id (int): Account ID.
            date (str): Transaction date.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY date ASC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by amount
    def get_history_by_amount_desc(self, account_id, amount):
        """ Retrieves the transaction history of an account by amount (descending)
        
        Args: account_id (int): Account ID.
            amount (float): Transaction amount.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY amount DESC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by amount
    def get_history_by_amount_asc(self, account_id, amount):
        """ Retrieves the transaction history of an account by amount (ascending)
        
        Args: account_id (int): Account ID.
            amount (float): Transaction amount.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? ORDER BY amount ASC '''
        self.db.cursor.execute(request, (account_id,))
        return self.db.cursor.fetchall()


    # Get history by category
    def get_history_by_category(self, account_id, category):
        """ Retrieves the transaction history of an account by category
        
        Args: account_id (int): Account ID.
            category (str): Transaction category.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? AND category = ? '''
        self.db.cursor.execute(request, (account_id, category))
        return self.db.cursor.fetchall()


    # Get history by type
    def get_history_by_type(self, account_id, transaction_type):
        """ Retrieves the transaction history of an account by type
        
        Args: account_id (int): Account ID.
            transaction_type (str): Transaction type.
        """
        request = ''' SELECT * FROM history WHERE account_id = ? AND transaction_type = ? '''
        self.db.cursor.execute(request, (account_id, transaction_type))
        return self.db.cursor.fetchall()


    # Get history between two dates
    def get_history_between_dates(self, account_id, start_date, end_date):
        """ Retrieves the history between two specific dates (format YYYY-MM-DD) """
        request = ''' SELECT * FROM history WHERE account_id = ? AND date BETWEEN ? AND ? ORDER BY date DESC '''
        self.db.cursor.execute(request, (account_id, start_date, end_date))
        return self.db.cursor.fetchall()


    # Get history by month
    def get_history_by_month(self, account_id, month, year):
        """ 
        Retrieves the history for a given month.
        month: format '01', '02'...
        year: format '2024'
        """
        # Use strftime to extract the month and year from the SQLite date column
        request = ''' 
            SELECT * FROM history 
            WHERE account_id = ? 
            AND strftime('%m', date) = ? 
            AND strftime('%Y', date) = ? 
            ORDER BY date DESC 
        '''
        self.db.cursor.execute(request, (account_id, month, year))
        return self.db.cursor.fetchall()