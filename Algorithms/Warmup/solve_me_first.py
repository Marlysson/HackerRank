# -*- cofing:utf-8 -*-

# Challenge : https://www.hackerrank.com/challenges/solve-me-first

def solveMeFirst(a,b):
	tipos = (int,float)

	if all( [isinstance(a,tipos) , isinstance(b,tipos)] ):
		return a+b
	else:
		raise ValueError("Ha valores incorretos")

res = solveMeFirst(1,3)

print(res)