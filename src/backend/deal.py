from src.database.database import Database



class Deal:
    def __init__(self):
        self.db = Database()





    # Deposit
    def add_deal(self, account_id, amount, category, description=""):
        if amount <= 0:
            return False, "Le dépôt doit être positif."

        request_update = ''' UPDATE account SET pay = pay + ? WHERE id = ? '''
        self.db.cursor.execute(request_update, (amount, account_id))

        request_history = ''' INSERT INTO history (account_id, amount, category, description) VALUES (?, ?, ?, ?)'''
        self.db.cursor.execute(request_history, (account_id, amount, category, description))

        self.db.conn.commit()
        return True, "Dépôt réalisé avec succès."





    # Withdrawal
    def remove_deal(self, account_id, amount, category, description=""):
        if amount <= 0:
            return False, "Le retrait doit être positif."

        request_update = ''' UPDATE account SET pay = pay - ? WHERE id = ? '''
        self.db.cursor.execute(request_update, (amount, account_id))

        request_history = ''' INSERT INTO history (account_id, amount, category, description) VALUES (?, ?, ?, ?)'''
        self.db.cursor.execute(request_history, (account_id, amount, category, description))

        self.db.conn.commit()
        return True, "Retrait réalisé avec succès."





    # Transfer
    def transfer_deal(self, account_id, amount, category, description=""):
        if amount <= 0:
            return False, "Le transfert doit être posifif"

        #{}
        request_update = ''' UPDATE account SET pay = pay - ? WHERE id = ? '''
        self.db.cursor.execute(request_update, (amount, account_id))

        request_history = ''' INSERT INTO history (account_id, amount, category, description) VALUES (?, ?, ?, ?)'''
        self.db.cursor.execute(request_history, (account_id, amount, category, description))

        self.db.conn.commit()
        return True, "Transfert réalisé avec succès."