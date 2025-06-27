lst=[]
for i in range(6):
    son=int(input(f"{i+1}-son: "))
    lst.append(son)
print(lst)
max_son=0
for i in lst:
    if i > max_son:
        max_son=i
print(max_son)
    