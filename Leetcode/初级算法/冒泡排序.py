mylist = [3, 4, 2, 1]

for i in range(len(mylist) - 1):
    for j in range(len(mylist) - 1 - i):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

print(mylist)


