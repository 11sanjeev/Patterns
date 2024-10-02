'''OUTPUT: for 4 rows:
   *
  **
 ***
****'''
row_size = int(input("Enter row size:"))

for i in range(row_size):
    for k in range(1,row_size-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print("")

i = 1
while i <= row_size:
    j = 0
    k = 0
    while j < row_size-i:
        print(" ",end="")
        j= j+1
    while k < i:
        print("*",end="")
        k= k+1
    print("")
    i = i+1