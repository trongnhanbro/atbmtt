#Ho va ten sinh vien: Tran Trong Nhan
#Ma so sinh vien: B2017064
#STT: 33

from os import path
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *
from tkinter import filedialog
WIDTH_INPUT_BOX = 100
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
	
def get_key(key_style):
    filename = filedialog.askopenfilename(
		    initialdir= path.dirname(__file__),
		    title = "Open " + key_style, 
            filetypes = (("PEM files", "*.pem"),("All files", "*.*"))
		)
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

def mahoa_rsa():
    txt = plaint_input.get().encode()
    pub_key = get_key("Public Key")
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    cipher_input.delete(0,END)
    cipher_input.insert(INSERT,entxt) 

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(
          mode = _mode, 
          initialdir= path.dirname(__file__),
          title = _title, 
          filetypes = _filetypes, 
          defaultextension = _defaultextension
        )
    
    if f is None: return
    f.write(content)
    f.close()


def generate_key():
    key = RSA.generate(1024)
    pri = save_file(
            key.exportKey('PEM'), 
            'wb', 
            'Lưu khóa cá nhân', 
            (("All files", "*.*"), 
            ("PEM files", "*.pem")), 
            ".pem"
        )
    pub = save_file(
          key.publickey().exportKey('PEM'), 
          'wb', 
          'Lưu khóa công khai', 
          (("All files", "*.*"),("PEM files", "*.pem")), 
          ".pem"
        )
    private_key_input.delete(0,END)
    private_key_input.insert(END,key.exportKey('PEM'))
    public_key_input.delete(0,END)
    public_key_input.insert(END,key.publickey().exportKey('PEM'))


#Giao diện
window = Tk()
window.title("Demo Mật Mã Đối Xứng DES")

plaint_label = Label(window, text="Văn bản gốc",font=("Arial", 16))
plaint_label.grid(column=0, row=1)

cipher_label = Label(window, text="Văn bản được mã hóa",font=("Arial", 16))
cipher_label.grid(column=0, row=3)

entxt_label = Label(window, text="Văn bản được giải mã",font=("Arial", 16))
entxt_label.grid(column=0, row=4)

private_label = Label(window, text="Khóa cá nhân",font=("Arial", 16))
private_label.grid(column=0, row=5)

public_label = Label(window, text="Khóa công khai",font=("Arial", 16))
public_label.grid(column=0, row=6)

plaint_input = Entry(window, width=WIDTH_INPUT_BOX)
plaint_input.grid(column=2, row=1)

cipher_input = Entry(window, width=WIDTH_INPUT_BOX)
cipher_input.grid(column=2, row=3)

decode_txt_input = Entry(window, width=WIDTH_INPUT_BOX)
decode_txt_input.grid(column=2, row=4)

private_key_input = Listbox(window, width=WIDTH_INPUT_BOX)
private_key_input.grid(column=2, row=5)

public_key_input = Listbox(window, width=WIDTH_INPUT_BOX)
public_key_input.grid(column=2, row=6)

encode_button = Button(window, text="Tạo và lưu Khóa", command=generate_key)
encode_button.grid(column=0, row=7)

encode_button = Button(window, text="Mã Hóa", command=mahoa_rsa)
encode_button.grid(column=1, row=7)

decode_button = Button(window, text="Giải Mã", )
decode_button.grid(column=2, row=7)

select_file_plaint_button = Button(window, 
                                   text="Chọn file txt", 
                                   command=select_file_plaint)
select_file_plaint_button.grid(column=3, row=1)

select_file_cipher_button = Button(window, 
                                   text="Chọn file txt", 
                                   command=select_file_cipher)
select_file_cipher_button.grid(column=3, row=3)

#Hien thi cua so
window.geometry('1000x480')
window.mainloop()