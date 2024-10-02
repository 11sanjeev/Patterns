'''OUTPUT for 5 rows:
1
22
333
4444
55555'''
row_size = int(input("Enter row size:"))
for i in range(1,row_size+1):
    for j in range(i):
        print(i,end="")
    print("")

i = 1
while i <= row_size:
    j = 1
    while j <= i:
        print(i,end="")
        j=j+1
    print("\n",end="")
    i = i+1