from math import gcd
pedagang = int(input())
hari = []

for i in range(pedagang):
    hari.append(int(input()))

kpk = 1
for j in hari:
    kpk = kpk*j//gcd(kpk,j)

print(kpk)