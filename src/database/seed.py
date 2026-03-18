import sqlite3
from pathlib import Path

# 1. On trouve le chemin du fichier de base de données
db_path = Path(__file__).parent / "budget_buddy.db"

# 2. On se connecte à la base (ça crée le fichier s'il n'existe pas)
conn = sqlite3.connect(db_path)

# Le curseur est un objet qui nous permet d'exécuter des requêtes SQL
cursor = conn.cursor()

# 3. On insère un client de test
# L'utilisation des "?" permet d'insérer les variables de manière sécurisée
try:
    cursor.execute('''
        INSERT INTO customer (login, password, last_name, first_name, email)
        VALUES (?, ?, ?, ?, ?)
    ''', ('jtest', 'mypassword', 'Test', 'Jean', 'jean@test.com'))

    # On récupère l'ID du client qu'on vient tout juste de créer
    customer_id = cursor.lastrowid
    print(f"✅ Client 'Jean Test' créé avec succès (ID : {customer_id})")

    # 4. On crée un compte bancaire lié à ce client
    cursor.execute('''
        INSERT INTO account (customer_id, account_type, pay)
        VALUES (?, ?, ?)
    ''', (customer_id, 'Courant', 1000.0))

    account_id = cursor.lastrowid
    print(f"✅ Compte 'Courant' créé pour Jean avec un solde (pay) de 1000.0 (ID : {account_id})")

    # 5. TRES IMPORTANT : On valide (commit) pour sauvegarder définitivement dans le fichier
    conn.commit()

except sqlite3.IntegrityError:
    # Si on relance le script, l'email 'jean@test.com' existe déjà en base, donc on aura une erreur d'intégrité (UNIQUE constraint)
    print("⚠️ Le client jean@test.com existe déjà dans la base !")

# 6. On ferme la connexion pour libérer le fichier
conn.close()
