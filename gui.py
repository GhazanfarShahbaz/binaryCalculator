import tkinter as tk
import binary
import PySimpleGUI as sg

# If this shows up as blank on mac, switch to light mode :(
def clearLabel(label):
    label.destroy()

def getBinary():
    value = entry_one.get()
    base = entry_two.get()

    if not value:
        return
    if not base or int(base) < 2:
        base = 2
    answer_one.set(f"Base {base} of {value} is: {binary.format(binary.decimalToBase(value, int(base)))}")
    root.update()

def getDecimal():
    value = binary_entry_one.get()
    base = binary_entry_two.get()

    if not value:
        return
    elif not base or int(base) < 2:
        base = 2
    elif not binary.validityCheck(value, int(base)):
        answer_two.set(f"Base {base} is not valid for the following binary number, {value}")
        root.update()
        return

    answer_two.set(f"Decimal of {value} in base {base} os : {binary.bitToDecimal(value, int(base))}")
    root.update()

def getComplement():
    value = complement_entry_one.get()
    base = complement_entry_two.get()

    if not value:
        return
    elif not base or int(base) < 2:
        base = 2
    elif not binary.validityCheck(value, int(base)):
        answer_three.set(f"Base {base} is not valid for the following binary number, {value}")
        root.update()
        return

    answer_three.set(f"Complement {base} of {binary.format(value)} is: {binary.format(binary.complement(value, int(base)))}")
    root.update()

def binaryOperations():
    operation = option.get()
    valueOne = operation_entry_one.get()
    valueTwo = operation_entry_three.get()
    baseOne = operation_entry_two.get()
    baseTwo= operation_entry_four.get()

    if not baseOne or int(baseOne) < 2:
        baseOne = 2
    else:
        baseOne = int(baseOne)
    if not baseTwo or int(baseTwo) < 2:
        baseTwo = 2
    else:
        baseTwo = int(baseTwo)
    
    if not binary.validityCheck(valueOne, int(baseOne)):
        answer_four.set(f"Base {baseOne} is not valid for the following binary number, {valueOne}")
        root.update()
        return
    if not binary.validityCheck(valueTwo, int(baseTwo)):
        answer_four.set(f"Base {baseTwo} is not valid for the following binary number, {valueTwo}")
        root.update()
        return
    
    answer_four.set(f"{valueOne}{operation}{valueTwo} is: {binary.format(binary.operation_gate(valueOne, valueTwo, operation, baseOne, baseTwo))} in base {baseOne}")
    root.update()
    




root=tk.Tk()

window = tk.Canvas(root, width=500, height=1000)
window.pack()

# Binary Conversion from Decimal
title_one = tk.Label(root, text = "Decimal To Binary")
window.create_window(250, 50, window=title_one)  

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

answer_one = tk.StringVar()
answer_one.set(" ")
output_one = tk.Label(root, textvariable=answer_one)
window.create_window(250, 200, window=output_one)



# Decimal Conversion from Binary
title_two = tk.Label(root, text = "Binary To Decimal")
window.create_window(250, 250, window=title_two) 

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


answer_two = tk.StringVar()
answer_two.set(" ")
output_two = tk.Label(root, textvariable=answer_two)
window.create_window(250, 400, window=output_two)


# Complement of Binary
title_three = tk.Label(root, text = "Complement of a Binary Number")
window.create_window(250, 450, window=title_three) 

complement_label_one = tk.Label(root, text = "Binary Number:")
window.create_window(10, 500, window=complement_label_one)  

complement_entry_one = tk.Entry(root) 
window.create_window(150, 500, window=complement_entry_one)

complement_label_two = tk.Label(root, text = "Base:")
window.create_window(260, 500, window=complement_label_two)  

complement_entry_two = tk.Entry(root) 
window.create_window(370, 500, window=complement_entry_two)

complement_button_one = tk.Button(root, text='Get the complement', command=getComplement)
complement_button_one.config(fg="red")
window.create_window(250, 550, window=complement_button_one)

answer_three = tk.StringVar()
answer_three.set(" ")
output_three = tk.Label(root, textvariable=answer_three)
window.create_window(250, 600, window=output_three) 

# Operations
operations = ["+", "-", "*"]
option = tk.StringVar(root)
option.set(operations[0])

title_Four = tk.Label(root, text = "Operations with Binary numbers")
window.create_window(250, 650, window=title_Four) 

operation_label_one = tk.Label(root, text = "Binary Number One:")
window.create_window(0, 700, window=operation_label_one)  

operation_entry_one = tk.Entry(root) 
window.create_window(150, 700, window=operation_entry_one)

operation_label_two = tk.Label(root, text = "Base One:")
window.create_window(270, 700, window=operation_label_two)  

operation_entry_two = tk.Entry(root) 
window.create_window(387, 700, window=operation_entry_two)


operation_label_three = tk.Label(root, text = "Binary Number Two:")
window.create_window(0, 750, window=operation_label_three)  

operation_entry_three = tk.Entry(root) 
window.create_window(150, 750, window=operation_entry_three)

operation_label_four = tk.Label(root, text = "Base Two:")
window.create_window(270, 750, window=operation_label_four)  

operation_entry_four = tk.Entry(root) 
window.create_window(387, 750, window=operation_entry_four)

menu = tk.OptionMenu(root, option, *operations)
menu.pack() 
window.create_window(250, 800, window=menu)

operation_button_one = tk.Button(root, text='Get answer', command=binaryOperations)
complement_button_one.config(fg="red")
window.create_window(250, 850, window=operation_button_one)

answer_four = tk.StringVar()
answer_four.set(" ")
output_four = tk.Label(root, textvariable=answer_four)
window.create_window(250, 900, window=output_four)



exitButton = tk.Button(root, text="Quit", command=root.quit)  # Close Button
window.create_window(250, 950, window=exitButton)
root.mainloop()                                         # Starts the window