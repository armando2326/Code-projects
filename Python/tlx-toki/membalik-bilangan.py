N = int(input())
nums = []

for i in range(N):
    nums.append(input())

for num in nums:
    temp = int(num)
    reverse = 0
    flag = True
    while flag:
        reverse = reverse*10 + temp%10
        temp = int(temp/10)
        if temp == 0:
            flag = False
    print(reverse)
