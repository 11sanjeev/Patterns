'''OUTPUT for 4 rows:
*
**
***
****'''
row_size = int(input("Enter row size:"))
for i in range(1,row_size+1):
    for j in range(i):
        print("*",end="")
    print("\n",end="")

i = 1
while i <= row_size:
    j = 0
    while j<i:
        print("*",end="")
        j = j+1
    print("\n",end="")
    i = i+1