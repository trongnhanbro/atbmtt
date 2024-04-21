#Bai 3
# CAC HAM CAN THIET
def Char2Num(c):
    return ord(c)-65

def Num2char(n):
    return chr(n+65)

def encryprtAF(txt,a,b,m):
    r=""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2char(e)
    return r

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1, = 1, 0, 0, 1
    while m!=0:
        q, a, m = a//m, m, a%m
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0 - q*y1
    if x0 < 0: x0 = temp+x0
    return x0

def decryptAF(txt,a,b,m):
    r=""
    a1 = xgcd(a,m)
    for c in txt:
        e = (a1*(Char2Num(c)-b)) % m
        r = r+Num2char(e)
    return r
#Bai 3
def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 128
    entxt = encryprtAF(plaintxt.get(), a, b, m)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)

def giaima():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 128
    detxt = decryptAF(ciphertxt.get(), a, b, m)
    DEAFbtntxt.delete(0,END)
    DEAFbtntxt.insert(INSERT,detxt)

#Giao dien
from tkinter import *

#Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

#Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lb1 = Label(window, text="CHUONG TRINH DEMO",font=("Arial Bold", 20))
lb1.grid(column=1, row=1)
lb2 = Label(window, text="MAT MA AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)

plainlb3 = Label(window, text="PLAIN TEXT", font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window, width=30)
plaintxt.grid(column=1, row=3)

KEYlb4 = Label(window, text="KEY PAIR", font=("Arial", 14))
KEYlb4.grid(column=2, row=3)

KEYA1 = Entry(window, width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window, width=5)
KEYB1.grid(column=4, row=3)

KEYlb4 = Label(window, text="KEY PAIR", font=("Arial", 14))
KEYlb4.grid(column=2, row=3)

#Tao nut co ten Afbtn
Afbtn = Button(window, text="Ma Hoa", command=mahoa)
Afbtn.grid(column=5, row=3)

#CIPHER TEXT
cipherlb5 = Label(window, text="CIPHER TEXT", font=("Arial", 14))
cipherlb5.grid(column=0, row=4)
ciphertxt = Entry(window, width=30)
ciphertxt.grid(column=1, row=4)

#Tao nut co ten DEAFbtn
DEAFbtn = Button(window, text="Giai Ma", command=giaima)
DEAFbtn.grid(column=2, row=4)

DEAFbtntxt = Entry(window, width=30)
DEAFbtntxt.grid(column=3, row=4)

#Hien thi cua so
window.geometry('800x600')
window.mainloop()



