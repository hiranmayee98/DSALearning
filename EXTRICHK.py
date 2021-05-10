'''
You're given the length of three sides a, b, and c respectively. 
Now If these three sides can form an Equilateral Triangle then print 1, 
if these three sides can form an Isosceles Triangle then print 2, 
if these three sides can form a Scalene Triangle then print 3, otherwise print −1.
'''


# cook your dish here
a,b,c =map(int,input().split(" "))
if (a+b)>c and (b+c)>a and (c+a)>b:
    if a==b and b==c and c==a:
        print(1)
    elif a==b or b==c or c==a:
        print(2)
    elif a!=b and b!=c and c!=a:
        print(3)
else :
    print(-1)
