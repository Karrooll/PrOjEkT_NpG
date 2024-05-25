from Odczyt import utworz_liste_aforyzmow
from Aforyzm import Aforyzm

def main():
    aforyzmy = utworz_liste_aforyzmow()
    while(True):
        print("\n-----------------AFORYZMY NA KAŻDY DZIEŃ-----------------")
        print("Aby wyświetlić aforyzm na dzisiejszy dzień wciśnij 1")
        print("Aby wyjść z programu wciśnij 0")
        try: #proste menu z obsługą błędu
            wybor = int(input("Podaj opcję: "))
            if wybor == 1:
                #tutaj będzie trzeba wrzucić mechanizm losowania aforyzmów
                #zależy od pomysłu, można np. utworzyć dwie listy aforyzmów (uzyte/nieuzyte)
                #i przezucac miedzy nimi - sprawdzcie sobie dzialanie teog na malym zbiorze
                aforyzmy[3].wyswietl_aforyzm() # <- aforzym musi być wybierany po wartości na liście
            elif wybor == 0:
                print("Wybrano wyjście z programu!")
                break
            else:
                print("Wybrano nieprawidłową, niedostępną opcję - wybierz jeszcze raz!")
        except ValueError:
            print("Podano wartość niecałkowitą - wybierz jeszcze raz!")



if __name__ == '__main__':
    main()