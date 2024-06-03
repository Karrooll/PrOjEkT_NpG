from playsound import playsound

# Funkcja odtwarzająca melodię z pliku
def odtworz_melodie():
    try:
        # Ścieżka do pliku z melodią
        playsound('Pliki_do_czytania/melody.mp3')
    except Exception as e:
        # Obsługa błędów podczas odtwarzania melodii
        print(f"Błąd podczas odtwarzania melodii: {e}")
