import tkinter as tk
from PIL import Image, ImageTk
import random, string
from tkinter import messagebox

users = {}  # Dictionary to store user credentials

def open_signup():
    login_frame.pack_forget()
    signup_frame.pack()

def signup():
    username = username_signup_entry.get()
    password = password_signup_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not password or not confirm_password:
        messagebox.showerror("Signup", "All fields are required!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Signup", "Passwords do not match!")
        return
    
    if username in users:
        messagebox.showerror("Signup", "Username already exists!")
        return
    
    users[username] = password
    messagebox.showinfo("Signup", "Account created successfully! Please log in.")
    open_login()

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login successful!")
        open_password_generator()
    else:
        messagebox.showerror("Login", "Invalid credentials. Please try again.")

def open_login():
    signup_frame.pack_forget()
    password_generator_frame.pack_forget()
    login_frame.pack()

def open_password_generator():
    login_frame.pack_forget()
    password_generator_frame.pack()

def passgen():
    length = min(val.get(), len(poor))
    if choice.get() == 1:
        return "".join(random.sample(poor, length))
    elif choice.get() == 2:
        return "".join(random.sample(average, length))
    elif choice.get() == 3:
        return "".join(random.sample(advance, length))
    else:
        return "Select Strength"

def callback():
    lsum.config(text=passgen())

root = tk.Tk()
root.title("Login and Signup Page")
root.geometry("800x600")  # Adjusted for a larger window

# Load and resize background image to fit window
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((1600, 800))  # Resize to match window size
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

frame_bg = "#A7C7E7"  # Light blue shade
text_fg = "#333333"
btn_bg = "#5A9"
btn_fg = "white"

def create_label(frame, text):
    return tk.Label(frame, text=text, fg=text_fg, bg=frame_bg, font=("Arial", 12))

def create_entry(frame, show=None):
    return tk.Entry(frame, show=show, font=("Arial", 12))

def create_button(frame, text, command):
    return tk.Button(frame, text=text, command=command, bg=btn_bg, fg=btn_fg, font=("Arial", 12), padx=5, pady=2)

login_frame = tk.Frame(root, bg=frame_bg, padx=20, pady=20)
login_frame.pack()

create_label(login_frame, "Username:").pack()
username_entry = create_entry(login_frame)
username_entry.pack()

create_label(login_frame, "Password:").pack()
password_entry = create_entry(login_frame, show="*")
password_entry.pack()

create_button(login_frame, "Login", check_login).pack(pady=5)
create_button(login_frame, "Don't have an account? Sign up", open_signup).pack()

signup_frame = tk.Frame(root, bg=frame_bg, padx=20, pady=20)
create_label(signup_frame, "Signup Page").pack()

create_label(signup_frame, "Username:").pack()
username_signup_entry = create_entry(signup_frame)
username_signup_entry.pack()

create_label(signup_frame, "Password:").pack()
password_signup_entry = create_entry(signup_frame, show="*")
password_signup_entry.pack()

create_label(signup_frame, "Confirm Password:").pack()
confirm_password_entry = create_entry(signup_frame, show="*")
confirm_password_entry.pack()

create_button(signup_frame, "Sign Up", signup).pack(pady=5)
create_button(signup_frame, "Back to Login", open_login).pack()

password_generator_frame = tk.Frame(root, bg=frame_bg, padx=20, pady=20)
create_label(password_generator_frame, "CHOOSE AN OPTION").pack()

choice = tk.IntVar()
tk.Radiobutton(password_generator_frame, text="WEAK", variable=choice, value=1, bg=frame_bg).pack()
tk.Radiobutton(password_generator_frame, text="AVERAGE", variable=choice, value=2, bg=frame_bg).pack()
tk.Radiobutton(password_generator_frame, text="STRONG", variable=choice, value=3, bg=frame_bg).pack()

create_label(password_generator_frame, "Password length:").pack()
val = tk.IntVar()
val.set(8)
tk.Spinbox(password_generator_frame, from_=4, to_=24, textvariable=val, width=13).pack()

create_button(password_generator_frame, "Suggest Password", callback).pack(pady=20)

lsum = tk.Label(password_generator_frame, text="Password here", font=("Arial", 20), bg=frame_bg)
lsum.pack()

poor = string.ascii_letters
average = string.ascii_letters + string.digits
symbols = "~!@#$%^&*()_-+={}[]|:;\"'<>,.?/"
advance = poor + average + symbols

root.mainloop()
