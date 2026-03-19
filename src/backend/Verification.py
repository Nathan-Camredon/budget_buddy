import sqlite3
from pathlib import Path

class Verify: 
    def __init__(self, id, password):
        self.iid = id
        self.ipassword = password

    def checkpassword(self):
        db_path = "src/database/budget_buddy.db"
        connexion = sqlite3.connect(db_path)
        
        request = "SELECT password FROM customer WHERE email = ? AND password = ?"
        
        cursor = connexion.execute(request, (self.iid, self.ipassword,))
        result = cursor.fetchone()
        
        connexion.close()

        if result is not None:
            return True
        else:
            return False
    
    def checkid(self): 
        db_path = "src/database/budget_buddy.db"
        connexion = sqlite3.connect(db_path)
        
        request = "SELECT email FROM customer WHERE email = ?"
        
        cursor = connexion.execute(request, (self.iid,))
        result = cursor.fetchone()
        
        connexion.close()

        if result is not None:
            return True
        else:
            return False

    def is_admin(self):
        """Vérifie si l'utilisateur est un administrateur (1) ou non (0)."""
        db_path = "src/database/budget_buddy.db"
        connexion = sqlite3.connect(db_path)
        
        request = "SELECT is_admin FROM customer WHERE email = ?"
        
        cursor = connexion.execute(request, (self.iid,))
        result = cursor.fetchone()
        
        connexion.close()
        
        # On retourne True si result[0] est 1, False sinon
        return result[0] == 1 if result else False

    def verify(self):
        """Vérifie l'existence de l'ID et la validité du mot de passe."""
        if self.checkid() and self.checkpassword():
            print("Connexion autorisé")
            return True
        return False


    def uncoding(self):
        pass
