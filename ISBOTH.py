'''
You're given a number N. 
If N is divisible by 5 or 11 but not both then print "ONE"(without quotes). 
If N is divisible by both 5 and 11 then print "BOTH"(without quotes). 
If N is not divisible by 5 or 11 then print "NONE"(without quotes).
'''
x=int(input())
if x%5==0 or x%11==0:
    print("ONE")
elif x%5==0 and x%11==0:
    print("BOTH")
else:
    print("NONE")
