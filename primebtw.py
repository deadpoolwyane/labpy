x=int(input("enter the first number "))
n=int(input("Enter the second number "))
print("The prime numbers are ")
for i in range(x,n+1):
	count=0
	for j in range(2,i):
		if (i%j==0):
			count=count+1
	if count==0:
	        print(i,"\t")

 
