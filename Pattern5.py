'''OUTPUT for 5 rows
*****
****
***
**
* '''
row_size = int(input("Enter row size:"))
for i in range(row_size,0,-1):
    for j in range(i):
        print("*",end="")
    print("")