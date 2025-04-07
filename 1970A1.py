t = input()
count_balance = 0
info = []
balance_list = []

for i in range(len(t)):
  info.append((count_balance, -i , t[i]))
  if t[i] == '(':
    count_balance += 1
  else:
    count_balance -= 1

info.sort()
balance_list = ''.join(char for _, _, char in info)
print(balance_list)
