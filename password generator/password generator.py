import tkinter as tk
from tkinter import ttk
import secrets
import string
import random

# Character sets
symbols = string.punctuation
upper_case_letters = string.ascii_uppercase
lower_case_letters = string.ascii_lowercase
numbers = string.digits

all_character = symbols + upper_case_letters + lower_case_letters + numbers

window = tk.Tk()
window.title('Password Generator')
window.iconbitmap(r'E:\Programming\Python\Python GUI\password generator\Apps password icon.ico')
window.configure(bg='#00F0FF')

width, height = 1200, 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
left = int(display_width / 2 - width / 2)
top = int(display_height / 2 - height / 2)
window.geometry(f'{width}x{height}+{left}+{top}')
window.resizable(False, False)

answer = tk.StringVar()

def generator_password():
    length = var.get()
    selected_characters = ""
    
    if var1.get():
        selected_characters += numbers
    if var2.get():
        selected_characters += upper_case_letters
    if var3.get():
        selected_characters += lower_case_letters
    if var4.get():
        selected_characters += symbols
        
    if not selected_characters:
        selected_characters = all_character

    password = [secrets.choice(selected_characters) for _ in range(length)]
    random.shuffle(password)
    final_output = ''.join(password)
    answer.set(final_output)

def button_press():
    password = answer.get()
    window.clipboard_append(password)
    window.update()
    button_copy.config(text='Copied')
    window.after(500, lambda: button_copy.config(text='Copy'))

label = tk.Label(
    text="Generate a Strong Password!",
    background='#00F0FF',
    font=('Arial', 35, 'bold'),
    justify='center'
)
label.pack(pady=15)

label = tk.Label(
    text="Create strong and secure passwords to keep your account safe online.",
    background='#00F0FF',
    foreground='black',
    font=('Arial', 15)
)
label.pack(pady=15)

output_label = tk.Label(
    textvariable=answer,
    background='#CBCBCB',
    foreground='black',
    font=('Arial', 15),
    width=45,
    height=2,
    borderwidth=3,
    relief="solid"
)
output_label.pack(pady=20)

button_copy = tk.Button(
    text='Copy',
    font=('Arial', 15, 'bold'),
    background='blue',
    foreground='white',
    width=6,
    height=1,
    borderwidth=5,
    relief="solid",
    command=button_press
)
button_copy.place(x=760, y=173)

button = tk.Button(
    text="Generate new",
    font=('Arial', 15, 'bold'),
    background='#D930FF',
    width=15,
    height=1,
    command=generator_password
)
button.pack()

customize_label = tk.Label(
    text="Customize your password",
    font=('Arial', 30),
    background='#00F0FF'
)
customize_label.pack(pady=35)

length_label = tk.Label(
    text='Password Length',
    background='#00F0FF',
    foreground='black',
    font=('Arial', 15, 'bold')
)
length_label.place(x=300, y=400)

var = tk.IntVar(value=15)

first_length_scale = tk.Radiobutton(
    text="10   Good",
    value=10,
    variable=var,
    font=('Arial', 15, 'bold'),
    background='#00F0FF',
    foreground='black'
)
first_length_scale.place(x=300, y=440)

second_length_scale = tk.Radiobutton(
    text="15   Strong",
    value=15,
    variable=var,
    font=('Arial', 15, 'bold'),
    background='#00F0FF',
    foreground='black'
)
second_length_scale.place(x=300, y=480)
second_length_scale.invoke()

third_length_scale = tk.Radiobutton(
    text="20   Very strong",
    value=20,
    variable=var,
    font=('Arial', 15, 'bold'),
    background='#00F0FF',
    foreground='black'
)
third_length_scale.place(x=300, y=520)

var1 = tk.BooleanVar()
number_cha = tk.Checkbutton(
    text="Numbers(0-9)",
    variable=var1,
    background='#00F0FF',
    foreground='black',
    font=('Arial', 15, 'bold')
)
number_cha.place(x=600, y=400)

var2 = tk.BooleanVar()
upper_letter_cha = tk.Checkbutton(
    text="Upper Case Letters(A-Z)",
    variable=var2,
    background='#00F0FF',
    foreground='black',
    font=('Arial', 15, 'bold')
)
upper_letter_cha.place(x=600, y=440)

var3 = tk.BooleanVar()
lower_letter_cha = tk.Checkbutton(
    text="Lower Case Letters(a-z)",
    variable=var3,
    background='#00F0FF',
    foreground='black',
    font=('Arial', 15, 'bold')
)
lower_letter_cha.place(x=600, y=480)

var4 = tk.BooleanVar()
symbols_cha = tk.Checkbutton(
    text="Symbols",
    variable=var4,
    background='#00F0FF',
    foreground='black',
    font=('Arial', 15, 'bold')
)
symbols_cha.place(x=600, y=520)

window.mainloop()
