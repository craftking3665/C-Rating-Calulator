import tkinter as tk
from tkinter import messagebox

def calculate_c_rate():
    try:
        capacity_mah = float(entry_capacity.get())
        current_a = float(entry_current.get())
        capacity_ah = capacity_mah / 1000  # Convert mAh to Ah
        c_rate = current_a / capacity_ah
        messagebox.showinfo("Result", f"The required C-rate is: {c_rate:.2f}C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")

# Create main window
root = tk.Tk()
root.title("C-Rate Calculator")

# Labels and input fields
label_capacity = tk.Label(root, text="Battery Capacity (mAh):")
label_capacity.pack(padx=10, pady=5)
entry_capacity = tk.Entry(root)
entry_capacity.pack(padx=10, pady=5)

label_current = tk.Label(root, text="ESC Maximum Current (A):")
label_current.pack(padx=10, pady=5)
entry_current = tk.Entry(root)
entry_current.pack(padx=10, pady=5)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_c_rate)
button_calculate.pack(pady=20)

# Start main loop
root.mainloop()