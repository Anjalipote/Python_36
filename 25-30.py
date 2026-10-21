# Second Most Frequent character
text = input("enter a string:")
counts={}
for char in text:
    counts[char]=counts.get(char,0)+1
sorted_chars = sorted(counts, key=counts.get,reverse=True)
if len(sorted_chars)>1:
    print("Second Most frequrnt chatacter: ",sorted_chars[1])
else:
    print("No second most frequent character found.")        

# Caesar Cipher
text = input("enter a message: ")
shift = int(input(" enter shift value: "))
mode = input("enter mode (encrypt/decrypt): ").strip().lower()
if mode == "decrypt":
    shift = -shift
result = ""
for char in text:
    if char.isalpha():
        base = ord("A") if char.isupper() else ord("a")
        result += chr((ord(char)-base + shift)% 26 + base)
    else:
        result += char
print("result: ",result)        

#email validator
email = input("enter email address: ")
is_valid =True
if email.count("@") !=1:
    is_valid = False 
else:
    username,domain = email.split("@")
    if not username or not domain:
        is_valid = False
    elif "." not in domain:
        is_valid=False
    elif domain.startswith(".")or domain.endswith("."):
        is_valid=False
if is_valid:
    print("valid Email")
else:
    print("Invalid Email")

# word frequency dictionary
sentence = input("enter a sentence: ") 
word_counts ={}
for word in sentence.split():
    word_counts[word]= word_counts.get(word, 0)+1
print("Word Frequencies: ",word_counts)                           


#Sentence Reversal
Sentence=input("enter a sentence: ")
words = sentence.split()
revesed_sentence = " ".join(reversed(words))
print("Output: ",revesed_sentence)

#string Rotation
str1 = input("enter first string: ")
str2 = input("enter second string: ")
if len(str1)==len(str2) and len(str1)> 0 and str2 in (str1 + str2):
    print("Output:Yes")
else:
    print("output:No")    