#run length encoding
text = input("Enter a string: ")
if not text:
    print("Compressedoutput: ")
else:
    result=""
    current_char=text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = char
            count = 1
    result += current_char + str(count)
    print("Compressed output: ",result)        

#string Compression
text = input("enter a string: ")
if not text:
        print("result: ")
else:
     compressed = ""
     current_char = text[0] 
     count = 1
     for char in text[1:]:
          if char == current_char:
              count += 1
          else:
               compressed += current_char +str(count)    
               current_char = char
               count= 1
     compressed += current_char +str(count)
     result = compressed if len(compressed)<len(text)else text
     print("result: ",result)

     
