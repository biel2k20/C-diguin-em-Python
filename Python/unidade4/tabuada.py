#coding: utf-8

a = int(raw_input())
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for e in l:
	tab = e * a
	print '%d x %d = %d' % (e, a, tab)
	e += 1
