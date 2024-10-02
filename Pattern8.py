'''OUTPUT for 3 rows:
321
321
321'''
row_size = int(input("Enter row size:"))
for i in range(row_size):
    for j in range(row_size):
        print(row_size-j,end="")
    print("")
i = 0

while i<= row_size:
    j = 0
    while j<row_size:
        print(row_size-j,end="")
        j = j+1
    print("")
    i = i+1