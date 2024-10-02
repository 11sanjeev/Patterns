'''OUTPUT for 3 rows
***
***
***'''
row_size = int(input("Enter number of rows for pattern :"))
for i in range (row_size):
    for j in range(row_size):
        print("*",end="")
    print("\n",end="")