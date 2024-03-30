from tkinter import *
from tkinter import messagebox
import requests
import json
import zxcvbn
import pickle
import os
import sys

def usrnme_gen():
    api_url1 = 'https://api.api-ninjas.com/v1/randomuser'
    response1 = requests.get(api_url1, headers={'X-Api-Key': 'A8HZvJ/ZDH2k0K1C1FmVDg==19nu4ZxYz9hgOtvk'})
    if response1.status_code == requests.codes.ok:
        data1 = json.loads(response1.text)
        random_usrnme = data1.get('username', '')
        usrnme_gen_entry.delete(0, END)
        usrnme_gen_entry.insert(0, random_usrnme)
    else:
        usrnme_gen_entry.delete(0, END)
        usrnme_gen_entry.insert(0, "Failed to generate username.")

def usrnme_clear():
    usrnme_gen_entry.delete(0, END)

def mode_dark():
    with open ('config.txt', 'w') as file:
        file.write('1')
    messagebox.showinfo("Restart", "Restart the prgram for the changes to take effect.")
    quit()

def mode_light():
    with open ('config.txt', 'w') as file:
        file.write('2')
    messagebox.showinfo("Restart", "Restart the prgram for the changes to take effect.")
    quit()

def estr_init(event):
    if pwd_gen.get() == 'The Sunday After The First Full Moon Following The Vernal Equinox':
        with open ('config.txt', 'w') as file:
            file.write('3')
        messagebox.showinfo("You Found The Secret !", "Restart the program to see the secret theme !")
        quit()
    else:
        pass

def mode_grab():
    try:
        with open ('config.txt', 'r') as file:
            mode_val=file.read().strip()
            try:
                val_cnv = int(mode_val)
                return val_cnv
            except ValueError:
                return 1
    except FileNotFoundError:
        return 1

