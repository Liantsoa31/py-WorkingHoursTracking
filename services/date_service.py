from datetime import datetime


def get_today_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_month_key(date_str):
    """
    dd-mm-yyyy → yyyy-mm (clé interne)
    """
    date = datetime.strptime(date_str, "%d-%m-%Y")
    return date.strftime("%Y-%m")

def get_month_label(date_str):
    """
    dd-mm-yyyy → Janvier 2026 (affichage)
    """
    date = datetime.strptime(date_str, "%d-%m-%Y")
    return date.strftime("%B %Y").capitalize()