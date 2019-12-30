list1 = [-3,-2,0,1,3,5,7,9]
# list1 = [1,2,3,4,6]
# list1 = [1,2,3]
# list1 = [-1,-2,-6]
list2 = []

for i in range(list1[0], list1[-1] + 20):
    if i > 0 and i not in list1:
        list2.append(i)

print(list2)
print(min(list2))