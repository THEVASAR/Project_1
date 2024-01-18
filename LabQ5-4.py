list1=[]
while True:
    element=input()
    if '-1' in element:
        break
    try:
        elements=list(map(int,element.split()))
    except ValueError:
        print('Error')
        exit()
   # elements=list(map(int,element.split(" ")))
    list1.append(elements)

a=len(list1[0])
for k in list1:
    if a!=len(k):
        print("Invalid Matrix")
        exit()

#print(list1)
list3=[] #First column of new mat
for j in range(len(list1[0])):
    list2=[] #First row of new mat 
    for i in list1:
        list2.append(i[j])
    list3.append(list2)

#print(list3)
for k in list3:
    for m in k:
        print(m,end=' ')
    print()
