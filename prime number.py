"""WAP TO ACCEPT A NUMBER n AND
   j. CHECK IF n IS PRIME
   k. GENERATE ALL PRIME NUMBERS TILL 'n'
   l. GENERATE FIRST n PRIME NUMBERS """

num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

def Prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)  
  
N=int(input("Enter N:"))  
i=2 
lst=[] 
while(1):  
    if(Prime(i)):  
        lst.append(i) 
        if(len(lst)==N): 
            break 
    i+=1 
print("First "+str(N)+" Prime numbers are:",end="") 
print(*lst)
