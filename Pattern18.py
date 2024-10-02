'''OUTPUT for 3 rows:
ABC
BCD
CDE'''
row_size = int(input("Enter row size: "))
for i in range(row_size):
    for j in range(row_size):
        ch = chr(ord("A")+j+i)
        print(ch,end="")
    print("")

i = 0
while i<row_size:
    j = 0
    while j < row_size:
        ch = chr(ord("A")+j+i)
        print(ch,end="")
        j = j+1
    print("")
    i = i+1