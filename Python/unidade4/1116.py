#coding: utf-8
#INACABADO####################################
a = int(raw_input())
l = []
g = []
for e in range(a):
	x = raw_input().split()
	l.append(x)
for e in range(len(l)):
	y = l[e]
	for r in range(len(l)):
		h = l[e][r]
		g.append(h)
		
print g

