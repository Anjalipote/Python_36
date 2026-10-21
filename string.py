#String length
s=input("enter a string: ")
count=0
for i in s:
    count +=1
print("length of string",s,"is",count)

#character count
s= input("enter a string: ")
vow=con=dig=space=sp=0
for ch in s:
    if ch in "aeiou":
        vow +=1
    elif ch.isalpha():
        con += 1
    elif ch.isdigit():
        dig +=1
    elif (ch == " "):
        space += 1
    else:
        sp += 1
print("vowels are",vow) 
print("consonants are ",con) 
print("digits are",dig) 
print("spaces are",space) 
print("special chatacter",sp)                 