#Ho và ten: Nguyễn Thanh Duy
#MSSV: B1913291
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import filedialog
from unittest.mock import sentinel

def generate_key():
	key = RSA.generate(1024)
	pri = save_file(key.exportKey('PEM'),'wb', 'Lưu khóa cá nhân', (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
	pub = save_file(key.publickey().exportKey('PEM'), 'wb', 'Lưu khóa công khai', (("All files", "*.*"),("PEM files", "*.pem")),".pem")
	pri_key.delete('1.0',END)
	pri_key.insert(END,key.exportKey('PEM'))
	pub_key.delete('1.0',END)
	pub_key.insert(END,key.publickey().exportKey('PEM'))

def save_file(content, _mode, _title, _filetypes, _defaultextension):
	f = filedialog.asksaveasfile(mode = _mode, initialdir = "D:/", title = _title, filetypes = _filetypes, defaultextension = _defaultextension)
	if f is None: return
	f.write(content)
	f.close()

def get_key(key_style):
	filename = filedialog.askopenfilename(initialdir = "D:/", title = "Open " + key_style, filetypes = (("PEM files", "*.pem"),("All files", "*.*")))
	if filename is None: return
	file = open(filename,"rb")
	key = file.read()
	file.close()
	return RSA.importKey(key)

def mahoa_rsa():
	txt = plaintxt.get().encode()
	pub_key = get_key("Public Key")
	cipher = PKCS1_v1_5.new(pub_key)
	entxt = cipher.encrypt(txt)
	entxt = base64.b64encode(entxt)
	ciphertxt.delete(0,END)
	ciphertxt.insert(INSERT,entxt)

def giaima_rsa():
    txt=ciphertxt.get().encode()
    txt=base64.b64decode(txt)
    pri_key=get_key("Private Key")
    cipher= PKCS1_v1_5.new(pri_key)
    detxt=cipher.decrypt(txt,sentinel)
    denctxt.delete(0,END)
    denctxt.insert(INSERT, detxt)


# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG RSA", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)
plainlb1 = Label(window, text="Văn bản gốc", font=("Arial", 14))
plainlb1.grid(column=0, row=3)
plaintxt = Entry(window, width=90)
plaintxt.grid(column=1, row=3)
plainlb2 = Label(window, text="Văn bản được mã hóa", font=("Arial", 14))
plainlb2.grid(column=0, row=4)
ciphertxt = Entry(window, width=90)
ciphertxt.grid(column=1, row=4)
plainlb3 = Label(window, text="Văn bản được giải mã", font=("Arial", 14))
plainlb3.grid(column=0, row=5)
denctxt = Entry(window, width=90)
denctxt.grid(column=1, row=5)
plainlb4 = Label(window, text="Khóa cá nhân", font=("Arial", 14))
plainlb4.grid(column=0, row=6)
pri_key = Text(window,height=10, width=60)
pri_key.grid(column=1, row=6)
plainlb5 = Label(window, text="Khóa công khai", font=("Arial", 14))
plainlb5.grid(column=0, row=7)
pub_key = Text(window, height=10, width=60)
pub_key.grid(column=1, row=7)
cre_keybtn = Button(window, text="Tạo khóa", command=generate_key)
cre_keybtn.grid(column=1, row=9)
AFbtn = Button(window, text="Mã Hóa", command=mahoa_rsa)
AFbtn.grid(column=1, row=10)
DEAFbtn = Button(window, text="Giải Mã", command=giaima_rsa)
DEAFbtn.grid(column=1, row=11)

# Hien thi cua so
window.geometry('800x600')
window.mainloop()
