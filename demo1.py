# Python program to illustrate
# function with main
def getInteger():
    result = int(input("Enter integer: "))
    return result
def add():
    n1=int(input("give value1="))
    n2=int(input("give value2="))
    s1=n1+n2
    #print(s1)
    return s1
def whilecheck(a):
    count=a
    while(count <=5):
        count = count+1
        print("hi welcome")
def loopchek()
    # Iterating over a list
    print("List Iteration")
    l = ["geeks", "for", "geeks"]
    for i in l:
            print(i)
            
    # Iterating over a tuple (immutable)
    print("\nTuple Iteration")
    t = ("geeks", "for", "geeks")
    for i in t:
            print(i)
            
    # Iterating over a String
    print("\nString Iteration")	
    s = "Geeks"
    for i in s :
            print(i)
            
    # Iterating over dictionary
    print("\nDictionary Iteration")
    d = dict()
    d['xyz'] = 123
    d['abc'] = 345
    for i in d :
            print("%s %d" %(i, d[i]))

        
    
#res=add()
#print(res)
    
def main():
	print("Started")

	# calling the getInteger function and
	# storing its returned value in the output variable
	output = getInteger()	
	print(output)
	res=add()
	print(res)
	
	whilecheck(0)

	loopchek()
	


# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    main()
