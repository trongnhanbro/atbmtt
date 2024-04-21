#Ho và ten: Nguyễn Thanh Duy
#MSSV: B1913291

# -*- coding: utf8 -*-
from tkinter import *
import tkinter as tk
from Crypto.Cipher import DES
import base64
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from tkinter import filedialog
from unittest.mock import sentinel


#mã hóa DES
def pad(s):
    #Them vao cuoi so con thieu cho du boi cua 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)
def unpad(s):
    return s[:-ord(s[len(s)-1:])]
class mahoa_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa DES")
        self.geometry('800x600')

        self.lbl = Label(self,text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)

        self.lb2 = Label(self,text="MẬT MÃ ĐỐI XỨNG DES",font=("Arial Bold", 15))
        self.lb2.grid(column=1, row=2)
        self.plainlb3 = Label(self,text="Văn bản gốc",font=("Arial", 14))
        self.plainlb3.grid(column=0, row=4)
        self.plaintxt = Entry(self,width=90)
        self.plaintxt.grid(column=1, row=4)
        self.lb4 = Label(self, text="Khóa",font=("Arial", 14))
        self.lb4.grid(column=0, row=5)
        self.keytxt = Entry(self,width=90)
        self.keytxt.grid(column=1, row=5)
        self.lb5 = Label(self,text="Văn bản được mã hóa",font=("Arial", 14))
        self.lb5.grid(column=0, row=6)
        self.ciphertxt = Entry(self,width=90)
        self.ciphertxt.grid(column=1, row=6)
        self.lb6 = Label(self,text="Văn bản được giải mã",font=("Arial", 14))
        self.lb6.grid(column=0, row=7)
        self.denctxt = Entry(self,width=90)
        self.denctxt.grid(column=1, row=7)
        self.btn_enc = Button(self, text="Mã Hóa",command=self.mahoa_DES)
        self.btn_enc.grid(column=1, row=9)
        self.btn_dec = Button(self, text="Giải Mã ",command=self.giaima_DES)
        self.btn_dec.grid(column=1, row=10)
        self.thoat = Button(self,text="Quay về màn hình chính",command=self.destroy)
        self.thoat.grid(column=1, row=11)

    def mahoa_DES(self):
        txt = pad(self.plaintxt.get()).encode()
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)
    def giaima_DES(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt))
        self.denctxt.delete(0,END)
        self.denctxt.insert(INSERT,detxt)

#ma hóa Affine
def Char2Num(c):
    if c == ' ':
        return 26
    return ord(c) - 65


def Num2Char(n):
    if n == 26:
        return ' '
    return chr(n + 65)


def encryptAF(txt, a, b, m):
    r = ""
    for c in txt:
        e = (a * Char2Num(c) + b) % m
        r = r + Num2Char(e)
    return r

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp + x0
    return x0


def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        e = (a1 * (Char2Num(c) - b)) % m
        r = r + Num2Char(e)
    return r


