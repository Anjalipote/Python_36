#print natural number
n=int(input("enter n number "))
i=1
while i<=n:
    print(i, end=" ")
    i += 1

#print even numbers
n=int(input("enter n:"))
i=2
while i<=n:
    print(i, end =" ")
    i += 2

#print odd numbers
n=int(input("enter n:"))
i=1
while i<=n:
    print(i,end=" ")
    i += 2

#sum of natural numbers
n=int(input("enter n: "))
i=1
sum=0
while i<= n:
    sum += i
    i += 1
print("sum =", sum)

#sum of odd numbers
n=int(input("enter n: "))
i = 1
sum = 0
while i<= n:
    sum += i
    i += 2
    print("sum of odd numbers =",sum)


#print sum of even numbers
n=int(input("enter n: "))
i = 2
sum = 0
while i<= n:
    sum += i
    i += 2
    print("sum of even numbers =",sum)

#print numbers in reverse order
n = int(input("enter n: "))
while n>= 1:
    print(n, end=" ")
    n -= 1

#print fibonacci series    
n=int(input("enter number of terms: "))
a = 0
b = 1
i = 1
while i<= n:
    print(a,end=" ")
    c = a + b
    a = b
    b = c 
    i += 1

#print factorial of number
n= int(input(" Enter a number: "))
fact = 1
i=1
while i <= n:
    fact *= i
    i += 1
print("factorial = ",fact)        

n=int(input("enter a number"))
for i in range (1,7):
    print(i)