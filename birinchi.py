# list ichidagi tupleni listga o'girish
lst = [(1, 2), (2, 3), (5, 4), (5, 3)]
lst2 = []
for i in lst:
    j = list(i)
    lst2.append(j)
print(lst2)

