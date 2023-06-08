x=input( "Enter the string ")
new=''
for i in range(1,len(x)+1):
	new=new+x[-i]
print('the reversed String ',new)
