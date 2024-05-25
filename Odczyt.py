from Aforyzm import Aforyzm

def wczytaj_aforzymy_tekst():
    aforyzmy = []
    with open("aforyzmy_testowe.txt", "r", encoding="utf8") as plik: #otwarcie pliku w trybie odczytu
        for line in plik:
            line = line.strip() #usuniecie bialych znakow na koncu i poczatku danej linii
            if line.endswith("*"): #uwzgledniamy znak konczacy *
                odczytany_aforyzm = line[:-1].strip() #odcięcie ostatniego znaku + usunięcie znaków białych
                if odczytany_aforyzm:
                    aforyzmy.append(odczytany_aforyzm) #dodanie do listy tekstów dla aforyzmów

    return aforyzmy

#Główna funkcja odczytująca aforyzmy - funkcja wyżej to funkcja pomocnicza
#tu tworzona jest lista obietków klasy Aforyzm
def utworz_liste_aforyzmow():
    aforyzmy = wczytaj_aforzymy_tekst()
    aforyzmy_class = []

    for aforyzm in aforyzmy:
        aforyzmy_class.append(Aforyzm(aforyzm)) #tworzenie obiektów Aforyzm + dodawanie do listy

    return aforyzmy_class