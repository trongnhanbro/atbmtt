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

print(decryptAF("LzlkCheQCKeNCheBCJvJ", 3, 5, 53))
#ARMMVFTVEMOFFDFPFONZFFFIFFFFFFF