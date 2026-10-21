text=input("enter a string")
result=""
for ch in text:
    if ch != " ":
        result += ch
print("string without spaces: ",result)