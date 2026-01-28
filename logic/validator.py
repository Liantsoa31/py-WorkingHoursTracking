from datetime import datetime

def validate_data(date, name, number):
    if not date.strip():
        raise ValueError("La date est obligatoire")
    
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        raise ValueError("La date doit être au format dd-mm-yyyy")
    
    if not name.strip():
        raise ValueError("Le nom est obligatoire")

    if not number.strip():
        raise ValueError("Le chiffre est obligatoire")

    if not number.isdigit():
        raise ValueError("Le chiffre doit être un nombre")
