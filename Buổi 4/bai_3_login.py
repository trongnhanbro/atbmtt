from Cryptodome.Hash import MD5, SHA1, SHA256, SHA512
from tkinter import messagebox
from tkinter import *
import os
import csv
WIDTH_INPUT_BOX = 40
# Function to handle login
def login():
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

    # Check if database file exists
    current_directory = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(current_directory, "CSDL.csv")
    if not os.path.exists(db_file):
        error_label.config(text="Không tìm thấy tập tin dữ liệu.")
        return

    # Check login credentials
    with open(db_file, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username:
                hashed_password = row[1]  # Password hash is stored in the second column
                # Try each hashing method to see if the password matches
                for method in [MD5, SHA1, SHA256, SHA512]:
                    hashed_attempt = method.new(password.encode()).hexdigest()
                    if hashed_attempt == hashed_password:
                        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
                        return
                error_label.config(text="Tên đăng nhập hoặc mật khẩu không đúng.")
                return

    error_label.config(text="Tài khoản không tồn tại.")
window = Tk()
window.title("Demo Đăng Nhập")

user_name_label = Label(window, text="Tên đăng nhập", font=("Arial", 16))
user_name_label.grid(column=0, row=1)
user_name_input = Entry(window, width=WIDTH_INPUT_BOX)
user_name_input.grid(column=1, row=1)

password_label = Label(window, text="Mật khẩu", font=("Arial", 16))
password_label.grid(column=0, row=2)
password_input = Entry(window, width=WIDTH_INPUT_BOX, show="*")
password_input.grid(column=1, row=2)

# Error message label
error_label = Label(window, text="", fg="red")
error_label.grid(column=1, row=3)

# Set up event handler for button
button_register = Button(window, text="Đăng Nhập", command=login)
button_register.grid(column=1, row=4)

# Hiển thị cửa sổ
window.geometry("400x120")
window.mainloop()
