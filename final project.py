import tkinter as tk
from tkinter import ttk

# Conversion factors
conversion_factors = {
    ("Kilograms", "Pounds"): 2.20462,
    ("Pounds", "Kilograms"): 1 / 2.20462,
    ("Meters", "Inches"): 39.3701,
    ("Inches", "Meters"): 1 / 39.3701,
    ("Liters", "Cups"): 4.22675,
    ("Cups", "Liters"): 1 / 4.22675
}

units = ["Kilograms", "Pounds", "Meters", "Inches", "Liters", "Cups"]

# Main converter function
def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result.set(f"{value} {to_unit}")
        else:
            key = (from_unit, to_unit)
            factor = conversion_factors.get(key)
            if factor:
                converted = value * factor
                result.set(f"{converted:.2f} {to_unit}")
            else:
                result.set("Conversion not supported")
    except ValueError:
        result.set("Please enter a valid number")

# Tkinter UI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("300x250")

label_title = tk.Label(root, text="Unit Converter", font=("Arial", 16))
label_title.pack(pady=10)

entry_value = tk.Entry(root, justify="center")
entry_value.pack(pady=5)

combo_from = ttk.Combobox(root, values=units, state="readonly")
combo_from.set("Select From")
combo_from.pack(pady=5)

combo_to = ttk.Combobox(root, values=units, state="readonly")
combo_to.set("Select To")
combo_to.pack(pady=5)

btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=10)

result = tk.StringVar()
label_result = tk.Label(root, textvariable=result, font=("Arial", 14))
label_result.pack(pady=10)

root.mainloop()
