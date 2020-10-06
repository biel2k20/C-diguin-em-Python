#coding: utf-8

l = [1, 1, 1, 3, 3, 3, 5, 5, 5, 7, 7, 7, 9, 9, 9]
d = [7, 6, 5, 9, 8, 7, 11, 10, 9, 13, 12, 11, 15, 14, 13]

for x in range(len(l)):
	e = l[x]
	f = d[x]
	print 'I=%d J=%d' % (e, f)
