x=input("enter a string")
y=input("enter a character you want to replace ")
z=input("enter a character with replace")
result=""
for ch in x:
    if(ch==y):
      result += z
    else:
      result += ch 
print(result)        

