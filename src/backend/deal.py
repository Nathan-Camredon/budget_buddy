from src.database.database import Database



class Deal:
    def __init__(self):
        self.db = Database()





    # Deposit
    def add_deal(self, account_id, amount, category, description=""):
        """
        Ajoute un dépôt à un compte.
        
        Args:
            account_id (int): ID du compte.
            amount (float): Montant du dépôt.
            category (str): Catégorie du dépôt.
            description (str): Description du dépôt.
            
        Returns:
            tuple: (bool, str) - Statut et message.
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
        Retire un montant d'un compte.
        
        Args:
            account_id (int): ID du compte.
            amount (float): Montant du retrait.
            category (str): Catégorie du retrait.
            description (str): Description du retrait.
            
        Returns:
            tuple: (bool, str) - Statut et message.
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
        Transfère un montant d'un compte à un autre.
        
        Args:
            account_id (int): ID du compte source.
            target_account_id (int): ID du compte destination.
            amount (float): Montant du transfert.
            category (str): Catégorie du transfert.
            description (str): Description du transfert.
            
        Returns:
            tuple: (bool, str) - Statut et message.
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