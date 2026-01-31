import os
import sys
from pathlib import Path

def resource_path(relative_path):
    """Chemin absolu vers une ressource (exe ou script)"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def app_data_path(app_name="WorkingHoursTracking"):
    base = Path.home() / "AppData" / "Local" / app_name
    base.mkdir(parents=True, exist_ok=True)
    return base

EXCEL_PATH = app_data_path() / "data.xlsx"

# Centralisation des en-têtes des tableaux excel et dans l'app
TABLE_HEADERS = ["Date", "Nom du projet", "Heures"]

# Labels du formulaire
FORM_LABELS = ["Date", "Nom du projet", "Heures"]