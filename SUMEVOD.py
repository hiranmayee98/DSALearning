'''
You are given a number N and find the sum of the first N odd and even numbers in a line separated by space. 
All even and odd numbers should be greater than 0.
'''
try :
    o=1
    e=2
    so=0
    se=0
    N=int(input())
    for i in range(N):
        so=so+o
        o=o+2
        se=se+e
        e=e+2
    if se>0 and so>0:
        print(so,se)
except EOFError as e:pass
