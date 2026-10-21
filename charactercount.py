#conting each character
text=input("enter a string")
counts={}
for char in text:
    counts[char]=counts.get(char, 0)+1
for char,count in counts.items():
    print(f"'{char}':{count}")

#Anagram check
str1=input("enter a string")
str2=input("enter a string")
if sorted(str1) == sorted(str2):
    print("strings are Anagram")
else:
    print("Not Anagram")

#remove duplicate character
text = input("enter a string: ")
result = "".join(dict.fromkeys(text))
print("result: ",result)

#Substirng Search
main_str=input("enter main string: ")
sub_str = input("enter a substring: ")
if sub_str in main_str:
    print("Substring exists in main string.")
else:
    print("Substring does not exist.")    

#count occurance of a word
a=input("enter a sentence: ")
target_word =input("enter word to count: ")
print("Occurance: ",a.split().count(target_word))

#password Validator
password=input("enter a password: ")
is_valid=(
len(password) >= 8 and 
any (c.isupper() for c in password)and
any(c.islower() for c in password)and
any(c.isdigit() for c in password)and
any(not c.isalnum() for c in password)
)
print("valid Password" if is_valid else "Invalid Password")
