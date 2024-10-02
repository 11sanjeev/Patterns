'''OUTPUT for 5 rows:
ABCDE
FGHIJ
KLMNO
PQRST
UVWXY'''

row_size = int(input("Enter row size: "))
ch = "A"
for i in range(row_size):
    for j in range(row_size):
        print(ch,end="")
        ch = chr(ord(ch)+1)
        
    print("")

ch = "A"
i = 0
while i < row_size:
    j =0
    while j < row_size:
        print(ch,end="")
        ch = chr(ord(ch)+1)
        j = j+1
    print("")
    i+=1
    