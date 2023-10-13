# cars = ['audi', 'benz', 'toyota',3]
# print(cars[0], cars[1], cars[2].title())
# cars.reverse()
# print(cars)
# cars.append(12)
# print(cars)
# cars.append('prem')
# cars.append('prem')
# print(cars)

# # below gives type error cannot compare str and int because list contains str and int
# # cars.sort()
# # print(cars)

# # removes first occurrence
# cars.remove('prem')
# print(cars)

# # append only for single element add to the end of the list, 
# # but extend is for multiple elements add to end of list
# cars.extend(['ok', 'hi'])
# print(cars)
# cars.extend({'ok2', 'hi2'})
# print(cars)
# cars.extend(('ok3', 'hi3'))
# print(cars)
# cars.extend({'ok4': 111, 'hi4': 222})
# print(cars)

# # it can give index error if list is empty or index out of range
# # to remove an element by index, default last element removal
# cars.pop()
# print(cars)
# cars.pop(1)
# print(cars)

# # to remove all elements in the list
# cars.clear()
# print(cars)

# # shallow copy 
# cars = ['Audi', 'Mercedes', 'Rolls Royes', {1: 2}, {2: { 3: {4: {'a': 'prem', 'b': [{1:2}]}}}}]
# dic = {1: 2, 3: {3: 2, 4: {1: {4:[{2:1}]}}}}
# dic2 = dic.copy()
# print(dic2)
# carsCopy = cars.copy()
# print(cars)
# print(carsCopy)
# dic2[1] = 2_000
# dic2[3][1] = 20_000
# print(51, dic, dic2)
# carsCopy[2] = 'hyundai'
# print(53, cars, carsCopy)
# carsCopy[3][1] = 300_000
# print(55, cars, carsCopy)

# print([1, 2, 3, 3, 4, 5, 3, 5].count(5))

# vv = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'g', 'i']
# # vv.reverse()
# print(vv)

# # it can raise value error if value is not present
# # index of a value and or within a range
# print(vv.index('b')) # 1
# print(vv.index('g', 4, 8))
# print(vv.index('g', 5, 8))
# print(vv.index('g', 6, 8))

# # magic or dunder methods
# print(cars.__contains__('Audi'))
# print(cars.__len__())

# # insert in between
# names = ['I', 'Premchand']
# print(names)
# names.insert(1, 'am')
# print(names)


# singleTypeList = [1, 2, 3, 4]
# print(singleTypeList)
# # below highlightes type error at 'str' but runs and prints the list
# # singleTypeList.append('str')
# # print(singleTypeList)

# # ls1 = [1,2,3,3]
# # print(ls1[1])

# # # last element
# # print(ls1[-1])

# # print(len(ls1))

# # # append to last 
# # ls1.append(1)

# # # insert anywhere
# # ls1.insert(1, 'ok')

# # # delete last element
# # ls1.pop()

# # # delete anywhere
# # del ls1[-1]

# # # delete a value
# # ls1.remove(3)
# # print(ls1)

# # ls2 = [1,2,3,3,1,5]

# # ls2.remove(3)

# # print(ls2)
# ls2 =[1,2,3,4,5,6,8]
# for i in ls2:
#     print(i)

# nums = [1, 2, 3, 4, 5]
# del nums[3]
# print(nums.sort())
# nums2 = sorted(nums, reverse=True)
# print(nums)
# print(nums2)
# print(len(nums))

# print([1, 2, 3, 4, 5, 6, 7, 8][1:4])

# print([1, 2, 3, 4, 5, 6, 7, 8][1:-1])

# print([1, 2, 3, 4, 5, 6, 7, 8][6:])

# print([1, 2, 3, 4, 5, 6, 7, 8][:4])

print(range(10))
for value in range(10):
    print(value)
    
print(range(10, 20))
for value in range(10, 20):
    print(value)
    
# even numbers
print(range(1, 20, 2))
for value in range(0, 20, 2):
    print(value)
    
# odd numbers
print(range(1, 11, 2))
for value in range(1, 20, 2):
    print(value)
    
# sum function and list
print(sum([1, 2, 3, 4, 5])) #15
# max function and list
print(max([1, 2, 3, 4, 5])) #5
# min function and list
print(min([1, 2, 3, 4, 5])) #1


# multi dimensional list
matrix = [[1, 2], [3, 4], [5, 6]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

for i, v in enumerate(matrix):
    for ii, vv in enumerate(v):
        # print(matrix[i][ii], end=' ')
        print(vv, end=' ')
    print()
    
# reversing list using :
a = [1, 2, 3, 4, 5]
print(a[::-1])

a = [1, 2, 3, 6, 4, 5]
print(a[::-1])

a = [5, 4, 3, 2, 1]
print(a[::-1])

a = ['a', 'b', 'c', 'f', 'g']
print(a[::-1])


# import itertools

num = [1,2,3,4,2,2,5]
cars = ['toyota','audi','maserati','ford','prem']
values = [100,200,300,400,500]

for (a,b,c) in zip(num, cars, values, strict=False):
    print(a,b,c)
    
print(198, [(a,b,c) for a,b,c in zip(num, cars, values)])

# can use bool and count combination for element existence check
print(num.count(2), bool(num.count(14)))
print(num.__getitem__(1))
print(5 in num)

# bool(num.index(1) <- don't use this for element existence check because index can be 0 so bool returns false
# also it raises an error if value is not present
print(num.index(1), bool(num.index(1))) 


mylist = ['a','a','a','b','c','c','d','e']
print (mylist)

print(set(mylist))
print(max(set(mylist), key=mylist.count))

nums = [1,1,1,1,1,1,2,3,4,5,5,5,5,5,5,5,5,4,4,4,4,2,2,2,2]
print(max(nums, key=nums.count), nums.count)


# nested list comprehensions 
vectors = [[1,2,3],[4,5,6],[7,8,9]]
L = []
for list in vectors:
    for number in list:
        L.append(number)
print (L)
print([n for list in vectors for n in list])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([i for row in matrix for i in row])
print([[row[i] for row in matrix] for i in [0,1,2]])
print([[row[i] for row in matrix] for i in range(3)])

x = 0
while x < 5:
     print(x)
     x += 1

for x in range(7):
    if (x == 3 or x==6):
        continue
    print(x)
    
print({1: 10, 1: 12})
print((1, 12, 12))

