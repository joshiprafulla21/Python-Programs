#Write a function which should be able to multiply 2 numbers,3 numbers,4 numbers or 5 numbers

#!/usr/bin/python
def mul(a,b=1,c=1,d=1,e=1):
	return (a*b*c*d*e)
def main():
	print("Multiplication :{}".format(mul(12,13)))
	print("Multiplication :{}".format(mul(12,13,4)))
	print("Multiplication :{}".format(mul(12,13,23,14)))
	print("Multiplication :{}".format(mul(12,13,3,45,11)))
if __name__=="__main__":
	main()
