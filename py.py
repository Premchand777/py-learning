

# a, b, c, d, e, f = 0b101, 0B110, 0o11001, 0O1111, 0xAFC, 0XAAB
# print(a, b, c, d, e, f)
# print(52e5, 3.4e-3)

# print(1.79e+308, 1.79e+309)

# print(5e-324, 5e-325)

# a = 2j
# b = 3 + 4j
# print(a, b, a.real, b.real, a.imag, b.imag, 0.2+0.1)

# from decimal import Decimal
# print(Decimal('0.2')+Decimal('0.1'), Decimal(), 0, Decimal('2.6'))

# print(11 / 5, 11 // 5, 11 % 5)

# print(bin(5), oct(50), hex(123))

# unit_price = 123543.7832
# qty = 30
# print( f"subtotal: {qty * unit_price}" )
# print( f"subtotal: {qty * unit_price:,.5f}" )

# # formatting percent numbers
# print(f"sales tax rate: {0.065:.2%}")
# print(f"sales tax rate: {0.95:.2%}")

# # multi line format strings
# print(f"""
# subtotal: {qty * unit_price:,.2f},
# tax_rate: {0.022:.2%}
# """)

# print(f'''test
#       {1000000000000:,.2f}
#       ''', 11 // 5) # 11 // 5 = 2.2 => 2

# print('C' in 'PremChand')

# final_outpout2 = f"""
# Subtotal  : ${18827.234:>10,.2f}
# Sales Tax : ${2343.345:<100,.2f}
# Total     : ${2342244.3432:^20,.2f}"""
# print(final_outpout2)

# print(not 10 > 0 and 10 < 100)

# from time import time

# print(time())
# _sum = 0
# lst = [1, 2, 3, 4, 5] # 31
# for i, e in enumerate(lst):
#     _sum += e
# print(_sum)
# print(time())


# print(time())
# sum2 = 0
# lst2 = [1, 2, 3, 4, 5] # 24
# for i in range(0, len(lst2)):
#     sum2 += lst2[i]
# print(sum2)
# print(time())

# print(['1', '2'] == ['1', '2'])


# logical operators
# without 0 on either side
# print(-9 and 9) # right element
# print(9 and -9) # right element
# print(1 and 1) # right element
# print(1 and 5) # right element
# print(5 and 2) # right element
# print(-5 and -10) # right element
# print(-10 and -5) # right element

# # with 0 on either side
# print(-9 and 0) # right element
# print(0 and -9) # right element
# print(1 and 0) # right element
# print(0 and 5) # right element
# print(5 and 2) # right element
# print(0 and -10) # right element
# print(-10 and -0) # right element

# boolean
# print(True and True)
# print(True and False)
# # boolean and str
# print(type(True and 'True'))
# print(type('True' and True))
# # boolean and ''
# print(type('' and True))
# print(type(True and ''), True and '')
# # boolean False and ''
# print(False and '') 
# print('' and False) 
# # boolean False and 0
# print(False and 0) 
# print(0 and False) 
# print(False and -10, '\n')

# # or
# print(1 or 1)
# print(1 or 3)
# print(5 or 30)
# print(1 or -3)
# print(-1 or 3)
# print(0 or 2)
# print(2 or 0)
# print(0 or -2)
# print(-2 or 0)

# print(True < 1, bool(1))
# print(True > 1, bool(1))
# print(True == 1, bool(1))
# print(True == 'st', bool('st'))
# print(True == '', bool(''))
# print(False == 'st', bool('st'))
# print(False == '', bool(''))

# joining multiple lines 
# if 1 and 1 \
#     and 'true' and 'true' \
#         and True and True \
#             and True and True:
#     print('HELLO')

# # multiple lines into single line
# print('first');print('second');print('third');var2 = 1
# print(var2)

# name = 'Premchand'
# print("Welcome %s" % name)

