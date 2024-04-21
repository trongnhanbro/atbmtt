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

print(encryptAF("Chuc ban lam bai TOT", 3, 5, 53))
#LzlkCheQCKeNCheBCJvJ