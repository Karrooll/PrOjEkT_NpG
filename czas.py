import datetime

def wybierz_aforyzm_na_dzien(aforyzmy, data):
    indeks = (data - datetime.date(2024, 5, 29)).days % len(aforyzmy)
    return aforyzmy[indeks]

def przesun_date_programu(obecna_data):
    print("Aktualna data: ", obecna_data)
    try:
        liczba_dni = int(input("Podaj liczbę dni do przesunięcia: "))
        nowa_data = obecna_data + datetime.timedelta(days=liczba_dni)
        print("Nowa data: ", nowa_data)
        return nowa_data
    except ValueError:
        print("Podano niepoprawną wartość, data nie została zmieniona.")
        return obecna_data

