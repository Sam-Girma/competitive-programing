from math import ceil
n,m,a = map(int,input().split())
Width = ceil(n/a)
Height = ceil(m/a)
print(int(Width*Height))
