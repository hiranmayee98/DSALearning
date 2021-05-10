'''
You're given the three angles a, b, and c respectively. 
Now check if these three angles can form a valid triangle with an area greater than 0 or not. 
Print "YES"(without quotes) if it can form a valid triangle with an area greater than 0, otherwise print "NO".
'''
a,b,c=map(int,input().split(" "))
if (a+b+c)==180 and a!=0 and b!=0 and c!=0:
    if (a+b)>=c or (b+c)>=a or (c+a)>=b:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
