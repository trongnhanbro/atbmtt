# Ho va ten sinh vien: Nguyen Thanh Duy
# Ma so sinh vien: B1913291

def Char2Num(c):
    if(c >= 'A' and c <= 'Z'):
        return ord(c)-65
    if(c >= 'a' and c <= 'z'):
        return ord(c)-71
    return 52

def Num2Char(c):
    if(c >= 0 and c <= 25):
        return chr(c+65)
    if(c >= 26 and c <= 51):
        return chr(c+71)
    return chr(94)

    
# def encryptAF A: 0, Z=25, a=32, z = 57

def encryptAF(txt, a, b, m):
    r=""
    for c in txt:
        e = (a*Char2Num(c)+b) % m 
        r = r + Num2Char(e)
    return r

def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 53
    entxt = encryptAF(plaintxt.get(),a,b,m)
    CipherTextInput.delete(0,END)
    CipherTextInput.insert(INSERT,entxt)


def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a%m
        x0, x1 = x1, x0 - q*x1 
        y0, y1 = y1, y0 - q*y1
    if x0 < 0:
        x0 = x0 + temp
    return x0

def decryptAF(txt, a, b, m):
    r=""
    a1 = xgcd(a, m)
    for c in txt:
        e = (a1*(Char2Num(c)-b)) % m 
        r = r + Num2Char(e)
    return r

def giaima():
    cipherText = CipherTextInput.get()
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 53
    detxt = decryptAF(cipherText,a,b,m)
    GiaiMaInput.delete(0,END)
    GiaiMaInput.insert(INSERT,detxt)

from tkinter import *

window = Tk()
window.title("Welcome to Demo AT&BMTT")

lb0 = Label(window, text=" ", font=("Arial Bold",10))
lb0.grid(column=0, row=0)
lb1 = Label(window, text="Chuong Trinh Demo", font=("Arial Bold",20))
lb1.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)
AFbtn = Button(window, text="Mã Hóa", command=mahoa)
AFbtn.grid(column=5, row=3)

CipherText = Label(window, text="CIPHER TEXT",font=("Arial", 14))
CipherText.grid(column=0, row=4)
CipherTextInput = Entry(window,width=20)
CipherTextInput.grid(column=1, row=4)
GiaiMaBtn = Button(window, text="Giai Ma", command=giaima)
GiaiMaBtn.grid(column=2, row=4)
GiaiMaInput = Entry(window,width=20)
GiaiMaInput.grid(column=3, row=4)

window.geometry('800x600')
window.mainloop()


