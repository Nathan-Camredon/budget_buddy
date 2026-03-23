from src.database.database import Database



class Deal:
    def __init__(self):
        self.db = Database()





    # Deposit
    def add_deal(self, account_id, amount, category, description=""):
        """
        Adds a deposit to an account.
        
        Args:
            account_id (int): Account ID.
            amount (float): Deposit amount.
            category (str): Deposit category.
            description (str): Deposit description.
            
        Returns:
            tuple: (bool, str) - Status and message.
        """

        if amount <= 0:
            return False, "Le dépôt doit être positif."

        #Update
        request_update = ''' UPDATE account SET pay = pay + ? WHERE id = ? '''
        self.db.cursor.execute(request_update, (amount, account_id))

        #History
        request_history = ''' INSERT INTO history (account_id, transaction_type, amount, category, description) VALUES (?, 'depot', ?, ?, ?)'''
        self.db.cursor.execute(request_history, (account_id, amount, category, description))

        self.db.conn.commit()
        return True, "Dépôt réalisé avec succès."





    # Withdrawal
    def remove_deal(self, account_id, amount, category, description=""):
        """
        Withdraws an amount from an account.
        
        Args:
            account_id (int): Account ID.
            amount (float): Withdrawal amount.
            category (str): Withdrawal category.
            description (str): Withdrawal description.
            
        Returns:
            tuple: (bool, str) - Status and message.
        """

        if amount <= 0:
            return False, "Le retrait doit être positif."

        #Update
        request_update = ''' UPDATE account SET pay = pay - ? WHERE id = ? '''
        self.db.cursor.execute(request_update, (amount, account_id))

        #History
        request_history = ''' INSERT INTO history (account_id, transaction_type, amount, category, description) VALUES (?, 'retrait', ?, ?, ?)'''
        self.db.cursor.execute(request_history, (account_id, amount, category, description))

        self.db.conn.commit()
        return True, "Retrait réalisé avec succès."





    # Transfer
    
    def transfer_deal(self, account_id, target_account_id, amount, category, description=""):
        """
        Transfers an amount from one account to another.
        
        Args:
            account_id (int): Source account ID.
            target_account_id (int): Destination account ID.
            amount (float): Transfer amount.
            category (str): Transfer category.
            description (str): Transfer description.
            
        Returns:
            tuple: (bool, str) - Status and message.
        """

        if amount <= 0:
            return False, "Le transfert doit être posifif"

        #Update
        request_update = ''' UPDATE account SET pay = pay - ? WHERE id = ? '''
        request_update_target = ''' UPDATE account SET pay = pay + ? WHERE id = ? '''
        self.db.cursor.execute(request_update, (amount, account_id))
        self.db.cursor.execute(request_update_target, (amount, target_account_id))
        print (f"Virement de {amount}€ du compte N°: {account_id} au compte N°: {target_account_id} réalisé avec succès")

        #History
        request_history = ''' INSERT INTO history (account_id, transaction_type, target_account_id, amount, category, description) VALUES (?, 'virement', ?, ?, ?, ?)'''
        self.db.cursor.execute(request_history, (account_id, target_account_id, amount, category, description))

        self.db.conn.commit()
        return True, "Transfert réalisé avec succès."