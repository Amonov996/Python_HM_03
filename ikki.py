# list ichidagi strga qaram qo'shish
son = int(input("Son kirit: "))
p = ['p','q']
q =[]
for i in range(son):
    for j in range(len(p)):
        q.append(p[j]+str(i+1))

print(q)





