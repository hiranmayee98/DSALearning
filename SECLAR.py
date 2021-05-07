#Given three distinct integers A, B and C, print the second largest number among them.
try :
    A=int(input())
    B=int(input())
    C=int(input())

    l=[A,B,C]
    l.sort()
    print(l[1])
except EOFError as e:pass