def app_mode():
    if mode_state==1:
        win.configure(background='black')
        title.configure(fg='white', bg='black')
        pwd_gen_text.configure(fg='white', bg='black')
        pwd_gen_btn.configure(fg='black', bg='white')
        pwd_gen_clear.configure(fg='black', bg='white')
        pwd_check_text.configure(fg='white', bg='black')
        pwd_check_btn.configure(fg='black', bg='white')
        creds_txt.configure(fg='white', bg='black')
        dropdown_menu.configure(fg='white', bg='black')
        pwd_show_btn.configure(fg='black', bg='white')
        pwd_hide_btn.configure(fg='black', bg='white')
        new_pwd_text.configure(fg='white', bg='black')
        add_cred_btn.configure(fg='black', bg='white')
        delete_cred_btn.configure(fg='black', bg='white')
        dark_mode_btn.configure(fg='black', bg='white')
        light_mode_btn.configure(fg='black', bg='white')
        usrnme_gen_txt.configure(fg='white', bg='black')
        usrnme_gen_btn.configure(fg='black', bg='white')
        usrnme_clear_btn.configure(fg='black', bg='white')
        app_mode_txt.configure(fg='white', bg='black')
        pwd_gen_l_12.configure(fg='black', bg='white')
        pwd_gen_l_16.configure(fg='black', bg='white')
    elif mode_state == 2:
        win.configure(background='white')
        title.configure(fg='black', bg='white')
        pwd_gen_text.configure(fg='black', bg='white')
        pwd_gen_btn.configure(fg='white', bg='black')
        pwd_gen_clear.configure(fg='white', bg='black')
        pwd_check_text.configure(fg='black', bg='white')
        pwd_check_btn.configure(fg='white', bg='black')
        creds_txt.configure(fg='black', bg='white')
        dropdown_menu.configure(fg='black', bg='white')
        pwd_show_btn.configure(fg='white', bg='black')
        pwd_hide_btn.configure(fg='white', bg='black')
        new_pwd_text.configure(fg='black', bg='white')
        add_cred_btn.configure(fg='white', bg='black')
        delete_cred_btn.configure(fg='white', bg='black')
        dark_mode_btn.configure(fg='white', bg='black')
        light_mode_btn.configure(fg='white', bg='black')
        usrnme_gen_txt.configure(fg='black', bg='white')
        usrnme_gen_btn.configure(fg='white', bg='black')
        usrnme_clear_btn.configure(fg='white', bg='black')
        app_mode_txt.configure(fg='black', bg='white')
        pwd_gen_l_12.configure(fg='white', bg='black')
        pwd_gen_l_16.configure(fg='white', bg='black')
    elif mode_state == 3:
        win.configure(background='grey')
        title.configure(fg='black', bg='grey')
        pwd_gen_text.configure(fg='black', bg='grey')
        pwd_gen_btn.configure(fg='white', bg='black')
        pwd_gen_clear.configure(fg='white', bg='black')
        pwd_check_text.configure(fg='black', bg='grey')
        pwd_check_btn.configure(fg='white', bg='black')
        creds_txt.configure(fg='black', bg='grey')
        dropdown_menu.configure(fg='black', bg='white')
        pwd_show_btn.configure(fg='white', bg='black')
        pwd_hide_btn.configure(fg='white', bg='black')
        new_pwd_text.configure(fg='black', bg='grey')
        add_cred_btn.configure(fg='white', bg='black')
        delete_cred_btn.configure(fg='white', bg='black')
        dark_mode_btn.configure(fg='white', bg='black')
        light_mode_btn.configure(fg='white', bg='black')
        usrnme_gen_txt.configure(fg='black', bg='grey')
        usrnme_gen_btn.configure(fg='white', bg='black')
        usrnme_clear_btn.configure(fg='white', bg='black')
        app_mode_txt.configure(fg='black', bg='grey')
        pwd_gen_l_12.configure(fg='white', bg='black')
        pwd_gen_l_16.configure(fg='white', bg='black')
        def sprg_mode():
            with open ('config.txt', 'w') as file:
                file.write('4')
            messagebox.showinfo("Restart", "Restart the program to see the changes.")
            quit()
        estr_thm=Button(win, text="Spring Mode", fg='white', bg='black', command=sprg_mode)
        estr_thm.place(x=660, y=460)
    elif mode_state == 4:
        win.configure(background='light blue')
        title.configure(fg='purple', bg='light blue')
        pwd_gen_text.configure(fg='purple', bg='light blue')
        pwd_gen_btn.configure(fg='black', bg='orange')
        pwd_gen_clear.configure(fg='black', bg='orange')
        pwd_check_text.configure(fg='purple', bg='light blue')
        pwd_check_btn.configure(fg='black', bg='orange')
        creds_txt.configure(fg='purple', bg='light blue')
        dropdown_menu.configure(fg='black', bg='orange')
        pwd_show_btn.configure(fg='black', bg='orange')
        pwd_hide_btn.configure(fg='black', bg='orange')
        new_pwd_text.configure(fg='purple', bg='light blue')
        add_cred_btn.configure(fg='black', bg='orange')
        delete_cred_btn.configure(fg='black', bg='orange')
        dark_mode_btn.configure(fg='black', bg='orange')
        light_mode_btn.configure(fg='black', bg='orange')
        usrnme_gen_txt.configure(fg='purple', bg='light blue')
        usrnme_gen_btn.configure(fg='black', bg='orange')
        usrnme_clear_btn.configure(fg='black', bg='orange')
        app_mode_txt.configure(fg='purple', bg='light blue')
        pwd_gen_l_12.configure(fg='black', bg='orange')
        pwd_gen_l_16.configure(fg='black', bg='orange')
    else:
        win.configure(background='black')
        title.configure(fg='white', bg='black')
        pwd_gen_text.configure(fg='white', bg='black')
        pwd_gen_btn.configure(fg='black', bg='white')
        pwd_gen_clear.configure(fg='black', bg='white')
        pwd_check_text.configure(fg='white', bg='black')
        pwd_check_btn.configure(fg='black', bg='white')
        creds_txt.configure(fg='white', bg='black')
        dropdown_menu.configure(fg='white', bg='black')
        pwd_show_btn.configure(fg='black', bg='white')
        pwd_hide_btn.configure(fg='black', bg='white')
        new_pwd_text.configure(fg='white', bg='black')
        add_cred_btn.configure(fg='black', bg='white')
        delete_cred_btn.configure(fg='black', bg='white')
        dark_mode_btn.configure(fg='black', bg='white')
        light_mode_btn.configure(fg='black', bg='white')
        usrnme_gen_txt.configure(fg='white', bg='black')
        usrnme_gen_btn.configure(fg='black', bg='white')
        usrnme_clear_btn.configure(fg='black', bg='white')
        app_mode_txt.configure(fg='white', bg='black')
        pwd_gen_l_12.configure(fg='black', bg='white')
        pwd_gen_l_16.configure(fg='black', bg='white')

