import hashlib
x=input("Enter your Password ")
y=hashlib.md5(x.encode())
print("the Hash is  ",y.hexdigest())
