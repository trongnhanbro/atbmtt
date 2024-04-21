
from tkinter import *
from Cryptodome.Cipher import DES
import base64
from tkinter import filedialog
from os import path

#Bài tập 1
def pad(s): 
    #Them vao cuoi so con thieu cho du boi cua 8
    return s + (8 - len(s) % 8) * chr(8-len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encode_DES():
    txt = pad(plaint_input.get()).encode("utf8")
    key = pad(key_input.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    cipher_input.delete(0, END)
    cipher_input.insert(INSERT, entxt)

def decode_DES():
    txt = cipher_input.get()
    txt = base64.b64decode(txt)
    key = pad(key_input.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    decode_txt_input.delete(0, END)
    decode_txt_input.insert(INSERT, detxt)


#Bài tập 2
#Học viên viết 1 chương trình cho phép mã hóa và giải mã 1 tập tin txt.

def select_file_plaint():
	file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
	with open(file) as f:
		data = f.read()

	plaint_input.delete(0,END)
	plaint_input.insert(INSERT,data)
      
def select_file_cipher():
	file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
	with open(file) as f:
		data = f.read()

	cipher_input.delete(0,END)
	cipher_input.insert(INSERT,data)

#Giao diện
window = Tk()
window.title("Demo Mật Mã Đối Xứng DES")

plaint_label = Label(window, text="Văn bản gốc",font=("Arial", 16))
plaint_label.grid(column=0, row=1)

key_label = Label(window, text="Khóa",font=("Arial", 16))
key_label.grid(column=0, row=2)

cipher_label = Label(window, text="Văn bản được mã hóa",font=("Arial", 16))
cipher_label.grid(column=0, row=3)

entxt_label = Label(window, text="Văn bản được giải mã",font=("Arial", 16))
entxt_label.grid(column=0, row=4)

plaint_input = Entry(window, width=50)
plaint_input.grid(column=2, row=1)

key_input = Entry(window, width=50)
key_input.grid(column=2, row=2)

cipher_input = Entry(window, width=50)
cipher_input.grid(column=2, row=3)

decode_txt_input = Entry(window, width=50)
decode_txt_input.grid(column=2, row=4)

encode_button = Button(window, text="Mã Hóa", command=encode_DES)
encode_button.grid(column=0, row=5)

decode_button = Button(window, text="Giải Mã", command=decode_DES)
decode_button.grid(column=1, row=5)

select_file_plaint_button = Button(window, 
                                   text="Chọn file txt", 
                                   command=select_file_plaint)
select_file_plaint_button.grid(column=3, row=1)

select_file_cipher_button = Button(window, 
                                   text="Chọn file txt", 
                                   command=select_file_cipher)
select_file_cipher_button.grid(column=3, row=3)

#Hien thi cua so
window.geometry('800x200')
window.mainloop()