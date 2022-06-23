num = [12, 34, 4, 23, 65, 54]

n = len(num)

for i in range(n):
    for j in range(n-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
            
print(num)
