'''OUTPUT for 5 rows:
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE'''
row_size = int(input("Enter row size:"))
for i in range(row_size):
    for j in range(row_size):
        ch = chr(ord('A')+i)
        #-> ord() convert symbol to its ASCII value like A = 65
        #-> chr() convert character from ASCII value to symbol like 65 = A
        print(ch,end="")
        
    print("")

i = 0
while i<row_size:
    j=0
    while j<row_size:
        ch = chr(ord('A')+i)
        print(ch,end="")
        j=j+1
    print("")
    i = i+1