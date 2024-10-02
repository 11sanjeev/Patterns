'''OUTPUT for 5 rows:
A
BB
CCC
DDDD
EEEEE'''
row_size = int(input("Enter row size: "))
ch = "A"
for i in range(1,row_size+1):
    for j in range(i):
        print(ch,end="")
    ch = chr(ord(ch)+1)
    print("")

i = 1
while i <=row_size:
    j = 0
    while j<i:
        print(ch,end="")
        j = j+1
    ch = chr(ord(ch)+1)
    print("")
    i = i+1
# Second approch
for i in range(row_size):   
    for j in range(i+1):
        ch = 'A'
        ch = chr(ord(ch)+i)
        print(ch,end="")     
    print("")

i = 0
while i<row_size:
    j = 0
    while j<=i:
        ch  = "A"
        ch = chr(ord(ch)+i)
        print(ch,end="")
        j = j+1
    print("")
    i = i+1
