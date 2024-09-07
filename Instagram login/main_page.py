from tkinter import *
from tkinter import messagebox
import time
import data_base as db


window = Tk()
window.title("Instagram")
window.geometry("900x600")
window.config(bg="white")

def open_sign_up():
    right_frm_in.grid_forget()
    right_frm_up.grid(column=1, row=0, pady=50, padx=50)

def open_sign_in():
    right_frm_up.grid_forget()
    right_frm_in.grid(column=1, row=0, pady=50, padx=50)

def set_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg="gray")
    entry.bind('<FocusIn>', lambda event: clear_placeholder(event, placeholder_text))
    entry.bind('<FocusOut>', lambda event: add_placeholder(event, placeholder_text))

def clear_placeholder(event, placeholder_text):
    entry: Entry = event.widget
    if entry.get() == placeholder_text:
        entry.delete(0, 'end')
        entry.config(fg="black")

def add_placeholder(event, placeholder_text):
    entry: Entry = event.widget
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg= "grey")

def sign_up():
    username = ent_username.get()
    password = ent_password.get()
    gender = gender_value.get()

    with open("data_base.py", 'r') as file:
        content = file.read()

    # Convert negative index to the corresponding positive index
    index = len(content) + -1
    
    # Insert the text at the specified index
    new_content = content[:index] + f" '{username}' : '{password}'," + content[index:]
    
    # Write the modified content back to the file
    with open("data_base.py", 'w') as file:
        file.write(new_content)
        file.close()

def login():
    username = in_ent_username.get().strip()
    password = in_ent_password.get().strip()
    if username in db.user_pass and db.user_pass[username] == password:
        messagebox.showinfo(title="logined succesfully", message="you are logining in.")
        window.after(3000, window.destroy)
    else:
        messagebox.showerror(title="wrong creditionals", message="your username or password is wrong")


# left frame for photos
left_frm = Frame(window)
left_frm.grid(column=0, row=0, padx=50, pady=10)

# Right frame for sign up
right_frm_up = Frame(window, relief="solid", borderwidth=1, bg="white")

# Right frame for sign in
right_frm_in = Frame(window, relief="solid", borderwidth=1, bg="white")
right_frm_in.grid(column=1, row=0, pady=50, padx=50)

# ------ Photos on the left side -------
photo = PhotoImage(file="1.png")
lbl_photo = Label(left_frm, image=photo, borderwidth=0)
lbl_photo.grid()

# ------------- sign in from ------------

# instagram logo
insta_logo = PhotoImage(file="insta_logo.png")
lbl_insta_logo = Label(right_frm_in, image=insta_logo, borderwidth=0)
lbl_insta_logo.grid(column=0, row=0, pady=(30, 20))

# User name entry
in_ent_username = Entry(right_frm_in, width=32)
in_ent_username.grid(column=0, row=1, padx=30, pady=30)
set_placeholder(in_ent_username, "Enter your username")

# password entry
in_ent_password = Entry(right_frm_in, width=32)
in_ent_password.grid(column=0, row=2, padx=30, pady=10)
set_placeholder(in_ent_password, "Enter your password")

# login button
btn_login = Button(right_frm_in, text="Login", command=login, bg="#3897f0", fg="white", width=25)
btn_login.grid(column=0, row=3, pady=10)

# seprator
lbl_seprte = Label(right_frm_in, text="------- OR -------", bg="white")
lbl_seprte.grid(column=0, row=4, pady=10)

# Add Facebook login option
fb_login_btn = Button(right_frm_in, text="Log in with Facebook", fg="#385185", bg="white", borderwidth=0)
fb_login_btn.grid(column=0, row=5, columnspan=2, pady=10)

# Add forgot password link
lbl_forgot = Label(right_frm_in, text="Forgot password?", fg="#385185", bg="white")
lbl_forgot.grid(column=0, row=6, columnspan=2, pady=(10, 30))

# Add a sign-up link
lbl_signup = Button(right_frm_in, text="Don't have an account? Sign up", fg="gray", bg="white", borderwidth=0, command=open_sign_up)
lbl_signup.grid(column=0, row=7, columnspan=2, pady=20)

# ------------- sign up from ------------

# instagram logo
lbl_insta_logo = Label(right_frm_up, image=insta_logo, borderwidth=0)
lbl_insta_logo.grid(column=0, row=0, pady=(30, 20))

# User name entry
ent_username = Entry(right_frm_up, width=32)
ent_username.grid(column=0, row=1, padx=30, pady=30)
set_placeholder(ent_username, "Enter your username")

# password entry
ent_password = Entry(right_frm_up, width=32)
ent_password.grid(column=0, row=2, padx=30, pady=10)
set_placeholder(ent_password, "Enter your password")

# radiobutton
gender_value = StringVar()
gender_value.set(" ")
frm_gender = Frame(right_frm_up, bg="white")
frm_gender.grid(column=0, row=3, pady=10)
Radiobutton(frm_gender, text="Male", variable=gender_value, value="male", bg="white").grid(column=0, row=0, padx=5)
Radiobutton(frm_gender, text="Female", variable=gender_value, value="female", bg="white").grid(column=1, row=0, padx=5)

# sign up button
btn_login = Button(right_frm_up, text="Sign up", command=sign_up, bg="#3897f0", fg="white", width=25)
btn_login.grid(column=0, row=4, pady=10)

# back to login page
lbl_signup = Button(right_frm_up, text="I already have account", fg="#3187A2", bg="white", borderwidth=0, command=open_sign_in)
lbl_signup.grid(column=0, row=5, columnspan=2, pady=20)

window.mainloop()
