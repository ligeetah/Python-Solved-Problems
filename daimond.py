num=int(input('Enter the number : '))
for i in range(num,0,-1):
    print(' '*i,'*'*2*(num-i))
for i in range(num):
    print(' '*i,'*'*2*(num-i))