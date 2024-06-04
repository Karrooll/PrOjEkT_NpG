from Odczyt import utworz_liste_aforyzmow
from czas import wybierz_aforyzm_na_dzien, przesun_date_programu
import datetime
from muzyka import odtworz_melodie

def main():
    # Odtwarzanie melodii po uruchomieniu programu
    odtworz_melodie()
    
    # Utworzenie listy aforyzmów
    aforyzmy = utworz_liste_aforyzmow()
    # Ustawienie dzisiejszej daty
    dzisiejsza_data = datetime.date.today()

    while True:
        # Wyświetlanie menu programu
        print('\n----------------AFORYZMY NA KAŻDY DZIEŃ----------------')
        print("Aby wyświetlić aforyzm na dzisiejszy dzień wciśnij 1")
        print("Aby przesunąć datę programu wciśnij 2")
        print("Aby wyjść z programu wciśnij 0")
        try:
            # Pobranie wyboru użytkownika
            wybor = int(input("Podaj opcję: "))
            if wybor == 1:
                # Wybranie i wyświetlenie aforyzmu na dzisiejszy dzień
                aforyzm_na_dzisiaj = wybierz_aforyzm_na_dzien(aforyzmy, dzisiejsza_data)
                print(aforyzm_na_dzisiaj)  # Wyświetlenie aforyzmu
            elif wybor == 2:
                # Przesunięcie daty programu
                dzisiejsza_data = przesun_date_programu(dzisiejsza_data)
            elif wybor == 0:
                # Wyjście z programu
                print("Wybrano wyjście z programu!")
                break
            else:
                # Obsługa nieprawidłowej opcji
                print("Wybrano nieprawidłową, niedostępną opcję - wybierz jeszcze raz!")
        except ValueError:
            # Obsługa błędu w przypadku podania wartości niecałkowitej
            print("Podano wartość niecałkowitą - wybierz jeszcze raz!")

if __name__ == '__main__':
    main()
