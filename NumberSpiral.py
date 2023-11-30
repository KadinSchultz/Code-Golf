# Problem: Number Spiral
# Link: https://code.golf/number-spiral#python
# Solutions characters: 258

# n = matrix length & width
# m = output matrix
# v = current value
# l = current location
# d = current direction
# s = string length

r=range
n,m,v,l,d=10,{},0,(0,0),(0,1)
def f():return(l[0]+d[0],l[1]+d[1])
while v<n*n:
    if set([-1,n]).intersection(f()) or f() in m:d=(d[1],d[0]*-1)
    m[l],l,v=str(v),f(),v+1
s=len(str(n*n))-1
for x in r(n):print(*[m[(x,y)].rjust(s,' ') for y in r(n)])
