a = [0] * 4


input_list = input().split(" ")  


for i in range(len(input_list)):
    a[i] = int(input_list[i])

a.sort()

for i in range(3):
    print(a[3] - a[i], end=" ")
