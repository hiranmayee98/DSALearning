'''
You're given the length of three sides a, b, and c respectively.
Now check if these three sides can form a triangle or not. 
Print "YES"(without quotes) if it can form a valid triangle with an area greater than 0, 
otherwise print "NO" (without quotes).
'''

a,b,c=map(float,input().split(" "))
s=(a+b+c)/2
A=(s*(s-a)*(s-b)*(s-c))**0.5
if (a+b)>c and (b+c)>a and (c+a)>b:
    if A>0:
        print("YES")
    else:
        print("NO")
