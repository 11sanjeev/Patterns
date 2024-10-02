'''OUTPUT for 4 rows:
1234
 234
  34
   4'''
row_size = int(input("Enter row size: "))

for i in range(row_size,0,-1):
    value = 1
    for j in range(row_size-i):
        print(" ",end="")
        value = value+1
    for k in range(i):
        print(value,end="")
        value = value + 1
    print("")


i = row_size
while i > 0:
    j = 0
    k = 0
    val = 1
    while j < row_size-i:
        print(" ",end="")
        j = j+1
        val = val+1
    while k < i:
        print(val,end="")
        k = k+1
        val = val+1
    print("")
    i = i-1