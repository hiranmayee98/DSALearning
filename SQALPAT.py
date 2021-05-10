'''
You're given a number N. Print the first N

lines of the below-given pattern.

1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
30 29 28 27 26

Input:
4

Sample Output 1:

1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
'''
c=0
d=5
N=int(input())
for i in range(1,N+1):
    st=" "
    for j in range(c+1,d+1):
        st=st+str(j)+" "
    if i%2==0:
        y=list(st.split(" "))
        y.reverse()
        str1=" "
        print(str1.join(y))
    else:
        print(st)
    c=d
    d=d+5
