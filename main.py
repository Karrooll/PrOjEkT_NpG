from Odczyt import utworz_liste_aforyzmow
from czas import wybierz_aforyzm_na_dzien, przesun_date_programu
import datetime

def main():
    aforyzmy = utworz_liste_aforyzmow()
    dzisiejsza_data = datetime.date.today()

    while(True):
        print("\n-----------------AFORYZMY NA KAŻDY DZIEŃ-----------------")
        print("Aby wyświetlić aforyzm na dzisiejszy dzień wciśnij 1")
        print("Aby przesunąć datę programu wciśnij 2")
        print("Aby wyjść z programu wciśnij 0")
        try: # proste menu z obsługą błędu
            wybor = int(input("Podaj opcję: "))
            if wybor == 1:
                aforyzm_na_dzisiaj = wybierz_aforyzm_na_dzien(aforyzmy, dzisiejsza_data)
                aforyzm_na_dzisiaj.wyswietl_aforyzm()
            elif wybor == 2:
                dzisiejsza_data = przesun_date_programu(dzisiejsza_data)
            elif wybor == 0:
                print("Wybrano wyjście z programu!")
                break
            else:
                print("Wybrano nieprawidłową, niedostępną opcję - wybierz jeszcze raz!")
        except ValueError:
            print("Podano wartość niecałkowitą - wybierz jeszcze raz!")

if __name__ == '__main__':
    main()