# Khoi tao man hinh chinh
class mahoa_AFF(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa Affine")
        self.geometry('800x600')
        self.lb0 = Label(self, text=" ", font=("Arial Bold", 10))
        self.lb0.grid(column=0, row=0)
        self.lbl = Label(self, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)
        self.lb2 = Label(self, text="MẬT MÃ AFFINE", font=("Arial Bold", 15))
        self.lb2.grid(column=0, row=2)
        self.plainlb3 = Label(self, text="PLAIN TEXT", font=("Arial", 14))
        self.plainlb3.grid(column=0, row=3)
        self.plaintxt = Entry(self, width=20)
        self.plaintxt.grid(column=1, row=3)
        self.KEYlb4 = Label(self, text="KEY PAIR", font=("Arial", 14))
        self.KEYlb4.grid(column=2, row=3)
        self.KEYA1 = Entry(self, width=3)
        self.KEYA1.grid(column=3, row=3)
        self.KEYB1 = Entry(self, width=5)
        self.KEYB1.grid(column=4, row=3)
        self.cipherlb4 = Label(self, text="CIPHER TEXT", font=("Arial", 14))
        self.cipherlb4.grid(column=0, row=4)
        self.ciphertxt = Entry(self, width=20)
        self.ciphertxt.grid(column=1, row=4)
        self.AFbtn = Button(self, text="Mã Hóa", command=self.mahoa)
        self.AFbtn.grid(column=5, row=3)
        self.DEAFbtntxt = Entry(self, width=20)
        self.DEAFbtntxt.grid(column=3, row=4)
        self.DEAFbtn = Button(self, text="Giải Mã", command=self.giaima)
        self.DEAFbtn.grid(column=2, row=4)
    def mahoa(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 27
        entxt = encryptAF(self.plaintxt.get(), a, b, m)
        self.ciphertxt.delete(0, END)
        self.ciphertxt.insert(INSERT, entxt)

    def giaima(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 27
        txt = decryptAF(self.ciphertxt.get(), a, b, m)
        self.DEAFbtntxt.delete(0, END)
        self.DEAFbtntxt.insert(INSERT, txt)

#giai ma RSA
def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(mode = _mode,initialdir = "D:/",title = _title,filetypes = _filetypes,defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()

def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "D:/",title = "Open " + key_style,filetypes = (("PEM files", "*.pem"),("Allfiles", "*.*")))
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

class mahoa_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa RSA")
        self.geometry('800x600')

        self.lb0 = Label(self, text=" ", font=("Arial Bold", 10))
        self.lb0.grid(column=0, row=0)
        self.lbl = Label(self, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)
        self.lb2 = Label(self, text="MẬT MÃ ĐỐI XỨNG RSA", font=("Arial Bold", 15))
        self.lb2.grid(column=1, row=2)
        self.plainlb1 = Label(self, text="Văn bản gốc", font=("Arial", 14))
        self.plainlb1.grid(column=0, row=3)
        self.plaintxt = Entry(self, width=90)
        self.plaintxt.grid(column=1, row=3)
        self.plainlb2 = Label(self, text="Văn bản được mã hóa", font=("Arial", 14))
        self.plainlb2.grid(column=0, row=4)
        self.ciphertxt = Entry(self, width=90)
        self.ciphertxt.grid(column=1, row=4)
        self.plainlb3 = Label(self, text="Văn bản được giải mã", font=("Arial", 14))
        self.plainlb3.grid(column=0, row=5)
        self.denctxt = Entry(self, width=90)
        self.denctxt.grid(column=1, row=5)
        self.plainlb4 = Label(self, text="Khóa cá nhân", font=("Arial", 14))
        self.plainlb4.grid(column=0, row=6)
        self.pri_key = Text(self,height=10, width=60)
        self.pri_key.grid(column=1, row=6)
        self.plainlb5 = Label(self, text="Khóa công khai", font=("Arial", 14))
        self.plainlb5.grid(column=0, row=7)
        self.pub_key = Text(self, height=10, width=60)
        self.pub_key.grid(column=1, row=7)
        self.cre_keybtn = Button(self, text="Tạo khóa", command=self.generate_key)
        self.cre_keybtn.grid(column=1, row=9)
        self.AFbtn = Button(self, text="Mã Hóa", command=self.mahoa_rsa)
        self.AFbtn.grid(column=1, row=10)
        self.DEAFbtn = Button(self, text="Giải Mã", command=self.giaima_rsa)
        self.DEAFbtn.grid(column=1, row=11)
        self.thoat = Button(self,text="Quay về màn hình chính",command=self.destroy)
        self.thoat.grid(column=1, row=12)

    # Tao khoa
    def generate_key(self):
        key = RSA.generate(1024)
        pri = save_file(key.exportKey('PEM'),'wb','Lưu khóa cá nhân',(("All files", "*.*"), ("PEM files", "*.pem")),".pem")
        pub = save_file(key.publickey().exportKey('PEM'),'wb','Lưu khóa công khai',(("All files", "*.*"),("PEM files", "*.pem")),".pem")
        self.pri_key.delete('1.0',END)
        self.pri_key.insert(END,key.exportKey('PEM'))
        self.pub_key.delete('1.0',END)
        self.pub_key.insert(END,key.publickey().exportKey('PEM'))

    # Ma hoa
    def mahoa_rsa(self):
        txt = self.plaintxt.get().encode()
        pub_key = get_key("Public Key")
        cipher = PKCS1_v1_5.new(pub_key)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)

    # Giai ma
    def giaima_rsa(self):
        txt=self.ciphertxt.get()
        txt=base64.b64decode(txt)
        pri_key=get_key("Private Key")
        cipher= PKCS1_v1_5.new(pri_key)
        detxt=cipher.decrypt(txt,sentinel)
        self.denctxt.delete(0,END)
        self.denctxt.insert(INSERT, detxt)


class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)
        self.mahoa_Affine = Button(text="Mã hóa Affine",font=("Times New Roman", 11),command=self.AFF)
        self.mahoa_Affine.pack()
        self.mahoa_DES = Button(text="Mã hóa DES",font=("Times New Roman", 11),command=self.des)
        self.mahoa_DES.pack()
        self.mahoa_RSA = Button(text="Mã hóa RSA ",font=("Times New Roman", 11),command=self.RSA)
        self.mahoa_RSA.pack()
        self.thoat = Button(text="Kết Thúc",font=("Times New Roman", 11),command=quit)
        self.thoat.pack()
    def des(self):
        mahoa_DES(self)
    def AFF(self):
        mahoa_AFF(self)
    def RSA(self):
        mahoa_RSA(self)
  
def main():
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry('300x200')
    MainWindow(window)
    window.mainloop()
main()