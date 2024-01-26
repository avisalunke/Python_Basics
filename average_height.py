students_height=input("input a list of students height").split()

for i in range (0,len(students_height)):
    students_height[i]=int(students_height[i])

print(students_height)
addition=0
n=0
for i in students_height:
    addition=addition+i
    n=n+1

print(addition)
print(addition/n)


total_height=sum(students_height)
total_num=len(students_height)
average=total_height/total_num
print(average)
