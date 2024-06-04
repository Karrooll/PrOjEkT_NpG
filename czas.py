import datetime
from aforyzmy_uzyte import sprawdz_czy_uzyty, zapisz_uzyty_aforyzm

def wybierz_aforyzm_na_dzien(aforyzmy, data):
    """Wybiera aforyzm na dany dzień, który nie był jeszcze użyty."""
    while True:  # Pętla, która będzie działać do momentu znalezienia nieużytego aforyzmu
        # Oblicz różnicę dni między podaną datą a datą 2024-06-5
        # i znajdź indeks w liście aforyzmów za pomocą modulo
        indeks = (data - datetime.date(2024, 6, 5)).days % len(aforyzmy)
        aforyzm_na_dzisiaj = aforyzmy[indeks]  # Wybierz aforyzm na podstawie obliczonego indeksu
        
        # Sprawdź, czy aforyzm został już użyty
        if not sprawdz_czy_uzyty(aforyzm_na_dzisiaj):
            # Zapisz aforyzm jako użyty
            zapisz_uzyty_aforyzm(aforyzm_na_dzisiaj)
            return aforyzm_na_dzisiaj  # Zwróć wybrany aforyzm, który nie był jeszcze użyty

def przesun_date_programu(obecna_data):
    # Wyświetl aktualną datę
    print("Aktualna data: ", obecna_data)
    try:
        # Pobierz od użytkownika liczbę dni do przesunięcia
        liczba_dni = int(input("Podaj liczbę dni do przesunięcia: "))
        # Oblicz nową datę, dodając liczbę dni do aktualnej daty
        nowa_data = obecna_data + datetime.timedelta(days=liczba_dni)
        # Wyświetl nową datę
        print("Nowa data: ", nowa_data)
        # Zwróć nową datę
        return nowa_data
    except ValueError:
        # Obsłuż błędne dane wejściowe
        print("Podano niepoprawną wartość, data nie została zmieniona.")
        return obecna_data
