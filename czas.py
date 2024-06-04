import datetime

def wybierz_aforyzm_na_dzien(aforyzmy, data):
    # Oblicz różnicę dni między podaną datą a datą 2024-06-05
    indeks = (data - datetime.date(2024, 6, 5)).days % len(aforyzmy)
    # Wybierz aforyzm na podstawie obliczonego indeksu
    return aforyzmy[indeks]

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
        return nowa_data
    except ValueError:
        # Obsłuż błędne dane wejściowe
        print("Podano niepoprawną wartość, data nie została zmieniona.")
        return obecna_data

