'''OUTPUT for 5 rows:
1234554321
1234**4321
123****321
12******21
1********1'''
row_size = int(input("Enter row size: "))
# i = 0
# while i < row_size:
#     j = 1
#     k = 1
#     l = 1
#     s = row_size-i
#     while j<= row_size-i:
#         print(j,end="")
#         j = j+1
#     while k <= i:
#         print("*",end="")
#         k = k+1
#     while l <=i:
#         print("*",end="")
#         l = l+1
#     while s > 0:
#         print(s,end="")
#         s = s-1
#     print("")
#     i = i+1

for i in range(row_size):
    for j in range(row_size-i):
        print(j+1,end="")
    for k in range(i):
        print("*",end="")
    for l in range(i):
        print("*",end="")
    for s in range(row_size-i,0,-1):
        print(s,end="")
    print("")