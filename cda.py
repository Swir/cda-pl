import tkinter as tk
from tkinter import messagebox
import subprocess

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

        if not url:
            messagebox.showwarning("Błąd", "Proszę podać link do strony CDA.")
            return

        try:
            subprocess.run(["cda-dl", url], check=True)
            messagebox.showinfo("Sukces", "Wideo zostało pobrane.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Błąd", f"Błąd podczas pobierania wideo:\n{e}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Niespodziewany błąd:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ProgramGUI(root)
    root.mainloop()
