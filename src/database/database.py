import sqlite3
from pathlib import Path

class Database:
    def __init__(self, db_name="budget_buddy.db"):
        db_path = Path(__file__).parent / db_name
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Activation des contraintes de clés étrangères (obligatoire sur SQLite)
        self.cursor.execute("PRAGMA foreign_keys = ON;")

        # Table CUSTOMER 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                first_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Table ACCOUNT 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS account (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                account_type TEXT NOT NULL,
                pay REAL DEFAULT 10.0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
            )
        ''')

        # Table HISTORY (Historique des transactions)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER NOT NULL,
                transaction_type TEXT CHECK(transaction_type IN ('depot', 'retrait', 'virement')) NOT NULL, 
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES account(id) ON DELETE CASCADE
            )
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    # Test
    db = Database()
    print("Base de données SQLite et tables créées avec succès !")
    db.close()
