'''
You're given the length of three sides a, b, and c respectively.
Now check if these three sides can form a triangle or not. 
Print "YES"(without quotes) if it can form a valid triangle with an area greater than 0, 
otherwise print "NO" (without quotes).
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
