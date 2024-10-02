'''OUTPUT for 5 rows:
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE'''



row_size = int(input("Enter row size: "))
for i in range(row_size):
    for j in range(row_size):
        ch = chr(ord("A")+j)
        print(ch,end="")
    print("")

i = 0
while i <row_size:
    j = 0
    while j < row_size:
        ch = chr(ord("A")+j)
        print(ch,end="")
        j = j+1

    print("")
    i = i+1