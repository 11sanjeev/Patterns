'''OUTPUT for 3 rows:
1
22
333'''
row_size = int(input("Enter row size:"))
for i in range(1,row_size+1):
    for j in range(i):
        print(i,end="")
    print("")