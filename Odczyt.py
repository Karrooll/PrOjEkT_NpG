from Aforyzm import Aforyzm

def wczytaj_aforzymy_tekst():
    aforyzmy = []
    with open("aforyzmy_testowe.txt", "r", encoding="utf8") as plik:
        for line in plik:
            line = line.strip() #usuniecie bialych znakow na koncu i poczatku danej linii
            if line.endswith("*"): #uwzgledniamy znak konczacy *
                odczytany_aforyzm = line[:-1].strip()
                if odczytany_aforyzm:
                    aforyzmy.append(odczytany_aforyzm)

    return aforyzmy

def utworz_liste_aforyzmow():
    aforyzmy = wczytaj_aforzymy_tekst()
    aforyzmy_class = []

    for aforyzm in aforyzmy:
        aforyzmy_class.append(Aforyzm(aforyzm))

    return aforyzmy_class