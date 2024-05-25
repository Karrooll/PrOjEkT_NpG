class Aforyzm:
    def __init__(self, tekst):
        self.tekst = tekst
        self.oceny = []

    def dodaj_ocene(self):
        ocena = int(input("Podaj ocenę z zakresu od 0 do 5: "))
        if ocena >= 0 and ocena <=5 and isinstance(ocena, int):
            self.oceny.append(ocena)
            print("Poprawnie dodano ocenę dla aforyzmu!")
        else:
            print("Błąd! Ocena spoza dozwolonego zakresu, bądź niecałkowita!")

    def wyswietl_aforyzm(self):
        print("Aforyzm na dzisiejszy dzień to: ")
        print(self.tekst)
        print("\nCzy chcesz dodać ocenę dla powyższego aforzymu?")
        print("Wybierz 1, jeśli tak lub 0, jeśli nie")