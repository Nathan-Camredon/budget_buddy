import sqlite3
import os

def seed_history():
    db_path = "src/database/budget_buddy.db"
    if not os.path.exists(db_path):
        print(f"Base de données non trouvée à {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # On vérifie quel account on utilise. Customer ID 2 est Nathan Camredon.
    # On va insérer pour account_id = 1 (qui appartient à customer_id = 2)
    account_id = 1

    transactions = [
        (account_id, 'depot', 1500.0, 'Salaire', 'Virement salaire Mars'),
        (account_id, 'retrait', 45.5, 'Courses', 'Carrefour Express'),
        (account_id, 'retrait', 30.0, 'Loisirs', 'Cinéma Pathé'),
        (account_id, 'depot', 50.0, 'Cadeau', 'Anniversaire mamie'),
        (account_id, 'retrait', 12.5, 'Alimentation', 'Boulangerie'),
        (account_id, 'retrait', 650.0, 'Loyer', 'Loyer mois de Mars'),
        (account_id, 'retrait', 60.0, 'Transport', 'Pass Navigo'),
        (account_id, 'retrait', 25.0, 'Santé', 'Pharmacie'),
    ]

    try:
        # On vide l'historique existant pour repartir à propre (optionnel)
        cursor.execute("DELETE FROM history WHERE account_id = ?", (account_id,))
        
        # Insertion des transactions
        cursor.executemany("""
            INSERT INTO history (account_id, transaction_type, amount, category, description) 
            VALUES (?, ?, ?, ?, ?)
        """, transactions)
        
        # On met à jour le solde (pay) du compte pour qu'il corresponde (Salaire 1500 + Cadeau 50 - autres retraits)
        # Total dépôts : 1550 | Total retraits : 45.5 + 30 + 12.5 + 650 + 60 + 25 = 823
        # Nouveau solde = 1550 - 823 = 727
        cursor.execute("UPDATE account SET pay = 727.0 WHERE id = ?", (account_id,))

        conn.commit()
        print(f"Historique généré avec succès pour le compte ID {account_id} (Nathan Camredon).")
        print("Solde mis à jour à 727,00€.")

    except Exception as e:
        print(f"Erreur lors du seeding : {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    seed_history()
