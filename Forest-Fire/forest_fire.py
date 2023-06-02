n, x = map(int, input().split())
p = list(int(num) for num in input().strip().split())[:n]

d = 0

p.sort()

c=len(p)-x

if c<=0:
	c=0
else:
	if p[c] == p[c-1]:
		d=-1

if d==0:
	print(p[c])
else:
	print(d)