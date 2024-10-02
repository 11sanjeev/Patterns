'''OUTPUT for 4 rows:
1
21
321
4321'''
row_size = int(input("Enter the row size :"))
for i in range(1,row_size+1):
    for j in range(i):
        print(i-j,end="")
    print("")

i = 1
while i<=row_size:
    j = 0
    while j<i:
        print(i-j,end="")
        j = j+1
    print("")
    i = i+1