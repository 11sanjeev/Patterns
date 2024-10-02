'''OUTPUT for 5 rows:
E
DE
CDE
BCDE
ABCDE'''
row_size = int(input("Enter the row size: "))
i = 1
while i <= row_size:
    j = 0
    while j < i:
        ch = chr(ord("A")+row_size-i+j)
        print(ch,end="")
        j = j+1
    print("")
    i = i+1

for i in range(1,row_size+1):
    for j in range(i):
        ch = chr(ord("A")+row_size-i+j)
        print(ch,end="")
    print("")