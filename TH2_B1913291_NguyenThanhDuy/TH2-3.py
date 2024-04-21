#Ho va ten: Nguyen Thanh Duy
#MSSV: B1913291
import pandas as pd
from Crypto.Cipher import DES3
from Crypto.Cipher import DES
import base64

def giaima_DES(vbmahoa, khoa):
    txt = vbmahoa
    txt = base64.b64decode(txt)
    key = pad(khoa).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    return detxt

def pad(s):
    return s + (8-len(s) % 8)*chr(8-len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

url = 'https://raw.githubusercontent.com/umpirsky/country-list/master/data/en/country.csv'
df = pd.read_csv(url)
country = df['value']

vbmahoa = "lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=="
vbgoiy = "The treasure is under the coconut tree"


for key in country:
    key = key[:7]
    try:
        res = giaima_DES(vbmahoa, key)
        res = res.decode('utf-8')
        if(res == vbgoiy):
            print(f"Khoa: {key} ",)
            print(f"{res}")
            break
     
    except: continue
    
mh2 = "LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=="
mh3 = "5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9"

print(giaima_DES(mh2, key).decode('utf-8'))
print(giaima_DES(mh3, key).decode('utf-8'))