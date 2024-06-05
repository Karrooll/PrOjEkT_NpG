# Ścieżka do pliku z użytymi aforyzmami
UZYTE_AFORYZMY_FILE = 'uzyte_aforyzmy.txt'

def sprawdz_czy_uzyty(aforyzmy, aforyzmy_uzyte):
    """Sprawdza, czy dany aforyzm był już użyty."""
    #Wczytanie uzywanych aforyzmow
    with open(UZYTE_AFORYZMY_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  #Usuwa białe znaki z początku i końca linii
            aforyzmy_uzyte.append(int(line))

    #Usuniecie uzywanych aforyzmow z listy do wysiwetlenia
    #Lista indeksow do usuniecia
    do_usuniecia = []
    for i in range(len(aforyzmy)):
        if aforyzmy[i].id in aforyzmy_uzyte:
            do_usuniecia.append(i)

    #Usuwanie konkretnych elementow
    dlg = len(aforyzmy)
    i=0
    while i < dlg:
        if aforyzmy[i].id in do_usuniecia:
            aforyzmy.pop(i)
            dlg -= 1
        else:
            i+=1

def zapisz_uzyte_aforyzmy(aforyzmy_uzyte):
    """Zapisuje dany aforyzm jako użyty."""
    with open(UZYTE_AFORYZMY_FILE, 'w+', encoding='utf-8') as file:
        #Zapis indeksow uzytych aforyzmow
        for uzyty in aforyzmy_uzyte:
            file.write(f'{uzyty}\n')