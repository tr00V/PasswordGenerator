from tkinter import *
from tkinter.ttk import Combobox, Checkbutton

from Password_class import Password

have_password = False


def _create_password():
    length_choice = int(combo.get())

    password = Password(length=length_choice,
                        letters_lower=chk_state_lower_latters.get(),
                        letters_upper=chk_state_upper_latters.get(),
                        numbers=chk_state_numbers.get(),
                        symbols=chk_state_symbols.get())

    passwords = password.check_passwords()

    return passwords


def clicked():
    global have_password

    if have_password:
        for widget in frame.winfo_children():
            widget.destroy()

    passwords = _create_password()

    count = 1
    for k, v in passwords.items():
        if v[0]:
            Label(frame, text=f"{k}", font=("Arial Bold", 10)).pack()
        else:
            Label(frame, text=f"{k}: {v[1]}", font=("Arial Bold", 10), foreground="red").pack()
        count += 1

    frame.grid()
    have_password = True


window = Tk()
window.title("Password Generator")
window.geometry('500x380')

lbl = Label(window, text="Hello! This is a password generator", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

frame = Frame()

combo_text = Label(window, text="Choice length", font=("Arial Bold", 10))
combo_text.grid(column=0, row=1)
combo = Combobox(window)
combo['values'] = (5, 8, 10, 12, 14, 22)
combo.current(3)
combo.grid(column=1, row=1)

chk_state_numbers = BooleanVar()
chk_state_numbers.set(True)
chk_1 = Checkbutton(window, text='Numbers 0-9', var=chk_state_numbers)
chk_1.grid(column=0, row=2)

chk_state_lower_latters = BooleanVar()
chk_state_lower_latters.set(True)
chk_2 = Checkbutton(window, text='Lower latters a-z', var=chk_state_lower_latters)
chk_2.grid(column=1, row=2)

chk_state_upper_latters = BooleanVar()
chk_state_upper_latters.set(True)
chk_3 = Checkbutton(window, text='Upper latters A-Z', var=chk_state_upper_latters)
chk_3.grid(column=0, row=3)

chk_state_symbols = BooleanVar()
chk_state_symbols.set(True)
chk_4 = Checkbutton(window, text='Symbols', var=chk_state_symbols)
chk_4.grid(column=1, row=3)

btn = Button(window, text="Generate", command=clicked, width=20, height=2, bg="blue", fg="black")
btn.grid(column=0, row=4)

window.mainloop()
