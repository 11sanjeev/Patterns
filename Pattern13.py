'''OUTPUT
1
23
345
4567
56789 '''

row_size = int(input("Enter the size of row:"))
for i in range(1,row_size+1):
    for j in range(i):
        print(j+i,end="")
    print("")

i = 1
while i <= row_size:
    j = 0
    while j < i:
        print(j+i,end="")
        j = j + 1
    print("")
    i = i+1