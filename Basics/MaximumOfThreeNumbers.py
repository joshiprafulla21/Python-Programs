#Accept 3 numbers, and write OPTIMIZED program to find out maximum number. Print maximum numbers

#!/usr/bin/python

def getMaxOfThree(iNum1,iNum2,iNum3):
	if iNum1 > iNum2:
		iNum2 = iNum1
	if iNum2 > iNum3:
		return iNum2
	else:
		return iNum3

def main():
	iNum1=input("Enter 1st number :")
	iNum2=input("Enter 2nd number :")
	iNum3=input("Enter 3rd number :")
	print("Maximum of 3 numbers is :{}".format(getMaxOfThree(iNum1,iNum2,iNum3)))

if __name__=="__main__":
	main()
