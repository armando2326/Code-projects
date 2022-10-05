b, p, l = input().split(" ")
b = int(b)
p = int(p)
l = int(l)

if (b > 10 or p > 40 or l > 90):
    if (b > 14 or p > 60 or l > 120):
        if (b > 18 or p > 80 or l > 180):
            print("X")
        else:
            print("L")
    else:
            print("M")
else:
    print("S")
