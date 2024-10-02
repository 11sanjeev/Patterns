'''OUTPUT for 5 rows:
A
BC
CDE
DEFG
EFGHI'''
row_size = int(input("Enter row size: "))
i = 0 
while i < row_size:
    j = 0
    while j <= i:
        ch = chr(ord("A")+i+j)
        print(ch,end="")
        j = j+1
    print("")
    i = i+1

for i in range(row_size):
    for j in range(i+1):
        ch = chr(ord("A")+i+j)
        print(ch,end="")
    print("")