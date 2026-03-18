"""
Seed script — inserts a test customer 'Dupont Dupont' with a 1000 € account.
Run once: python src/database/seed.py
"""
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "budget_buddy.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# Insert customer (skip if email already exists)
cursor.execute("""
    INSERT OR IGNORE INTO customer (login, password, name, first_name, email)
    VALUES (?, ?, ?, ?, ?)
""", ("dupont", "dupont1234", "Dupont", "Dupont", "dupont@budgetbuddy.fr"))

customer_id = cursor.lastrowid

# Insert account with 1000 €
cursor.execute("""
    INSERT INTO account (customer_id, account_type, pay)
    VALUES (?, ?, ?)
""", (customer_id, "courant", 1000.0))

conn.commit()
conn.close()

print(f"✅ Client 'Dupont Dupont' créé (id={customer_id}) avec un compte courant de 1000 €.")
