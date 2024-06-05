from Odczyt import utworz_liste_aforyzmow
from czas import wybierz_aforyzm_na_dzien, przesun_date_programu, zmiana_aforyzmu
import datetime
from muzyka import odtworz_melodie
from aforyzmy_uzyte import zapisz_uzyte_aforyzmy, sprawdz_czy_uzyty

def main():
    # Odtwarzanie melodii po uruchomieniu programu
    odtworz_melodie()
    # Utworzenie listy aforyzmów
    aforyzmy = utworz_liste_aforyzmow()
    #Użyte aforyzmy
    aforyzmy_uzyte = []
    # Ustawienie dzisiejszej daty
    dzisiejsza_data = datetime.date.today()
    # Odczytanie uzytych aforyzmow z poprzedniego dzialania programu
    sprawdz_czy_uzyty(aforyzmy, aforyzmy_uzyte)


    while True:
        # Wyświetlanie menu programu
        print('\n----------------AFORYZMY NA KAŻDY DZIEŃ----------------')
        print("Aby wyświetlić aforyzm na dzisiejszy dzień wciśnij 1")
        print("Aby przesunąć datę programu wciśnij 2")
        print("Aby wyjść z programu wciśnij 3")
        try:
            # Pobranie wyboru użytkownika
            wybor = int(input("Podaj opcję: "))
            print(wybor)
            if wybor == 1:
                # Wybranie i wyświetlenie aforyzmu na dzisiejszy dzień
                aforyzm_na_dzisiaj, aforyzmy = wybierz_aforyzm_na_dzien(aforyzmy, aforyzmy_uzyte, dzisiejsza_data)
                aforyzm_na_dzisiaj.wyswietl_aforyzm()
            elif wybor == 2:
                # Przesunięcie daty programu
                #Zapisanie uzytego aforyzmu i usuniecie z puli
                aforyzm_na_dzisiaj, aforyzmy = wybierz_aforyzm_na_dzien(aforyzmy, aforyzmy_uzyte, dzisiejsza_data)
                zmiana_aforyzmu(aforyzmy, aforyzmy_uzyte, aforyzm_na_dzisiaj)
                dzisiejsza_data = przesun_date_programu(dzisiejsza_data)
            elif wybor == 3:
                # Wyjście z programu
                #Rowniez zapisanie uzytegi aforyzmu i usuniecie z puli
                aforyzm_na_dzisiaj, aforyzmy = wybierz_aforyzm_na_dzien(aforyzmy, aforyzmy_uzyte, dzisiejsza_data)
                zmiana_aforyzmu(aforyzmy, aforyzmy_uzyte, aforyzm_na_dzisiaj)
                zapisz_uzyte_aforyzmy(aforyzmy_uzyte)
                print("Wybrano wyjście z programu!")
                break
            else:
                # Obsługa nieprawidłowej opcji
                print("Wybrano nieprawidłową, niedostępną opcję - wybierz jeszcze raz!")
        except ValueError :
                #Obsługa błędu w przypadku podania wartości niecałkowitej
                print("Podano wartość niecałkowitą - wybierz jeszcze raz!")

if __name__ == '__main__':
    main()
