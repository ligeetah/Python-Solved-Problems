num1=input("Enter first number : ")
num2=input("Enter second number : ")
ans=''
rem=0
for i in range(len(num1)):
    a=str(int(num1[i])+int(num2[i])+rem)
    if len(a)>0:
        ans=ans+a[len(a)-1]
        rem=int(a[0])
    else:
        rem=0
        ans=ans+a[0]
print(ans)
# str='33'
# s=''
# if len(str)>0:
#     s=s+str[1]
#     print(s)