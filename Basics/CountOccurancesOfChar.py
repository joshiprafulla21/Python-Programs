#Write a program to accept string & a charter or another string and without using count method, count the occurances of second string into first string.
#!/usr/bin/python

def countOccurances(string,char):
	count=0
	for letter in string:
		if(letter==char):
			count=count+1
	print(count )
def main():
	string = input("Enter string :")
	char = input("Enter character :")
	countOccurances(string,char)

if __name__=="__main__":
	main()
