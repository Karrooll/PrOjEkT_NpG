import datetime
from Odczyt import utworz_liste_aforyzmow, znajdz_i_nadpisz_aforyzm

def wybierz_aforyzm_na_dzien(aforyzmy, aforyzmy_uzyte, data):
    """Wybiera aforyzm na dany dzień, który nie był jeszcze użyty."""
    # Oblicz różnicę dni między podaną datą a datą 2024-06-5
    # i znajdź indeks w liście aforyzmów za pomocą modulo
    if len(aforyzmy) == 0:
        #Jeśli lista pusta odczytaj od nowa
        aforyzmy = utworz_liste_aforyzmow()
        #Wyczyść uzyte indeksy
        aforyzmy_uzyte.clear()
    indeks = (data - datetime.date(2024, 6, 5)).days % len(aforyzmy)
    aforyzm_na_dzisiaj = aforyzmy[indeks]  # Wybierz aforyzm na podstawie obliczonego indeksu
    return aforyzm_na_dzisiaj, aforyzmy

def zmiana_aforyzmu(aforyzmy, aforyzmy_uzyte, aforyzm_na_dzisiaj):
    #Mechanizm zapisu uzytych aforyzmow i usuwania mozliwosci ich wybrania
    aforyzmy_uzyte.append(aforyzm_na_dzisiaj.id)
    for aforyzm in aforyzmy:
        if aforyzm.id == aforyzm_na_dzisiaj.id:
            #Nadpisanie danych o aforzymie, gdyz zniknie on z listy - stracilibysmy dane o ocenach
            znajdz_i_nadpisz_aforyzm(aforyzm.id, aforyzm.zwroc_srednia(), aforyzm.liczba_ocen + len(aforyzm.oceny))
            aforyzmy.remove(aforyzm)

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
