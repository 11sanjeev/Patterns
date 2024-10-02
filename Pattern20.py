'''OUTPUT for 5 rows:
A
BC
DEF
GHIJ
KLMNO'''
row_size = int(input("Enter the row size: "))
ch ="A"
i = 0
while i<row_size:
    j = 0
    while j <= i:
        print(ch,end="")
        ch = chr(ord(ch)+1)
        j = j+1
    print("")
    i = i+1

ch = "A"
for i in range(row_size):
    for j in range(row_size):
        print(ch,end="")
        ch = chr(ord(ch)+1)
    print("")