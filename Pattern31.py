row_size = int(input("Enter row size :"))
for i in range(row_size):
    for j in range(i+1):
        if j%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print("")

i = 0
while i < row_size:
    j = 0
    while j < i+1:
        if j % 2 == 0:
            print("1",end="")
        else:
            print("0",end="")
        j = j+1
    print("")
    i = i+1 
