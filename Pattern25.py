'''OUTPUT for 4 rows:
1111
 222
  33
   4'''
row_size = int(input("Enter row size:"))
value = 1
for i in range(row_size,0,-1):
    for j in range(row_size-i):
        print(" ",end="")
    for k in range(i):
        print(value,end="")
    value = value+1
    print("")

i = row_size
val = 1
while i > 0:
    j = 0
    k = 0
    while j < row_size-i:
        print(" ",end="")
        j = j+1
    while k < i:
        print(val,end="")
        k = k+1
    val = val+1    
    print("")
    i = i-1