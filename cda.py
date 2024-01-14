import tkinter as tk
import requests
from bs4 import BeautifulSoup
import re

class ProgramGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pobieranie Wideo CDA")
        
        self.label_url = tk.Label(master, text="Podaj link do strony CDA:")
        self.entry_url = tk.Entry(master, width=40)

        self.button_pobierz = tk.Button(master, text="Pobierz Wideo", command=self.pobierz_wideo)

        self.label_url.pack(pady=(10, 0), padx=10)
        self.entry_url.pack(pady=10, padx=10)
        self.button_pobierz.pack(pady=10)

    def pobierz_wideo(self):
        url = self.entry_url.get()

        try:
            linki_wideo_cda = self.pobierz_linki_wideo_cda(url)
            
            if linki_wideo_cda:
                print("Znalezione linki wideo na CDA:")
                for i, link in enumerate(linki_wideo_cda, start=1):
                    print(f"{i}. {link}")

                pobierz = input("Czy chcesz pobrać wideo? (tak/nie): ").lower()

                if pobierz == 'tak':
                    for i, link in enumerate(linki_wideo_cda, start=1):
                        self.pobierz_wideo_cda(link, i)
                    print("Wideo zostało pobrane.")
                else:
                    print("Koniec programu.")
            else:
                print("Nie znaleziono linków wideo na CDA.")
        except Exception as e:
            print(f"Błąd podczas pobierania wideo: {e}")

    def pobierz_linki_wideo_cda(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        linki_wideo = []

        # Przeszukaj tagi script
        for script_tag in soup.find_all('script'):
            script_content = script_tag.get_text()

            # Wykorzystaj wyrażenie regularne do odnalezienia linków wideo
            matches = re.findall(r'(https://[^"]+\.mp4)', script_content)

            # Dodaj znalezione linki do listy
            linki_wideo.extend(matches)

        return linki_wideo

    def pobierz_wideo_cda(self, link, numer):
        print(f"Pobieranie wideo {numer}...")
        response = requests.get(link)

        # Zapisz plik wideo na dysku
        nazwa_pliku = f"video_{numer}.mp4"
        with open(nazwa_pliku, 'wb') as file:
            file.write(response.content)

        print(f"Wideo {numer} zostało pobrane i zapisane jako {nazwa_pliku}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ProgramGUI(root)
    root.mainloop()