# n = 10
# print('Number in octal format = %o' % n) # 12
# print('Number in hex format = %x' % n) #a
# n = 500
# print('Number in binary format = %d' % n) # 500
# n = 64
# print('Number in exponential format = %e' % n) # 6.400000e+01
# print('Number in float format = %f' % n) # 64.000000 default 6 floating points
# print('Number in float format = %.2f' % n) # 64.00

# # Field Width and Precision Width
# # 100.2456854356
# print('%01.3f' % 200)
# print('%02.3f' % 200)
# print('%03.3f' % 200)
# print('%06.3f' % 200)
# print('%07.3f' % 200)
# print('%8.3f' % 200)
# print('%08.3f' % 200)
# print('%010.3f' % 200)
# print('% f' % 200)
# print('% f' % 5.12345)
# print('%f' % -5.12345)

# print('% +f' % 5.12345)
# print('%f' % -5.12345)

# # variables swapping
# a, b = 100, 200
# print(a, b)
# a, b = b, a
# print(a, b, '\n')

# global keyword
# g1 = 50
# def f1(): 
#     global v1
#     v1 = 100
#     print(v1)
#     print(g1)
    
# print(f1())
# print(v1)


# single line if statement
# if not True:
#     print('TRUE')
# else:
#     print('FALSE')
# print('\n')

# print('TRUE') if not True else print('FALSE')

# print(100 / 5) if 100 > 5 else print(5 / 100)






# Dictionary
# Py dictionaries are containers for unordered items/objects and are comma-separated set of key:value pairs
# Keys in dictionaries are unique and used for indexing so keys must be immutable data types only i.e string, number and tuple
# we can create an empty dictionary using curly brackets

# dic = {}
# print(209, dic == dict, type(dic) == dict)

# book = dict()
# print(212, type(book) == dict)

# book = dict(name='software', price=500)
# print(book)

# print(book.get('name')) # key present -> returns value i.e software
# print(book.get('name2')) # No key present -> returns None
# print(book['name'])
# # print(book['n']) # throws KeyError as key is not present


# print(bool(book.get('name')) == True)

# if bool(book.get('name2')):
#     print('KEY EXISTING')
# else:
#     print('KEY NOT EXISTING')

# # update a dict
# # book.update(pages=250, author='Prem')
# # print(book)

# book['pages'] = 250
# book['author'] = 'Prem'

# print(book)

# cars = {}
# cars.setdefault('carName', 'audi')
# print(cars)
# cars.update(n=100, m=200)
# cars.update({1: 'k'})
# print(cars)

# names = {}
# names.setdefault(100)
# print(names)
# if names:
#     print('not empty')
# else:
#     print('empty')
    
# # to create a new dict from another dict with a default value
# newDict = dict.fromkeys({'name': 'Audi'}, { 1: 'Hi', 2: { 3: 'Hello'}})
# print(newDict)

# newDict2 = newDict
# print(newDict2)

# newDict2['name'][1] = 'Bye'
# print(newDict2)
# print(newDict, '\n\n\n\n\n')

# # shallow copy 
# # main level key values changes won't be reflected in original object but key values changes in nested
# # object(s) will be reflected in original object

# newDict3 = dict.copy(newDict)
# # print(newDict)
# # print(newDict3)
# newDict3['name'][2][3] = 'Bye'
# print(newDict3)
# print(newDict, '\n')

# newDict3['name'] = 'Premchand'
# print(newDict3)
# print(newDict, '\n\n\n')


# # deep copy
# # keys values changes won't be reflected in original object
# import copy
# newDict4 = copy.deepcopy(newDict)
# print(newDict)
# print(newDict4)

# newDict4['name'][2][3] = 'Hello'
# print(newDict4)
# print(newDict, '\n')

# newDict4['name'] = {}
# print(newDict4)
# print(newDict)


# create a new dictionary from two collections using dict class constructor and zip
d1 = dict(zip([1, 2], [3, 4])) # (1, 3), (2, 4)
# zip([1, 2, 3], [4, 5, 6]) # (1, 4), (2, 5), (3, 6)
print(dict(zip([1, 2, 3], [4, 5, 6])))
print(d1)

