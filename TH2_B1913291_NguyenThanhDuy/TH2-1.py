#Ho va ten: Nguyen Thanh Duy
#MSSV: B1913291

from Crypto.Cipher import DES 
import base64

def pad(s):
    return s + (8-len(s)%8)*chr(8-len(s)%8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES():
    txt = pad(inputVanbangoc.get()).encode("utf8")
    key = pad(inputKhoa.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    inputVbmahoa.delete(0, END)
    inputVbmahoa.insert(INSERT, entxt)

def giaima_DES():
    txt = inputVbmahoa.get()
    txt = base64.b64decode(txt)
    key = pad(inputKhoa.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    inputVbgiaima.delete(0, END)
    inputVbgiaima.insert(INSERT, detxt)




from tkinter import *

window = Tk()
window.title("Welcome to Demo AT&BMTT")

lb0 = Label(window, text=" ", font=("Arial Bold",10))
lb0.grid(column=0, row=0)

lb1 = Label(window, text="Chuong Trinh Demo", font=("Arial Bold",20))
lb1.grid(column=1, row=1)

lb2 = Label(window, text="Mat ma doi xung DES", font=("Arial Bold",10))
lb2.grid(column=1, row=2)

vanbangoc = Label(window, text="Van ban goc",font=("Arial", 14))
vanbangoc.grid(column=0, row=3)
inputVanbangoc = Entry(window,width=100)
inputVanbangoc.grid(column=1, row=3)

khoa = Label(window, text="Khoa",font=("Arial", 14))
khoa.grid(column=0, row=4)
inputKhoa = Entry(window,width=100)
inputKhoa.grid(column=1, row=4)

vbmahoa = Label(window, text="Van ban duoc ma hoa",font=("Arial", 14))
vbmahoa.grid(column=0, row=5)
inputVbmahoa = Entry(window,width=100)
inputVbmahoa.grid(column=1, row=5)

vbgiaima = Label(window, text="Van ban duoc giai ma",font=("Arial", 14))
vbgiaima.grid(column=0, row=6)
inputVbgiaima = Entry(window,width=100)
inputVbgiaima.grid(column=1, row=6)

btnMahoa = Button(window, text="Mã Hóa", command=mahoa_DES)
btnMahoa.grid(column=0, row=7)

btnGiaima = Button(window, text="Giai ma", command=giaima_DES)
btnGiaima.grid(column=1, row=7)


window.geometry('800x600')
window.mainloop()
