'''OUTPUT for 4 rows:
4444
333
22
1'''
row_size = int(input("Enter row size:"))
for i in range (row_size,0,-1):
    for j in range(i):
        print(i,end="")
    print("")