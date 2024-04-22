def Char2Num(c):
    if '0' <= c <= '9':
        return ord(c) - 48  # '0' -> 0, '1' -> 1, ..., '9' -> 9
    if 'A' <= c <= 'Z':
        return ord(c) - 55  # 'A' -> 10, 'B' -> 11, ..., 'Z' -> 35
    if 'a' <= c <= 'z':
        return ord(c) - 61  # 'a' -> 36, 'b' -> 37, ..., 'z' -> 61
    if c == ' ':
        return 62  # khoảng trắng
    return 63  # ký tự không nhận dạng

def Num2Char(c):
    if 0 <= c <= 9:
        return chr(c + 48)  # 0 -> '0', 1 -> '1', ..., 9 -> '9'
    if 10 <= c <= 35:
        return chr(c + 55)  # 10 -> 'A', 11 -> 'B', ..., 35 -> 'Z'
    if 36 <= c <= 61:
        return chr(c + 61)  # 36 -> 'a', 37 -> 'b', ..., 61 -> 'z'
    if c == 62:
        return ' '  # khoảng trắng
    return chr(94)  # ký tự không nhận dạng

def encryptAF(txt, a, b, m):
    r = ""
    for c in txt:
        e = (a * Char2Num(c) + b) % m 
        r += Num2Char(e)
    return r

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1 
        y0, y1 = y1, y0 - q * y1
    if x0 < 0:
        x0 += temp
    return x0

def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        e = (a1 * (Char2Num(c) - b)) % m 
        r += Num2Char(e)
    return r

# Test mã hóa và giải mã
# Test mã hóa và giải mã
plain_text = "Hello World 123"
a = 7
b = 10
m = 64  # số ký tự trong bảng mã mới
encrypted_text = encryptAF(plain_text, a, b, m)
print("Mã hóa:", encrypted_text)
decrypted_text = decryptAF(encrypted_text, a, b, m)
print(decrypted_text)
# print("Giải mã:", decrypted_text.encode('utf-8').decode('utf-8'))


#hựhrwhj