with open('tables.txt','w') as file:
    for i in range(2,21):
        file.write('\n')
        for m in range(1,11):
            file.write(f'{i}*{m}={i*m}\n')