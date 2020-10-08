import tkinter as tk
from tkinter import StringVar, Label
import binary
import PySimpleGUI as sg

# If this shows up as blank on mac, switch to light mode :(
def getBinary():
    value = entry_one.get()
    base = entry_two.get()

    if not value:
        return
    if not base or int(base) < 2:
        base = 2

    label = tk.Label(root, text = f"Base {base} of {value} is: {binary.decimalToBase(value, int(base))}")
    window.create_window(250, 200, window=label)    

def getDecimal():
    value = binary_entry_one.get()
    base = binary_entry_two.get()
    if not value:
        return
    if not base or int(base) < 2:
        base = 2

    print(binary.bitToDecimal(value, int(base)))

    label = tk.Label(root, text = f"Decimal of {value} in base {base} os : {binary.bitToDecimal(value, int(base))}")
    window.create_window(250, 400, window=label)    

def getComplement():
    value = complement_entry_one.get()
    base = complement_entry_two.get()

    if not value:
        return
    if not base or int(base) < 2:
        base = 2

    label = tk.Label(root, text = f"Complement {base} of {value} is: {binary.complement(value, int(base))}")
    window.create_window(250, 550, window=label) 



root=tk.Tk()

window = tk.Canvas(root, width=500, height=1000)
window.pack()

# Binary Conversion from Decimal

label_one = tk.Label(root, text = "Decimal Number:")
window.create_window(10, 100, window=label_one)  

entry_one = tk.Entry(root) 
window.create_window(150, 100, window=entry_one)

label_two = tk.Label(root, text = "Base:")
window.create_window(260, 100, window=label_two)  

entry_two = tk.Entry(root) 
window.create_window(370, 100, window=entry_two)

button_one = tk.Button(root, text='Get the Binary conversion', command=getBinary)
button_one.config(fg="red")
window.create_window(250, 150, window=button_one)


# Decimal Conversion from Binary

binary_label_one = tk.Label(root, text = "Binary Number:")
window.create_window(10, 300, window=binary_label_one)  

binary_entry_one = tk.Entry(root) 
window.create_window(150, 300, window=binary_entry_one)

binary_label_two = tk.Label(root, text = "Base:")
window.create_window(260, 300, window=binary_label_two)  

binary_entry_two = tk.Entry(root) 
window.create_window(370, 300, window=binary_entry_two)

binary_button_one = tk.Button(root, text='Get the decimal conversion', command=getDecimal)
binary_button_one.config(fg="red")
window.create_window(250, 350, window=binary_button_one)


# Complement of Binary

complement_label_one = tk.Label(root, text = "Binary Number:")
window.create_window(10, 450, window=complement_label_one)  

complement_entry_one = tk.Entry(root) 
window.create_window(150, 450, window=complement_entry_one)

complement_label_two = tk.Label(root, text = "Base:")
window.create_window(260, 450, window=complement_label_two)  

complement_entry_two = tk.Entry(root) 
window.create_window(370, 450, window=complement_entry_two)

complement_button_one = tk.Button(root, text='Get the complement', command=getComplement)
complement_button_one.config(fg="red")
window.create_window(250, 500, window=complement_button_one)



exitButton = tk.Button(root, text="Quit", command=root.quit)  # Close Button
window.create_window(250, 750, window=exitButton)
root.mainloop()                                         # Starts the window