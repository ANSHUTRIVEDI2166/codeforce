ans=int(input())
str=input()

cn=0
for i in range(ans):
    if str[i]=='A':
        cn+=1
    else:
        cn-=1

if cn==0:
    print('Friendship')
elif cn>0:
    print('Anton')
else:
    print('Danik')
