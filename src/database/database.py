import sqlite3
from pathlib import Path

class Database:
    def __init__(self, db_name="budget_buddy.db"):
        # On s'assure que la base de données est créée dans le même dossier que ce fichier
        db_path = Path(__file__).parent / db_name
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Activation des contraintes de clés étrangères (obligatoire sur SQLite)
        self.cursor.execute("PRAGMA foreign_keys = ON;")

        # Table CUSTOMER (Client)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Table ACCOUNT (Compte bancaire)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS account (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                account_type TEXT NOT NULL,
                balance REAL DEFAULT 0.0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
            )
        ''')

        # Table HISTORY (Historique des transactions)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL, 
                amount REAL NOT NULL,
                description TEXT,
                date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES account(id) ON DELETE CASCADE
            )
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    # Test simple pour vérifier que la base se crée bien
    db = Database()
    print("Base de données SQLite et tables créées avec succès !")
    db.close()
