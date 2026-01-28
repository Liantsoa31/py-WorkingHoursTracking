/#/ Repo structure /#/
WorkHoursTracking/
│
├── main.py                  # Point d’entrée de l’application
│
├── ui/                       # Interface graphique
│   ├── __init__.py
│   ├── app.py                # Fenêtre principale
│   ├── form.py               # Formulaire (nom, chiffre, bouton)
│   └── styles.py             # Styles UI (optionnel)
│
├── logic/                    # Logique métier
│   ├── __init__.py
│   ├── controller.py         # Lien entre UI et logique
│   └── validator.py          # Validation des données
│
├── services/                 # Services techniques
│   ├── __init__.py
│   ├── excel_service.py      # Gestion du fichier Excel
│   └── date_service.py       # Gestion de la date
│
├── config/                   # Configuration
│   ├── __init__.py
│   └── settings.py           # Chemins, nom fichier Excel, etc.
│
├── data/                     # Données générées
│   └── data.xlsx             # Fichier Excel