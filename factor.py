x=int(input("enter the number "))
print("the factors of the number",x, "  are ")
for i in range(1,x+1):
	if(x%i==0):
		print(i)
