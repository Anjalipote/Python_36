string=input("enter a string: ")
upp = low = 0
for ch in string:
    if ch.isupper():
        upp += 1
    elif ch.islower():
        low += 1
    else:
        print("incorrect string")
print("upper case letters are: ",upp) 
print("lower case letters are: ",low)               