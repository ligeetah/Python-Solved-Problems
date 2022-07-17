def flatten(list):
    listr=[]
    for i in range(len(list)):
        for m in range(len(i)):
            listr.append(m)
    return listr
print(flatten([[1,2],[3,4,6,3,3]]))