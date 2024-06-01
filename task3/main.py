import tkinter as tk
from tkinter import PhotoImage, messagebox
import string
import random
import tkinter

font1 = ('Fredoka', 18, 'bold')
font2 = ('Fredoka', 10, 'bold')

def generate_password():
    length = length_var.get()
    strength = strength_var.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid length (positive integer).")
        return

    length = int(length)

    if strength == "Poor":
        characters = string.ascii_lowercase
    elif strength == "Moderate":
        characters = string.ascii_letters + string.digits
    elif strength == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        messagebox.showerror("Invalid Strength", "Please select a valid password strength.")
        return

    password = ''.join(random.choice(characters) for i in range(length))
    result_var.set(password)
    print(password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

def update_menu_color(*args):
    strength = strength_var.get()
    if strength == "Poor":
        color = "#ae2012"
    elif strength == "Moderate":
        color = "#ca6702"
    elif strength == "Strong":
        color = "#40798c"
    else:
        color = "#82c0cc"
    strength_menu.config(bg=color, fg="#fff", activebackground=color, activeforeground="#fff")


root = tk.Tk()
root.title("Password Generator")
root.geometry("500x550")
image_path= PhotoImage(file="Images/password.jpg")
bg_image= tkinter.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)


length_var = tk.StringVar()
strength_var = tk.StringVar(value="Moderate")
strength_var.trace("w", update_menu_color) 
result_var = tk.StringVar()

# Widgets
length_entry = tk.Entry(root, justify='center', textvariable=length_var, font=font1, fg='#000',bg='#E1E2E2',border=0,width=17)
length_entry.place(x=140, y=162)


strength_options = ["Poor", "Moderate", "Strong"]

#  OptionMenu
strength_menu = tk.OptionMenu(root, strength_var, *strength_options)
strength_menu.config(font=font2,bg="#82c0cc", fg="#fff", activebackground="#489fb5", activeforeground="#fff", border=3)
strength_menu.place(x=370, y=218)


menu = strength_menu['menu']
menu.config(bg="#E1E2E2", fg="black", activebackground="#BFCED7", activeforeground="black")

butt=PhotoImage(file="Images/button.png")
generate_button = tk.Button(image=butt, cursor="hand2",bg='#B4B4BF',activebackground='#B4B4BF',border=0 ,command=generate_password)
generate_button.place(x=87, y=270)


result_entry = tk.Entry(root,justify='center',font=font1, textvariable=result_var, fg='#fff',bg='#60B95C',border=0,width=17)
result_entry.place(x=140, y=381.5)

copy_img=PhotoImage(file="Images/copy.png")
copy_button = tk.Button(image=copy_img, cursor="hand2",bg='#B4B4BF',activebackground='#B4B4BF',border=0,command=copy_to_clipboard)
copy_button.place(x=150, y=430)




root.mainloop()
