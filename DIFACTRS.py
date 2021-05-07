#You are given a number N and find all the distinct factors of N
try:
    x=int(input())
    c=0
    s=""
    for i in range(1,x+1):
        if x%i==0:
            s=s+str(i)+" "
            c=c+1
    print(c)
    print(s)
except EOFError as e: pass
