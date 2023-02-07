# listda o'sishitartibida kelgan sonlarni hisoblash

lst = [1,2,3,4,1,4,5,4,8,9,-1,3,5]
count =0
for i in range(len(lst)-1):
    if lst[i-1]>lst[i] and lst[i] < lst[i+1]:
        count+=1
print(count)