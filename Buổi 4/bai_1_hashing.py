from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Hash import MD5, SHA1, SHA256, SHA512
from Cryptodome.Cipher import PKCS1_v1_5
import base64
from tkinter import *

WIDTH_INPUT_BOX = 60
def hashing():
    content = plaint_input.get().encode()
    func = hash_mode.get()
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
    hash_value.delete(0, END)
    hash_value.insert(INSERT, rs)


window = Tk()
window.title("Demo Chương Trình Băm")

plaint_label = Label(window, text="Văn bản gốc", font=("Arial", 16))
plaint_label.grid(column=0, row=1)
plaint_input = Entry(window, width=WIDTH_INPUT_BOX)
plaint_input.grid(column=1, row=1)

hash_label = Label(window, text="Giá trị băm", font=("Arial", 16))
hash_label.grid(column=0, row=3)
hash_value = Entry(window, width=WIDTH_INPUT_BOX)
hash_value.grid(column=1, row=3)

radioGroup = LabelFrame(window, text="Hàm băm")
radioGroup.grid(row=2, column=1)
hash_mode = IntVar()
hash_mode.set(-1)

md5_func = Radiobutton(
    radioGroup,
    text="Hash MD5",
    font=("Times New Roman", 11),
    variable=hash_mode,
    value=0,
    command=hashing,
)
md5_func.grid(row=4, column=0)

sha1_func = Radiobutton(
    radioGroup,
    text="Hash SHA1",
    font=("Times New Roman", 11),
    variable=hash_mode,
    value=1,
    command=hashing,
)
sha1_func.grid(row=5, column=0)

# Tương tự đối với sha256 và sha512
sha256_func = Radiobutton(
    radioGroup,
    text="Hash SHA256",
    font=("Times New Roman", 11),
    variable=hash_mode,
    value=2,
    command=hashing,
)
sha256_func.grid(row=4, column=1)

sha512_func = Radiobutton(
    radioGroup,
    text="Hash SHA512",
    font=("Times New Roman", 11),
    variable=hash_mode,
    value=3,
    command=hashing,
)
sha512_func.grid(row=5, column=1)
# Hien thi cua so
window.geometry("520x180")
window.mainloop()
