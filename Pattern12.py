'''OUTPUT for 4 rows:
1
23
456
78910'''
row_size = int(input("Enter the size of row: "))
count = 1
for i in range(1,row_size+1):
    for j in range(i):
        print(count,end="")
        count = count+1
    print("")

i = 1
count = 1
while i <= row_size:
    j = 1 
    while j <= i:
        print(count,end="")
        count = count+1
        j = j+1
    print("")
    i = i + 1