class Aforyzm:
    def __init__(self, tekst, p_id):
        self.tekst = tekst
        self.oceny = []
        self.id = p_id

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

    def wyswietl_oceny(self): #wyświetlanie średniej ocen
        print("\nŚrednia ocen dla tego aforyzmu to: ")
        if len(self.oceny) == 0:
            print("Brak ocen dla danego aforyzmu!")
        else:
            print(sum(self.oceny)/len(self.oceny))
            print("Na podstawie danej ilości ocen: ", len(self.oceny))

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