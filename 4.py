# Problem 4  _______(Alone Function)_______

def aloneFunc (list1):
    for i in range(1,len(list1)-1):
        if list1[i]==list1[i-1] or list1[i]==list1[i+1]:
            continue
        elif list1[i+1]>=list1[i-1]:
                list1[i]=list1[i+1]
        else:
                list1[i]=list1[i-1]
    return list1

list5=[1, 1, 2, 3, ]
print(aloneFunc(list5))

print(aloneFunc)