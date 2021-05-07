'''
Chef went to a shop and buys a pens and b pencils. 
Each pen costs x units and each pencil costs y units. 
Now find what is the total amount Chef will spend to buy a pens and b pencils.
'''
try:
    string =input()
    a,b,x,y=map(int,string.split(" "))
    print(a*x+b*y)
except EOFError as e : pass
