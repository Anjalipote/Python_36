text=input("enter a string")
target = input("enter the character to count:")
count=0
for ch in text:
    if ch == target:
        count += 1
print("frequency: ",count)        