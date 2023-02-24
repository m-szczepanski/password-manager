from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for letter in range(randint(8, 10))]
    numbers_list = [choice(numbers) for number in range(randint(2, 4))]
    symbols_list = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)
    password = "".join(password_list)

    password_textbox.insert(0, f"{password}")
    pyperclip.copy(password)


def save():
    website = website_textbox.get()
    username = username_textbox.get()
    inserted_password = password_textbox.get()

    if len(website) == 0 or len(username) == 0 or len(inserted_password) == 0:
        messagebox.showerror(title="credentials error", message="Don't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Website: {website}\nEmail/Username: {username}\n"
                                                      f"Password: {inserted_password}\nAre you sure that everything is correct?")
        if is_ok:
            with open("./database/database.txt", "a") as data_file:
                data_file.write(f"{website}\t|\t{username}\t|\t{inserted_password}\n")
                website_textbox.delete(0, END)
                password_textbox.delete(0, END)


window = Tk()
window.title("PassManager")
logo = PhotoImage(file="./logo.png")
window.config(padx=50, pady=50, bg="#F5EAEA")
window.iconphoto(False, logo)
window.resizable(False, False)

canvas = Canvas(width=200, height=200, bg="#F5EAEA", highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:", bg="#F5EAEA", font=("Calibri", 12, "normal"))
website_label.grid(column=0, row=1)

username_label = Label()
username_label.config(text="Email/Username:", bg="#F5EAEA", font=("Calibri", 12, "normal"))
username_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:", bg="#F5EAEA", font=("Calibri", 12, "normal"))
password_label.grid(column=0, row=3)

website_textbox = Entry(width=35, bg="#F5EAEA")
website_textbox.grid(column=1, row=1, rowspan=1, columnspan=2)
website_textbox.focus()

username_textbox = Entry(width=35, bg="#F5EAEA")
username_textbox.grid(column=1, row=2, rowspan=1, columnspan=2)
username_textbox.insert(0, "test@test.pl")

password_textbox = Entry(width=21, bg="#F5EAEA")
password_textbox.grid(column=1, row=3)

generate = Button()
generate.config(text="Generate Password", bg="#F16767", highlightthickness=1, command=generate_password)
generate.grid(column=2, row=3)

add_button = Button()
add_button.config(text="Add", bg="#F16767", width=36, highlightthickness=1, command=save)
add_button.grid(column=1, row=4, rowspan=1, columnspan=2)

window.mainloop()
