# Ho va ten sinh vien: Nguyễn Thanh Duy
# Ma so sinh vien: B1913291
#STT: 33

# -*- coding: utf-8 -*-
from tkinter import *
import csv
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import hashlib
import base64
import random


def hashing():
    user = usr.get()
    passw = pw.get().encode()
    func = random.randint(0, 3)
    if func == 0:
        pw_result = MD5.new(passw)
    if func == 1:
        pw_result = SHA1.new(passw)
    if func == 2:
        pw_result = SHA256.new(passw)
    if func == 3:
        pw_result = SHA512.new(passw)

    rsp = pw_result.hexdigest().upper()
    valid = 1
    try:
        f = open('CSDL.csv')
        reader = csv.reader(f)
        for i in reader:
            if user == i[0]:
                valid = 0
            else:
                valid = 1
        if valid == 1:
            with open('CSDL.csv', 'a', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow([user, rsp])
                ale.config(text = "Tạo tài khoản thành công!")
        else:
            ale.config(text = "Tên tài khoản đã tồn tại!\nVui lòng chọn tên khác")
    except:
        with open('CSDL.csv', 'a', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([user, rsp])
            ale.config(text = "Tạo tài khoản thành công!")


window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb1 = Label(window, text="Tạo tài khoản", font=("Arial Bold", 20))
lb1.grid(column=1, row=0)

lb2 = Label(window, text="Tên đăng nhập", font=("Arial", 15))
lb2.grid(column=0, row=1)
usr = Entry(window, width=40)
usr.grid(column=1, row=1)

lb3 = Label(window, text="Mật khẩu", font=("Arial", 15))
lb3.grid(column=0, row=2)
pw = Entry(window, show="*", width=40)
pw.grid(column=1, row=2)

ale = Label(window, text="", font=("Arial", 10))
ale.grid(column=1, row=3)

resigter = Button(window, text="Tạo tài khoản", command=hashing)
resigter.grid(column=1, row=4)


window.geometry('400x170')
window.mainloop()
