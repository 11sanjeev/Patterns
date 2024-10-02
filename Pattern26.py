'''OUTPUT for 4 rows:
   1
  22
 333
4444'''
row_size = int(input("Enter row size: "))
for i in range(row_size):
    for j in range(1,row_size-i):
        print(" ",end="")
    for k in range(i+1):
        print(i+1,end="")
    print("")

i = 1
while i <= row_size:
    j = 0
    k = 0
    while j<row_size-i:
        print(" ",end="")
        j = j+1
    while k < i:
        print(i,end="")
        k = k+1
    print("")
    i = i+1