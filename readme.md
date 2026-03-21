# Budget Buddy - Application de Gestion Bancaire

Budget Buddy est une application de gestion de finances personnelles développée avec Python et CustomTkinter. Elle permet de suivre ses comptes, effectuer des dépôts, des retraits et des virements, tout en visualisant l'historique des transactions.

## 🚀 Fonctionnalités

- **Interface Utilisateur Moderne** : Design premium avec support du mode sombre.
- **Gestion de Comptes** : Visualisation du solde en temps réel.
- **Transactions** : Historique détaillé avec filtres par type (Dépôt, Retrait, Virement).
- **Actions Bancaires** : Effectuez des opérations directement depuis l'interface Popup.
- **Visualisation** : Graphiques d'évolution des revenus (en cours de développement).

## 🛠️ Installation

### Prérequis
- Python 3.10 ou supérieur.

### Étapes
1. Clonez le dépôt.
2. Créez un environnement virtuel :
   ```bash
   python -m venv .venv
   ```
3. Activez l'environnement :
   - Windows : `.venv\Scripts\activate`
   - Mac/Linux : `source .venv/bin/activate`
4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Utilisation

Pour lancer l'application principale, utilisez la commande suivante depuis la racine du projet :

```bash
python -m src.frontend.InterfaceLogin
```

> [!IMPORTANT]
> Il est crucial de lancer la commande avec `-m` depuis la racine pour que les imports du package `src` soient correctement résolus.

## 📁 Structure du Projet

- `src/frontend/` : Contient toutes les interfaces graphiques (Login, User, Popups).
- `src/backend/` : Logique métier (vérifications, transactions).
- `src/database/` : Script de création et accès à la base de données SQLite.
- `src/assets/` : Ressources graphiques (logos, icônes).

## 🗃️ Base de données
Le projet utilise SQLite. Le fichier de base de données se trouve dans `src/database/budget_buddy.db`. Si le fichier n'existe pas, il sera créé automatiquement au premier lancement.
