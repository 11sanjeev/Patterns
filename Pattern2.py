'''OUTPUT for 3 rows:
111
222
333'''
row_size = int(input("Ente row size:"))
for i in range(1,row_size+1):
    for j in range(row_size):
        print(i,end="")
    print("\n",end="")