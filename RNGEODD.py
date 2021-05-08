'''
You're given two numbers L and R. 
Print all odd numbers between L and R (both inclusive) in a single line separated by space, in ascending (increasing) order.
'''
try :
   x=input()
   L,R=map(int,x.split(" "))
   for i in range(L,R+1):
       if i%2!=0:
           print(i)
           
except EOFError as e:pass
