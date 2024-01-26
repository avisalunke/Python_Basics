Score_list=input("please enter scores").split()

for i in range(0,len(Score_list)):
    Score_list[i]=int(Score_list[i])

print(max(Score_list))


highest_score=0
for n in Score_list:
    if n>highest_score:
        highest_score=n
print(highest_score)