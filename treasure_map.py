row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]

map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position=input("where do you want to put the treasure")

vertical=int(position[0])
horizontal=int(position[1])

selected_row=map[horizontal-1]
selected_row[vertical-1]="x"

print(f"{row1}\n{row2}\n{row3}")


# position=int(position)
# print(position)

# row_number=position%10
# index_number=int(position/10)-1

# if row_number==1:
#     row1[index_number]="x"
# if row_number==2:
#     row2[index_number]="x"
# if row_number==3:
#     row3[index_number]="x"

# print(f"{row1}\n{row2}\n{row3}")