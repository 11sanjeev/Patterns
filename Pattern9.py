'''OUTPUT for 3 rows:
123
456
789'''
row_size = int(input("Enter row size:"))
for i in range(row_size):
    for j in range(1,row_size+1):
        print(j+i*3,end="")
    print("")
i = 0
while i < row_size:
    j = 1
    while j <= row_size:
        print(j+i*3,end="")
        j = j+1
    print("")
    i = i+1