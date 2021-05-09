'''



import math
try :
    
    a,b,c=map(float,input().split(" "))
    s=(a+b+c)/2
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    if A>0:
        print("YES")
    else:
        print("NO")
except EOFError as e:pass