# zip(['a', 'b', 'c'], [100, 200, 300]) # ('a', 100), ('b', 200), ('c', 300)

# dict(('a', 100), ('b', 200), ('c', 300)) # { 'a': 100, 'b': 200, 'c': 300 }
print([tp for tp in zip([1, 2, 3, 4, 5], [100, 2000, 300, 400, 500], ['a', 'b', 'c', 'd', 'e'])])

# remove a key value pair from dictionary using pop
d1 = { 'a': 100, 'b': 200 }
print(d1.pop('ba', None))
print(d1)

#  remove a key value pair from dictionary using popitem
d2 = { 'a': 100, 'b': 200 }
print(d2.popitem())
print(d2)

# dictionary comprehension method
lst = { 1: 10, 2: 20, 3: 30 }
lst2 = {}
lst2.update(lst)
for k in lst:
    print(k)
    lst2.update({ k: lst[k] })

print(lst2)

# dictionary comprehension method - expression `for` variables part `in` collection/iterableObject condition
d4 = { k: v for k, v in lst.items() if v != 10 }
print(d4)


# Counter class from collections module
from collections import Counter
colors = ['green', 'red', 'blue', 'blue', 'green', 'orange', 'green']

counter = Counter(colors)
print(counter)

print(counter['green'])

# counter.update('vioooolett')
counter.update({ 'green', 'white', 'black'})
print(counter)

nums = [1,2,3,1,1,1,2,3,4,4,4,5,6,7,7, 9,9,9,9,9, 5,5,5,5,5,2,2,2,2]
counter = Counter(nums)
print(counter)
print(counter[7])

counter.update([8,8])
print(counter)
print(counter.most_common())
print(counter.most_common(3)[0][1])


print(None == True)
print(None == False)
var = None
if var:
    print('Data exists')
else:
    print('No data')
    
#  iterate over dictionary
colorDict = { 'Green': 100, 'White': 200, 'Yellow': 300 }
for colorKey, code in colorDict.items():
    print(f'{colorKey}\'s color code is: {code}')


# sorting the dictionary based on letters
letters = {
    'bac': 1,
    'bab': 2,
    'afh': 3,
    'afg': 4
}
for key in sorted(letters):
    print('%s: %s' % (key, letters[key])) # %s -> used as a string placeholder, % -> used to format the string
        #  1^  2^      1^       2^
        #   |   |_______|________|
        #   |___________|
        
# sorting the disctionary based on numbers
nums = {
    2: 1,
    44: 28,
    1: 3,
    3: 4,
    4: 5
}
for key in sorted(nums, reverse=True):
    print('%s: %s' % (key, nums[key]))
# max and min values from dictionary
keyMax = max(nums.keys(), key=(lambda k: nums[k])) # lambda is an anonymous function
print(keyMax, nums[keyMax])
keyMin = min(nums.keys(), key=(lambda key: nums[key]))
print(keyMin, nums[keyMin])

# concatenating dictionaries
dic1 = { 1: 'a', 2: 'b' }
dic2 = { 3: 'c', 4: 'd' }
dic3 = { 5: 'e', 6: 'f' }
dic4 = {}
dic5 = {}
from time import time
print(time())
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
print(time())
print(time())
for d in (dic1, dic2, dic3): dic5.update(d)
print(dic5)
print(time())

fruits = {"mango": 2, "orange": 6}

# Use len() function to get the length of the dictionary
print("Length:", len(fruits))


ns = [9]
ns.append(1)
print(ns)
print([1] + [2])
nums = [1,2]
nums[len(nums):] = [3]
print(nums)

for x in set('abc'):
    print(x*3)
    
print(all([1,2,3]))
print(all([1,2,0]))
print(all([1,2,None]))

for a in range(0,10,2):
    print(a)
print(all(a % 2==0 for a in range(0,10,2)))
print(a for a in range(0,10,2))



















