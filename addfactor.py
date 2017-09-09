#! usr/bin/python

num1 = int(input("Enter the number"))
#print(num1)
temp = 1


for i in range (2,num1):
	
	if (num1%i == 0) :
		temp  = temp + i 
		print("The Divisor except number itself is {}".format(i))
		#print(i)

print("The sum of divisors are:")
print(temp)
	
		