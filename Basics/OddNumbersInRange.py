#Write a program to accept a range from user and print all odd numbers in the same. Hint: Don't use any arithmatic operator. #Accept 2 vaules. Use bitwise. Do validation for upper & lower numbers

#!/usr/bin/python

def printOddNumbers(iLower,iUpper):
	for x in range(iLower,iUpper,1):
		if(x & 1):
			print(x )

def main():
	iLower=input("Enter lower bound :")
	iUpper=input("Enter upper bound :")
	print("Odd numbers in given range :")
	printOddNumbers(iLower,iUpper)
if __name__=="__main__":
	main()
