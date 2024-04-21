#Ho và ten: Nguyễn Thanh Duy
#MSSV: B1913291
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64
def hashing():
	content = plaintxt.get().encode()
	func = hashmode.get()
	if func == 0:
		result = MD5.new(content)
	if func == 1:
		result = SHA1.new(content)
	if func == 2:
		result = SHA256.new(content)
	if func == 3:
		result = SHA512.new(content)
# Học viên tự cài đặt các phương thức cho SHA256 và SHA512
	rs = result.hexdigest().upper()
	hashvalue.delete(0,END)
	hashvalue.insert(INSERT,rs)

# -*- coding: utf8 -*-
# Tao giao dien chuong trinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="Chương Trình Băm", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
plainlb1 = Label(window, text="Văn bản", font=("Arial", 14))
plainlb1.grid(column=0, row=2)
plaintxt = Entry(window, width=65)
plaintxt.grid(column=1, row=2)
plainlb2 = Label(window, text="Giá trị Băm", font=("Arial", 14))
plainlb2.grid(column=0, row=8)
hashvalue = Entry(window, width=65)
hashvalue.grid(column=1, row=8)

radioGroup = LabelFrame(window, text = "Hàm băm")
radioGroup.grid(column=1, row=3)
hashmode = IntVar()
hashmode.set(-1)
md5_func = Radiobutton(radioGroup,text="Hash MD5",font=("Times New Roman", 11),variable=hashmode,value=0,command=hashing)
md5_func.grid(column=1,row=4)
sha1_func = Radiobutton(radioGroup,text="Hash SHA1",font=("Times New Roman", 11),variable=hashmode,value=1,command=hashing)
sha1_func.grid(column=1, row=5)
# Tương tự đối với sha256 và sha512
sha256_func =Radiobutton(radioGroup,text="Hash SHA256",font=("Times New Roman", 11),variable=hashmode,value=2,command=hashing)
sha256_func.grid(column=1, row=6)
sha512_func =Radiobutton(radioGroup,text="Hash SHA512",font=("Times New Roman", 11),variable=hashmode,value=3,command=hashing)
sha512_func.grid(column=1, row=7)
# Hien thi cua so
window.geometry('550x300')
window.mainloop()