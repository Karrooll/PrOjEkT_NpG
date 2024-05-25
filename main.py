from Odczyt import utworz_liste_aforyzmow
from Aforyzm import Aforyzm

def main():
    aforyzmy = utworz_liste_aforyzmow()
    wybor = 2
    while(wybor != -1):
        print("Aby wyśiwetlić aforyzm wciśnij 1")
        print("Aby wyjść z programu wciśnij 0")
        wybor = int(input("Podaj opcję: "))

        if wybor == 1:
            x=1



if __name__ == '__main__':
    main()