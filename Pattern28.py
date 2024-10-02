'''OUTPUT for 4 rows:
   1
  23
 456
78910'''
row_size = int(input("Enter row size:"))
value = 1
for i in range (row_size):
    for k in range (1,row_size-i):
        print(" ",end="")
    for j in range(i+1):
        print(value,end="")
        value = value+1
    print("")

i = 1
val = 1
while i <= row_size:
    j = 0
    k = 0
    while j < row_size-i:
        print(" ",end="")
        j = j+1
    while k < i:
        print(val,end="")
        val = val + 1
        k = k+1
    print("")
    i = i+1