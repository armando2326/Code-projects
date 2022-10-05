A, OP, B = input().split(" ")
A = int(A)
B = int(B)
OP = str(OP)

def hitungapakah(x, y, z):
    if z == "+":
        return (x + y)
    elif z == "-":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == ">":
        v = (x > y)
    elif z == "<":
        v = (x < y)
    elif z == "=":
        v = (x == y)
    
    if v:
        return "benar"
    else:
        return "salah"

print(hitungapakah(A, B, OP))