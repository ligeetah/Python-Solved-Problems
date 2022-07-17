from pyparsing import Word


def get_capitals(str):
    list=[]
    for i in range(len(str)):
        if(str[i].isupper()):
            list.append(i)
    return list
print(get_capitals('WOoWEDJJjjnnJK'))