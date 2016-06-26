# -*- cofing:utf-8 -*-

def solveMeFirst(a,b):
	tipos = (int,float)

	if all( [isinstance(a,tipos) , isinstance(b,tipos)] ):
		return a+b
	else:
		raise ValueError("Ha valores incorretos")

res = solveMeFirst(1,"a")

print(res)
