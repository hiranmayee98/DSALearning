'''
Chef went to a shop and buys a pens and b pencils. 
Each pen costs x units and each pencil costs y units. 
Now find what is the total amount Chef will spend to buy a pens and b pencils.
'''
try:
    string =input()
    l=[]
    for i in string:
        if i !=" ":
            l.append(int(i))
    a=l[0]
    b=l[1]
    x=l[2]
    y=l[3]
    print(a*x+b*y)
except EOFError as e : pass
