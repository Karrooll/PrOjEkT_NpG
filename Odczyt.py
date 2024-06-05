import csv
from Aforyzm import Aforyzm

def wczytaj_aforyzmy_tekst():
    aforyzmy = []
    #Wczytanie danych o aforyzmach z pliku tekstowego
    with open("aforyzmy_testowe.csv", "r", encoding="utf8") as plik:
        #Odczytanie csv
        csv_reader = csv.reader(plik)
        next(csv_reader)  #Pomijamy nagłówek
        for row in csv_reader:
            if row:
                #Wczytuje odpoweidnie dane, dla sredniej i liczby ocen 0 jesli dana kolumna jest pusta
                p_id = int(row[0])
                tekst = row[1].strip()
                srednia = float(row[2]) if row[2] else 0.0
                liczba_ocen = int(row[3]) if row[3] else 0
                #Tworzenie krotki aforyzmu
                aforyzmy.append((p_id, tekst, srednia, liczba_ocen))
    return aforyzmy

def utworz_liste_aforyzmow():
    #Wczytywanie listy krotek o aforyzmach
    aforyzmy = wczytaj_aforyzmy_tekst()
    aforyzmy_class = []

    #Tworzenie obiektu klasy aforyzm
    for p_id, tekst, srednia, liczba_ocen in aforyzmy:
        aforyzmy_class.append(Aforyzm(tekst, p_id, srednia, liczba_ocen))
    #Zwrot listy obiektów
    return aforyzmy_class

def znajdz_i_nadpisz_aforyzm(aforyzm_id, nowa_srednia, nowa_liczba_ocen):
    #Wczytanie gotowej listy obiektów klasy aforyzm
    aforyzmy = utworz_liste_aforyzmow()
    znaleziony = False

    #Wyszukiwanie aforyzmu, ktorego dane chcemy uaktualnic po id
    for aforyzm in aforyzmy:
        if aforyzm.id == aforyzm_id:
            aforyzm.srednia = nowa_srednia
            aforyzm.liczba_ocen = nowa_liczba_ocen
            znaleziony = True
            break

    #Dokonanie zmian w pliku csv
    if znaleziony:
        with open("aforyzmy_testowe.csv", "w", newline='', encoding="utf8") as plik:
            #Zapis w konkretnym pliku
            csv_writer = csv.writer(plik)
            #Oraz w konkretnych kolumnach
            csv_writer.writerow(["ID", "Aforyzm", "Średnia", "Ilość liczb"])
            for aforyzm in aforyzmy:
                csv_writer.writerow([aforyzm.id, aforyzm.tekst, aforyzm.srednia, aforyzm.liczba_ocen])
        print("Aforyzm zaktualizowany pomyślnie.")
    else:
        print("Aforyzm nie został znaleziony.")

def zapis_koncowy(aforyzmy):
    #Funkcja zbiorcza zapisujaca liste aforyzmow funkcja znajdz_i_nadpisz_aforyzm
    for aforyzm in aforyzmy:
        znajdz_i_nadpisz_aforyzm(aforyzm.id, aforyzm.zwroc_srednia() , aforyzm.liczba_ocen+len(aforyzm.oceny))