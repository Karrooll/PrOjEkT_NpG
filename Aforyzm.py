class Aforyzm:
    def __init__(self, tekst, p_id, srednia=0.0, liczba_ocen=0):
        self.tekst = tekst
        self.oceny = []
        self.id = p_id
        self.srednia = srednia
        self.liczba_ocen = liczba_ocen

    def dodaj_ocene(self):
        while True:
            try: #mechanizm dodawania oceny z obsługą błędu
                ocena = int(input("Podaj ocenę z zakresu od 0 do 5: "))
                if ocena >= 0 and ocena <=5:
                    self.oceny.append(ocena)
                    print("Poprawnie dodano ocenę dla aforyzmu!")
                    break
                else:
                    print("Błąd! Ocena spoza dozwolonego zakresu, bądź niecałkowita!")
            except ValueError:
                print("Podano wartość niecałkowitą lub niedozwoloną dla oceny - wybierz jeszcze raz!")

    def wyswietl_oceny(self): #wyświetlanie średniej ocen w zależnosci od przypadku
        print("\nŚrednia ocen dla tego aforyzmu to: ")
        #Dla każdej opcji inny sposób liczenia - zależy od stanu obiektu
        if len(self.oceny) == 0 and self.liczba_ocen == 0:
            print("Brak ocen dla danego aforyzmu!")
        elif len(self.oceny) ==0 and self.liczba_ocen != 0:
            print(self.srednia)
            print("Na podstawie danej ilości ocen: ", (self.liczba_ocen))
        elif len(self.oceny) !=0 and self.liczba_ocen == 0:
            print(sum(self.oceny) / len(self.oceny))
            print("Na podstawie danej ilości ocen: ", len(self.oceny))
        else:
            print((self.srednia*self.liczba_ocen+sum(self.oceny))/(len(self.oceny)+self.liczba_ocen))
            print("Na podstawie danej ilości ocen: ", len(self.oceny)+self.liczba_ocen)

    #Główny mechanizm wyświetlania aforyzmów do main - funkcje powyżej
    #to funkcje pomocniczne
    def wyswietl_aforyzm(self):
        print("\nAforyzm na dzisiejszy dzień to: ")
        print(self.tekst)
        self.wyswietl_oceny()
        print("\nCzy chcesz dodać ocenę dla powyższego aforzymu?")
        while True:
            try: #mechanizm wyboru dodawania oceny z osbluga bledu (zabezpieczenie przed literami i niecalkowitymi)
                print("Wybierz 1, jeśli tak lub 0, jeśli nie: ")
                wybor_ocena = int(input())
                if wybor_ocena == 1:
                    self.dodaj_ocene()
                    break
                elif wybor_ocena == 0:
                    break
                else:
                    print("Wybrano nieprawidłową opcję, wybierz jeszcze raz!")
            except ValueError:
                print("Podano wartość niecałkowitą lub niedozwoloną - wybierz jeszcze raz!")

    def zwroc_srednia(self):
        #Mechanizm analogiczny do wyswietl_oceny - tutaj tym razem zwracamy wartosc sredniej w return
        if len(self.oceny) == 0 and self.liczba_ocen == 0:
            return 0
        elif len(self.oceny) ==0 and self.liczba_ocen != 0:
            return (self.srednia)
        elif len(self.oceny) !=0 and self.liczba_ocen == 0:
            return (sum(self.oceny) / len(self.oceny))
        else:
            return ((self.srednia*self.liczba_ocen+sum(self.oceny))/(len(self.oceny)+self.liczba_ocen))