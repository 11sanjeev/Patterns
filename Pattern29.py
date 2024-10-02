'''OUTPUT for 4 rows:
   1
  121
 12321
1234321'''
row_size = int(input("Enter row size: "))
j = 0
for i in range(row_size):
    for k in range(1,row_size-i):
        print(" ",end="")
    for j in range(i+1):
        print(j+1,end="")
        j = j+1
    for l in range(i):
        print(j-l-1,end="")
    print("")

i = 1
while i<=row_size:
    j=0
    k=0
    l=1
    while j < row_size-i:
        print(" ",end="")
        j=j+1
    while k < i:
        print(k+1,end="")
        k=k+1
    while l < i:
        print(k-l,end="")
        l = l+1
    print("")
    i = i+1