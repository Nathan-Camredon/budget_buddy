"""
Seed script — inserts a test customer 'Dupont Dupont' with a 1000 € account.
Run once: python src/database/seed.py
"""
from pathlib import Path
import sys

# Ajout du dossier src au sys.path pour permettre l'import de database
root = Path(__file__).parent.parent.parent
sys.path.append(str(root))

from src.database.database import Database

db = Database()
conn = db.conn
cursor = db.cursor
cursor.execute("PRAGMA foreign_keys = ON;")

# Insert regular customer
cursor.execute("""
    INSERT OR IGNORE INTO customer (login, password, name, first_name, email, is_admin)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("dupont", "dupont1234", "Dupont", "Dupont", "dupont@budgetbuddy.fr", 0))

# Get regular customer id
cursor.execute("SELECT id FROM customer WHERE email = ?", ("dupont@budgetbuddy.fr",))
customer_id = cursor.fetchone()[0]

# Insert admin customer
cursor.execute("""
    INSERT OR IGNORE INTO customer (login, password, name, first_name, email, is_admin)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("admin", "admin1234", "Admin", "System", "admin@budgetbuddy.fr", 1))

# Insert account with 1000 € for the regular customer
cursor.execute("""
    INSERT OR IGNORE INTO account (customer_id, account_type, pay)
    VALUES (?, ?, ?)
""", (customer_id, "courant", 1000.0))

conn.commit()
conn.close()

print(f"✅ Client 'Dupont Dupont' créé (id={customer_id}) avec un compte courant de 1000 €.")
