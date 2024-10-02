'''OUTPUT for 4 rows:
****
 ***
  **
   *'''
row_size = int(input("Enter row size:"))
for i in range(row_size,0,-1):
    for k in range(row_size-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("")

i = row_size
while i>0:
    j = 0
    k = 0
    while j<row_size-i:
        print(" ",end="")
        j = j+1
    while k < i:
        print("*",end="")
        k = k+1
    print("")
    i = i-1