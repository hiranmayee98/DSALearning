#You are given a list of N integers and you need to reverse it and print the reversed list in a new line

i=int(input())
l=list(map(str,input().split(" ")))
l.reverse()
st=" "
print(st.join(l))
