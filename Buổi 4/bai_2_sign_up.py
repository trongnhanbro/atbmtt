from Cryptodome.Hash import MD5, SHA1, SHA256, SHA512
import random
from tkinter import messagebox
from tkinter import *
import os
import csv

WIDTH_INPUT_BOX = 40
# Function to hash password with random method
def hash_password(password):
    methods = [MD5.new(), SHA1.new(), SHA256.new(), SHA512.new()]
    selected_method = random.choice(methods)

    selected_method.update(password.encode())
    hashed_password = selected_method.hexdigest()

    return hashed_password

# Function to handle account creation
def create_account():
    username = user_name_input.get()
    password = password_input.get()
    # Reset error messages
    error_label.config(text="")

    if not username:
        error_label.config(text="Vui lòng nhập tên đăng nhập.")
        return
    elif not password:
        error_label.config(text="Vui lòng nhập mật khẩu.")
        return
    
    # Check if database file exists, create if not
    current_directory = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(current_directory, "CSDL.csv")
    if not os.path.exists(db_file):
        with open(db_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Tên đăng nhập", "Mật khẩu"])
    # Check if username already exists
    with open(db_file, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username:
                error_label.config(text="Tên đăng nhập đã tồn tại.")
                return
    # Hash password with random method
    hashed_password = hash_password(password)
    # Add account to database
    with open(db_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])
    messagebox.showinfo("Thông báo", "Tạo tài khoản thành công!")


window = Tk()
window.title("Demo Tạo Tài Khoản")

user_name_label = Label(window, text="Tên đăng nhập", font=("Arial", 16))
user_name_label.grid(column=0, row=1)
user_name_input = Entry(window, width=WIDTH_INPUT_BOX)
user_name_input.grid(column=1, row=1)

password_label = Label(window, text="Mật khẩu", font=("Arial", 16))
password_label.grid(column=0, row=2)
password_input = Entry(window, width=WIDTH_INPUT_BOX)
password_input.grid(column=1, row=2)

# Error message label
error_label = Label(window, text="", fg="red")
error_label.grid(column=1, row=3)

# Set up event handler for button
button_register = Button(window, text="Tạo Tài Khoản", command=create_account)
button_register.grid(column=1, row=4)

# Hiển thị cửa sổ
window.geometry("400x120")
window.mainloop()