def internet_check():
    try:
        check = requests.get("https://www.example.com", timeout = 5)
        if check.status_code == 200:
            pass
        else:
            messagebox.showwarning("Internet Connection", "You're not connected to the internet. Some features will not work.")

    except requests.ConnectionError:
        messagebox.showerror("Internet Connection", "Failed to connect to the internet. Restart the program to try again. Without internet some features won't work.")

def delete_cred():
    selected_option = dropdown_var.get()
    if selected_option:
        del pwd_pwd[selected_option]
        pwd_options.remove(selected_option)
        dropdown_var.set("")
        pwd_entry.delete(0, END)
        save_credentials()
        update_dropdown()
    else:
        messagebox.showerror("Error", "Please select a credential to delete.")

def add_cred():
    new_cred = new_cred_entry.get()
    new_cred1 = new_cred_entry1.get()
    if new_cred and new_cred1:
        pwd_options.append(new_cred)
        pwd_pwd[new_cred] = new_cred1
        save_credentials()
        update_dropdown()
        new_cred_entry.delete(0, END)
        new_cred_entry1.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter both option and content.")

def save_credentials():
    try:
        with open("credentials.pkl", "wb") as f:
            pickle.dump(pwd_pwd, f)
    except Exception as e:
        print("Error saving credentials:", e)

