
import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from matplotlib import patches
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

app = customtkinter.CTk()
app.title('Bmi Calculator')
app.geometry('500x630')
app.resizable(width=False, height=False)
app.config(bg="#94BBF9")

font1 = ('Times New Roman', 22, 'bold')
font2 = ('Times New Roman', 27, 'bold')
font3 = ('Times New Roman', 18, 'bold')

# Database
conn = sqlite3.connect('data.db')
table_create = '''CREATE TABLE IF NOT EXISTS User_data(sr_no INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR, height FLOAT, lentype TEXT, weight FLOAT, scaletype TEXT, bmi_result FLOAT, healthstats TEXT)'''
conn.execute(table_create)

def calculate_bmi():
    try:
        username = name_entry.get()
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        lentype = var1.get()
        scaletype = var2.get()

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_data WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            error_message = f"Username '{username}' already exists with details:\n\n"
            error_message += f"Height: {existing_user[2]} {existing_user[3]}\n"
            error_message += f"Weight: {existing_user[4]} {existing_user[5]}\n"
            error_message += f"BMI: {existing_user[6]:.2f}\n"
            error_message += f"Health Status: {existing_user[7]}"
            messagebox.showerror("Error", error_message)
            return
            

        if lentype == 'ft':
            height *= 30.48
        if scaletype == 'lbs':
            weight *= 0.453592

        bmi = weight / ((height / 100) ** 2)
        health_status = determine_health(bmi)

        result_label.configure(text=f'Your BMI: {bmi:.2f}\nHealth Status: {health_status}')

        conn.execute("INSERT INTO User_data (username, height, lentype, weight, scaletype, bmi_result, healthstats) VALUES (?, ?, ?, ?, ?, ?, ?)", (username, height, lentype, weight, scaletype, bmi, health_status))
        conn.commit()



    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for height and weight.")
    

def determine_health(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9<= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
    #scatter plot
def create_scatter_plot():
    cursor=conn.cursor()
    cursor.execute(("SELECT sr_no, bmi_result FROM User_data"))
    data= cursor.fetchall()

    sr_values=[row[0] for row in data]
    bmi_values=[row[1] for row in data]

    colors = []
    for bmi in bmi_values:
        if bmi<18.5:
            colors.append('blue')
        elif 18.5<= bmi < 24.9:
            colors.append('green')
        elif 24.9 <= bmi < 29.9:
            colors.append('yellow')
        else:
            colors.append('red')
 

    plt.scatter(sr_values,bmi_values, c=colors)
    plt.xlabel('Number of Users')
    plt.ylabel('BMI')
    plt.title('BMI Scatter Plot')
    plt.grid(True)
    
    legend_elements=[
        mpatches.Patch(color='blue', label='Underweight'),
        mpatches.Patch(color='green', label='Normal'),
        mpatches.Patch(color='yellow', label='Overweight'),
        mpatches.Patch(color='red', label='Obese'),
        ]
    plt.legend(handles=legend_elements, loc='upper right', fontsize='small', handlelength=1.5) 

    plt.show()
    conn.commit()
    conn.close()


# Top
top = ImageTk.PhotoImage(Image.open("Images/head.png"))
top_img = customtkinter.CTkLabel(app, image=top, text='', bg_color='#94BBF9')
top_img.pack(side='top', fill='x')

# Name
name_label = customtkinter.CTkLabel(app, font=font2, text='Username:', bg_color='#94BBF9', text_color='#3946A5', width=100, corner_radius=10)
name_label.place(x=50, y=120)

name_entry = customtkinter.CTkEntry(app, font=font1, fg_color='#DFE3F1', text_color='#000', border_color='#94BBF9', corner_radius=10, bg_color='#94BBF9', width=200)
name_entry.place(x=200, y=120)

# Height
height_label = customtkinter.CTkLabel(app, font=font2, text='HEIGHT:', bg_color='#94BBF9', text_color='#3946A5', width=100, corner_radius=10)
height_label.place(x=50, y=190)

height_entry = customtkinter.CTkEntry(app, font=font1, fg_color='#DFE3F1', text_color='#000', border_color='#94BBF9', corner_radius=10, bg_color='#94BBF9', width=100)
height_entry.place(x=200, y=190)

# Weight
weight_label = customtkinter.CTkLabel(app, font=font2, text='WEIGHT:', bg_color='#94BBF9', text_color='#3946A5', width=100, corner_radius=10)
weight_label.place(x=50, y=260)

weight_entry = customtkinter.CTkEntry(app, font=font1, fg_color='#DFE3F1', text_color='#000', border_color='#94BBF9', corner_radius=10, bg_color='#94BBF9', width=100)
weight_entry.place(x=200, y=260)

weight_opt = ['kg', 'lbs']
height_opt = ['cm', 'ft']
var1 = StringVar()
var2 = StringVar()

height_opt = customtkinter.CTkComboBox(app, font=font3, text_color='#3946A5', fg_color='#DFE3F1', border_color='#DFE3F1', dropdown_fg_color='#DFE3F1', dropdown_text_color='#000', bg_color='#94BBF9', dropdown_hover_color='#5E93DF', button_color='#DFE3F1', button_hover_color='#5E93DF', corner_radius=10, values=height_opt, variable=var1, width=70)
height_opt.place(x=310, y=193)
height_opt.set('cm')

weight_opt = customtkinter.CTkComboBox(app, font=font3, text_color='#3946A5', fg_color='#DFE3F1', border_color='#DFE3F1', dropdown_fg_color='#DFE3F1', dropdown_text_color='#000', bg_color='#94BBF9', dropdown_hover_color='#5E93DF', button_color='#DFE3F1', button_hover_color='#5E93DF', corner_radius=10, values=weight_opt, variable=var2, width=70)
weight_opt.place(x=310, y=263)
weight_opt.set('kg')

calculate_button = customtkinter.CTkButton(app, command=calculate_bmi, font=font2, text_color='#fff', text='CALCULATE', fg_color='#3946A5', hover_color='#5E93DF', bg_color='#94BBF9', cursor='hand2', corner_radius=10, width=278, height=65.5)
calculate_button.place(x=110, y=340)

result_label = customtkinter.CTkLabel(app, font=font1, fg_color='#DFE3F1', text='', text_color='#3946A5', corner_radius=18, bg_color='#94BBF9', width=400, height=142)
result_label.place(x=50, y=420)

#visualize
scatter_plot=customtkinter.CTkButton(app, command=create_scatter_plot,font=font1, text_color='#fff', text='VISUALIZE', fg_color='#3946A5', hover_color='#5E93DF',border_color='#94BBF9', bg_color='#94BBF9', cursor='hand2', corner_radius=10, width=75,height=30)
scatter_plot.place(x=175,y=570)

app.mainloop()
