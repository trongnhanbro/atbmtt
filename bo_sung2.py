string = "qwertyuiopasdfghjklzxcvbnm"
a = "123"
b = "abcde3456"

c = "a1b2c3"
def xen(a, b):
    check = ""
    result = ""
    for i in range(0, len(b)):
        if i == len(b) - 1:
            result += b[i]
            break
        result += b[i]
        if i <= len(a) - 1:
            result += a[i]
        else:
            for e in string:
                if e not in a and e not in check:
                    result += e
                    check += e
                    break
    return result


