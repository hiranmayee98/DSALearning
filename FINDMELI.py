#You are given a list of N integers and a value K. Print 1 if K exists in the given list of N integers, otherwise print −1.


x=(input())
y=(input())
N,K=map(int,x.split(" "))
l=[int(x) for x in y.split(" ")]
if K in l:
  print("1")
else:
  print("-1")
