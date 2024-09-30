import tkinter as tk
from tkinter import messagebox

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to perform the conversion
def convert_temperature():
    try:
        temp_value = float(entry_temp.get())
        unit = temp_unit.get()

        if unit == "Celsius":
            fahrenheit = celsius_to_fahrenheit(temp_value)
            kelvin = celsius_to_kelvin(temp_value)
            result.set(f"{temp_value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        elif unit == "Fahrenheit":
            celsius = fahrenheit_to_celsius(temp_value)
            kelvin = fahrenheit_to_kelvin(temp_value)
            result.set(f"{temp_value}°F is {celsius:.2f}°C and {kelvin:.2f}K.")
        elif unit == "Kelvin":
            celsius = kelvin_to_celsius(temp_value)
            fahrenheit = kelvin_to_fahrenheit(temp_value)
            result.set(f"{temp_value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F.")
        else:
            messagebox.showerror("Invalid Unit", "Please select a valid temperature unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Define the window size
root.geometry("400x200")

# Label for the temperature entry
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack(pady=10)

# Entry widget to get the temperature value
entry_temp = tk.Entry(root)
entry_temp.pack(pady=5)

# Option menu to select the unit of the temperature
temp_unit = tk.StringVar(value="Celsius")
unit_menu = tk.OptionMenu(root, temp_unit, "Celsius", "Fahrenheit", "Kelvin")
unit_menu.pack(pady=5)

# Button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

# Label to display the result
result = tk.StringVar()
label_result = tk.Label(root, textvariable=result, font=("Arial", 14))
label_result.pack(pady=10)

# Start the GUI event loop
root.mainloop()
