x=int(input("Enter thr Number "))
count=0
for i in range(2, x):
	if(x%i)==0:
		count=count+1
if count==0:
	print("Prime " )
else:
	print("Composite ")
