from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=45, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

numbers = []

def button_click(number):
    current_number = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current_number) + str(number))


def clear_action():
    entry.delete(0, END)


def add_action():
    numbers.append(entry.get())
    entry.delete(0, END)
    global action
    action = 'addition'


def subtract_action():
    numbers.append(entry.get())
    entry.delete(0, END)
    global action
    action = 'subtraction'


def multiply_action():
    numbers.append(entry.get())
    entry.delete(0, END)
    global action
    action = 'multiplication'


def divide_action():
    numbers.append(entry.get())
    entry.delete(0, END)
    global action
    action = 'division'


def equals_action():
    numbers.append(entry.get())
    entry.delete(0, END)
    print(action)
    if action == 'addition':
        entry.insert(0, int(numbers[-2]) + int(numbers[-1]))
    elif action == 'subtraction':
        entry.insert(0, int(numbers[-2]) - int(numbers[-1]))
    elif action == 'multiplication':
        entry.insert(0, int(numbers[-2]) * int(numbers[-1]))
    elif action == 'division':
        entry.insert(0, int(numbers[-2]) / int(numbers[-1]))


# Define Buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_dot = Button(root, text='.', padx=42, pady=20, command=lambda: button_click('.'))
button_comma = Button(root, text=',', padx=42, pady=20, command=lambda: button_click(','))


button_add = Button(root, text='+', padx=38, pady=20, command=add_action)
button_subtract = Button(root, text='-', padx=39, pady=20, command=subtract_action)
button_multiply = Button(root, text='*', padx=39, pady=20, command=multiply_action)
button_divide = Button(root, text='/', padx=39, pady=20, command=divide_action)

button_equals = Button(root, text='=', padx=91, pady=20, command=equals_action)
button_clear = Button(root, text='Clear', padx=81, pady=20, command=clear_action)


# Display the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_dot.grid(row=4, column=0)
button_comma.grid(row=4, column=2)


button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)


button_clear.grid(row=5, column=0, columnspan=2)
button_equals.grid(row=5, column=2, columnspan=2)

root.mainloop()