import tkinter as tk
from tkinter import messagebox

def calculate_c_rate():
    try:
        capacity_mah = float(entry_capacity.get())
        current_a = float(entry_current.get())
        capacity_ah = capacity_mah / 1000  # Umwandlung von mAh in Ah
        c_rate = current_a / capacity_ah
        messagebox.showinfo("Ergebnis", f"Die benötigte C-Rate ist: {c_rate:.2f}C")
    except ValueError:
        messagebox.showerror("Ungültige Eingabe", "Bitte gib gültige Zahlenwerte ein.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("C-Rate Rechner")

# Labels und Eingabefelder
label_capacity = tk.Label(root, text="Akkukapazität (mAh):")
label_capacity.pack(padx=10, pady=5)
entry_capacity = tk.Entry(root)
entry_capacity.pack(padx=10, pady=5)

label_current = tk.Label(root, text="Maximalstrom des ESC (A):")
label_current.pack(padx=10, pady=5)
entry_current = tk.Entry(root)
entry_current.pack(padx=10, pady=5)

# Berechnen-Button
button_calculate = tk.Button(root, text="Berechnen", command=calculate_c_rate)
button_calculate.pack(pady=20)

# Hauptschleife starten
root.mainloop()