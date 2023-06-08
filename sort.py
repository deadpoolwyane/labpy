def sort(a):
	for i in range(len(a)):
		for j in range(len(a)-1):
			if a[j]>a[j+1]:
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
	return a
def printf(a):
	for i in a:
		print(i)
a=eval(input("Enter the number "))
print(type(a))
a=list(a)
x= sort(a)
printf(x)
