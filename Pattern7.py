'''OUTPUT for 3 rows:
123
123
123'''
row_size = int(input("Enter row size:"))
for i in range (row_size):
    for j in range(1,row_size+1):
        print(j,end="")
    print("")