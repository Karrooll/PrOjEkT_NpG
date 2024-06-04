import os

# Ścieżka do pliku z użytymi aforyzmami
UŻYTE_AFORYZMY_FILE = 'Pliki_do_czytania/uzyte_aforyzmy.txt'

def sprawdz_czy_uzyty(aforyzm):
    """Sprawdza, czy dany aforyzm był już użyty."""
    if os.path.exists(UŻYTE_AFORYZMY_FILE):
        with open(UŻYTE_AFORYZMY_FILE, 'r', encoding='utf-8') as file:
            uzyte_aforyzmy = file.read().splitlines()
            if aforyzm in uzyte_aforyzmy:
                return True
    return False

def zapisz_uzyty_aforyzm(aforyzm):
    """Zapisuje dany aforyzm jako użyty."""
    with open(UŻYTE_AFORYZMY_FILE, 'a', encoding='utf-8') as file:
        file.write(f'{aforyzm}\n')
