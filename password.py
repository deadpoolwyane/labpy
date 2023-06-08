x=input("Enter the password ")
special=0
lower=0
upper=0
digit=0
for i in x:
	if i in "@#$%^&*()_+|=\ ":
		special=1
	elif i.isupper()==True:
		lower=1
	elif   i.islower()==True:
		upper=1
	elif  i.isdigit()==True:
		digit=1
sum=special+lower+upper+digit
if sum==4 and len(x)>8:
	print("Strong ")
elif sum==2 and len(x)>6:
	print("Moderate")
else:
	print("weak")
