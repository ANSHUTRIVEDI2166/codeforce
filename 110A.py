n = input()

count = 0
for i in n:
    if i in '47':
        count += 1
        
if count in {4, 7}:
    print("YES")
else:
    print("NO")
