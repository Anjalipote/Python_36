student=input("enter a name: ")
per=int(input("enter a marks of student: "))
if(per>=90):
    print(student,"has excellent marks")
elif(per>=80):
    print(student,"has very good marks")     
elif(per>=70):
     print(student,"has good marks")
elif(per>=60):
     print(student,"has Average marks")
else:
     print(student,"has poor marks")     