from Cryptodome.Cipher import DES
import base64
def pad(s): 
    # Nếu độ dài của chuỗi là bội số của 8, không thêm gì cả
    if len(s) % 8 == 0:
        return s
    # Ngược lại, thêm vào cuối số ký tự còn thiếu cho đủ bội của 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)


def unpad(s):
    # Lấy ký tự cuối cùng trong chuỗi, chuyển nó thành số nguyên,
    # và sử dụng nó để xác định số lượng ký tự padding cần loại bỏ.
    padding_size = ord(s[-1])
    
    # Kiểm tra xem số lượng padding có hợp lệ không.
    if padding_size > 8 or padding_size <= 0:
        raise ValueError("Invalid padding size")
    
    # Loại bỏ padding và trả về chuỗi đã được loại bỏ padding.
    return s[:-padding_size]


def decrypt_des(cipher_input, key_input):
  txt = base64.b64decode(cipher_input)
  key = pad(key_input).encode("utf8")
  cipher = DES.new(key, DES.MODE_ECB)
  
  # Kiểm tra xem dữ liệu có đúng kích thước khối không.
  if len(txt) % 8 != 0:
    raise ValueError("Invalid ciphertext size")
  
  plaintext = unpad(cipher.decrypt(txt))
  return plaintext


def main():
  """
  Hàm chính.
  """

  # Danh sách từ điển các quốc gia.
  countries = ["VIETNAM", "UNITED STATES", "UNITED KINGDOM", "CHINA", "JAPAN"]

  # Văn bản được mã hóa DES.
  ciphertext = "LsmDvf9t1pLPn+NZ99+cVx+V1RO12/9KNqk9"

  # Duyệt qua danh sách từ điển các quốc gia.
  for country in countries:
    # Giải mã văn bản bằng khóa là tên quốc gia.
    plaintext = decrypt_des(ciphertext, country)

    # Kiểm tra xem văn bản giải mã có hợp lệ hay không.
    if plaintext and not plaintext.startswith("-----BEGIN "):
      print("Khóa:", country)
      print("Văn bản gốc:", plaintext)
      break

if __name__ == "__main__":
  main()
