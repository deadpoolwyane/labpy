def fact(n):
	if n==1 or n==0:
		return 1 
	else:
		return n*fact(n-1)
x=int(input("enter the n "))
r=int(input("enter the r "))
print('thesumis',fact(x)/(fact(r)*fact(x-r)))
