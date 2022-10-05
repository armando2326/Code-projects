input = int(input())

#string method
def numstring(x):
    num = str(x)
    sum = 0
    for i in num:
        sumd = int(i)
        sum += sumd
    return sum

#int method
def instring(x):
    sum = 0
    while x > 0:
        sumd = x%10
        sum += sumd
        x = int(x/10)
    return sum

print(numstring(input))
print(instring(input))