import tkinter as tk
from tkinter import messagebox
import subprocess
import threading

class VideoDownloader:
    def download_video(self, url, callback):
        try:
            download_thread = threading.Thread(target=self._download_video, args=(url, callback))
            download_thread.start()
            return True
        except Exception as e:
            messagebox.showerror("Błąd", f"Niespodziewany błąd:\n{e}")
            return False

    def _download_video(self, url, callback):
        try:
            subprocess.run(["cda-dl", url], check=True)
            if callback:
                callback()
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Błąd", f"Błąd podczas pobierania wideo:\n{e}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Niespodziewany błąd:\n{e}")

class ProgramGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pobieranie Wideo CDA")
        master.configure(bg="#f0f0f0")  # Ustawienie koloru tła
        master.geometry("500x200")  # Ustawienie rozmiaru okna

        self.label_url = tk.Label(master, text="Podaj link do strony CDA:", font=("Helvetica", 12), bg="#f0f0f0")
        self.entry_url = tk.Entry(master, width=40, font=("Helvetica", 10))

        self.button_pobierz = tk.Button(master, text="Pobierz Wideo", command=self.pobierz_wideo,
                                        font=("Helvetica", 12), bg="#4caf50", fg="white")  # Zielony przycisk

        self.label_url.pack(pady=(20, 0), padx=10)
        self.entry_url.pack(pady=10, padx=10)
        self.button_pobierz.pack(pady=10)

        self.video_downloader = VideoDownloader()

    def pobierz_wideo(self):
        url = self.entry_url.get()

        if not url:
            messagebox.showwarning("Błąd", "Proszę podać link do strony CDA.")
            return

        self.master.update_idletasks()  # Zaktualizuj widżety, aby natychmiast zobaczyć zmiany

        self.video_downloader.download_video(url, self.on_download_complete)

    def on_download_complete(self):
        self.master.after(0, lambda: messagebox.showinfo("Sukces", "Wideo zostało pobrane."))

if __name__ == "__main__":
    root = tk.Tk()
    gui = ProgramGUI(root)
    root.mainloop()
