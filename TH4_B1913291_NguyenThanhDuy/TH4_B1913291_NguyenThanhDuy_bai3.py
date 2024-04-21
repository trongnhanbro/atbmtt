# Ho va ten sinh vien: Nguyễn Thanh Duy
# Ma so sinh vien: B1913291

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
    f = open('CSDL.csv')
    reader = csv.reader(f)
    for i in reader:
        if user == i[0] and MD5.new(passw).hexdigest().upper() in i[1]:
            ale.config(text = "Đăng nhập thành công!")
            break
        elif user == i[0] and SHA1.new(passw).hexdigest().upper() in i[1]:
            ale.config(text = "Đăng nhập thành công!")
            break
        elif user == i[0] and SHA256.new(passw).hexdigest().upper() in i[1]:
            ale.config(text = "Đăng nhập thành công!")
            break
        elif user == i[0] and SHA512.new(passw).hexdigest().upper() in i[1]:
            ale.config(text = "Đăng nhập thành công!")
            break
        else:
            ale.config(text = "Sai tên đăng nhập hoặc mật khẩu!")


window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb1 = Label(window, text="Đăng nhập", font=("Arial Bold", 20))
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

resigter = Button(window, text="Đăng nhập", command=hashing)
resigter.grid(column=1, row=4)


window.geometry('400x170')
window.mainloop()
