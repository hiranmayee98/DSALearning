try :
    n=int(input())
    for i in range(n):
        x=0
        while x<(n-i-1):
            print(" ",end=" ")
            x=x+1
        else:
            for j in range(i+1):
                print("*",end=" ")
        print()
    
except EOFError as e:pass
