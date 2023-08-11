x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_main = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            condition = i + j + k
            if condition != n:
                list_main.append([i, j, k])
print(list_main)
