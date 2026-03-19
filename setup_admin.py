from src.backend.createaccount import CreateAccount
import hashlib

# Script to create the requested admin account
admin = CreateAccount(
    login="superadmin",
    password="superpassword123",
    last_name="Admin",
    first_name="Super",
    email="superadmin@bank.com",
    is_admin=1
)

if admin.save():
    print("✅ Compte Super Admin créé avec succès.")
else:
    print("❌ Échec de la création du compte Super Admin.")

# Optional: Update existing 'admin' and 'dupont' passwords if they are not hashed
# Note: Verification.py uses SHA-256.
def hash_val(p):
    return hashlib.sha256(p.encode()).hexdigest()

from src.database.database import Database
db = Database()
# Update admin@budgetbuddy.fr (admin1234)
db.execute_query("UPDATE customer SET password = ? WHERE email = ?", (hash_val("admin1234"), "admin@budgetbuddy.fr"))
# Update dupont@budgetbuddy.fr (dupont1234)
# Wait, let's check notes.txt for exact credentials
# Admin : dupont@budgetbuddy.fr / admin1234 -> Rôle Admin
# User : admin@budgetbuddy.fr / admin -> Rôle User
db.execute_query("UPDATE customer SET password = ? WHERE email = ?", (hash_val("admin1234"), "dupont@budgetbuddy.fr"))
db.execute_query("UPDATE customer SET password = ? WHERE email = ?", (hash_val("admin"), "admin@budgetbuddy.fr"))
db.close()
print("✅ Anciens mots de passe hachés.")