def load_credentials():
    try:
        with open("credentials.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
    except EOFError:
        return {}
    except Exception as e:
        print("Error loading credentials:", e)
        return {}

def update_dropdown():
    dropdown_menu['menu'].delete(0, 'end')
    for option in pwd_options:
        dropdown_menu['menu'].add_command(label=option, command=lambda value=option: dropdown_var.set(value))

def pwd_hide():
    pwd_entry.delete(0, END)

def pwd_show():
    selected_option = dropdown_var.get()
    if selected_option in pwd_pwd:
        pwd_entry.delete(0, END)
        pwd_entry.insert(0, pwd_pwd[selected_option])
    else:
        messagebox.showerror("Error", "No password found for the selected credential.")

def pwd_check_clicked():
    password=pwd_check.get()
    if password == "":
        pwd_check_result_text.set("Please enter the password.")
    else:
        def get_password_strength(password):
            result = zxcvbn.zxcvbn(password)
            return result['score']
        strength_score = get_password_strength(password)
        if strength_score == 4:
            pwd_check_result_text.set(f"Strength : Strong | Score : {strength_score}/4")
        elif strength_score == 3 :
            pwd_check_result_text.set(f"Strength : Moderate | Score : {strength_score}/4")
        elif strength_score == 2 :
            pwd_check_result_text.set(f"Strength : Ok | Score : {strength_score}/4")
        elif strength_score == 1 :
            pwd_check_result_text.set(f"Strength : Low | Score : {strength_score}/4")
        elif strength_score == 0 :
            pwd_check_result_text.set(f"Strength : Very Low | Score : {strength_score}/4")
        else:
            pwd_check_result_text.set("Unable to obtain score.")

length = 12

def l_12():
    global length
    length = 12
    btn_12 = 12
    temp_var = length
    length = btn_12

def l_16():
    global length
    length = 12
    btn_16 = 16
    temp_var_2 = length
    length = btn_16

def pwd_gen_clicked():
    global length
    api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
    response = requests.get(api_url, headers={'X-Api-Key': 'A8HZvJ/ZDH2k0K1C1FmVDg==19nu4ZxYz9hgOtvk'})
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        random_password = data.get('random_password', '')
        pwd_gen.delete(0, END)
        pwd_gen.insert(0, random_password)
    else:
        pwd_gen.delete(0, END)
        pwd_gen.insert(0, "Failed to generate password. Try Again")

def pwd_gen_clear():
    pwd_gen.delete(0, END)

win = Tk()
win.title("AI Password Manager")
win.geometry('830x570')
win.resizable(False, False)
win.configure(background='black')

script_dir = os.path.dirname(sys.argv[0])
icon_path = os.path.join(script_dir, 'apm.png')
icon = PhotoImage(file=icon_path)
win.iconphoto(False, icon)

mode_change_init = 1

mode_state = mode_grab()

internet_check()

title = Label(win, text="AI Password Manager", font=('Arial', 16), fg='white', bg='black')
title.place(x=50, y=40)

pwd_gen_text=Label(win, text="Password Generator :", font=('Arial', 15), fg='white', bg='black')
pwd_gen_text.place(x=50, y=100)

pwd_gen=Entry(win, width=40)
pwd_gen.place(x=50, y=150)
pwd_gen.insert(0, "Default Password Length is 12.")

pwd_gen_l_12 = Button(win, text="12", fg='black', bg='white', command=l_12)
pwd_gen_l_12.place(x=220, y=180)

pwd_gen_l_16 = Button(win, text="16", fg='black', bg='white', command=l_16)
pwd_gen_l_16.place(x=245, y=180)

pwd_gen_btn=Button(win, text="Generate Password", fg='black', bg='white', command=pwd_gen_clicked)
pwd_gen_btn.place(x=50, y=180)

pwd_gen_clear=Button(win, text="Clear", fg='black', bg='white', command=pwd_gen_clear)
pwd_gen_clear.place(x=163, y=180)

pwd_check_text=Label(win, text="Password Strength Checker :", font=('Arial', 15), fg='white', bg='black')
pwd_check_text.place(x=50, y=240)

pwd_check=Entry(win, width=40)
pwd_check.place(x=50, y=285)

pwd_check_result_text = StringVar(win)
pwd_check_result=Entry(win, width=35, state='readonly', textvariable=pwd_check_result_text)
pwd_check_result_text.set("Result will appear here.")
pwd_check_result.place(x=50, y=310)

pwd_check_btn=Button(win, text="Check Password", fg='black', bg='white', command=pwd_check_clicked)
pwd_check_btn.place(x=50, y=340)

pwd_pwd = load_credentials()
pwd_options = list(pwd_pwd.keys())
dropdown_var = StringVar(win)
dropdown_var.set("")

creds_txt=Label(win, text="Your Credentials :", fg='white', bg='black', font=('Arial', 12))
creds_txt.place(x=460, y=120)

dropdown_menu = OptionMenu(win, dropdown_var, "")
dropdown_menu.configure(fg='white', bg='black', width=40)
dropdown_menu.place(x=460, y=150)

pwd_entry=Entry(win, width=47)
pwd_entry.place(x=460, y=190)

pwd_show_btn=Button(win, text="Show Password", fg='black', bg='white', command=pwd_show)
pwd_show_btn.place(x=460, y=215)

pwd_hide_btn=Button(win, text="Hide Password", fg='black', bg='white', command=pwd_hide)
pwd_hide_btn.place(x=555, y=215)

pwd_gen.bind('<Return>', estr_init)

new_pwd_text=Label(win, text="Add Credentials :", font=('Arial', 12), fg='white', bg='black')
new_pwd_text.place(x=460, y=250)

new_cred_entry=Entry(win, width = 47)
new_cred_entry.insert(0, "Enter Your Account ID/Name/Username")
new_cred_entry.place(x=460, y=280)

new_cred_entry1=Entry(win, width = 47)
new_cred_entry1.insert(0, "Enter Your Password")
new_cred_entry1.place(x=460, y=305)

add_cred_btn=Button(win, text="Add Credentials", fg='black', bg='white', command=add_cred)
add_cred_btn.place(x=460, y=330)

delete_cred_btn = Button(win, text="Delete Credential", fg='black', bg='white', command=delete_cred)
delete_cred_btn.place(x=646, y=215)

app_mode_txt=Label(win, text="App Mode :", font=('Arial', 12), fg='white', bg='black')
app_mode_txt.place(x=460, y=400)

dark_mode_btn=Button(win, text="Dark Mode", fg='black', bg='white', command=mode_dark)
dark_mode_btn.place(x=560, y=460)

light_mode_btn=Button(win, text="Light Mode", fg='black', bg='white', command=mode_light)
light_mode_btn.place(x=460, y=460)

usrnme_gen_txt=Label(win, text="Generate Username :", font=('Arials', 15), fg='white', bg='black')
usrnme_gen_txt.place(x=50, y=390)

usrnme_gen_entry=Entry(win, width=40)
usrnme_gen_entry.place(x=50, y=435)

usrnme_gen_btn=Button(win, text="Generate Username", fg='black', bg='white', command=usrnme_gen)
usrnme_gen_btn.place(x=50, y=465)

usrnme_clear_btn=Button(win, text="Clear", fg='black', bg='white', command=usrnme_clear)
usrnme_clear_btn.place(x=166, y=465)

app_mode()
update_dropdown()
win.mainloop()
