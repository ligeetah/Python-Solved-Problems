def score(num):
    with open('score.txt','r')as f:
        if(num>int(f.readline())):
            with open('score.txt','w')as f:
                f.write(str(num))
score(435)