# DICTIONARY
# Py dictionaries are containers for unordered items/objects and are comma-separated set of key:value pairs
# Keys in dictionaries are unique and used for indexing so keys must be immutable data types only i.e string, number and tuple
# we can create an empty dictionary using curly brackets

# empty dict using curly brackets
dic = {}
print(8, dic == dict, type(dic) == dict)

# empty dict using dict contructor
dic = dict()
print(dic)

# through keyword args i.e kwargs
dic = dict(name='Prem', age=27)
print(dic)
print(dic.get('name'))

print(type(bool(dic.get('role1'))) == bool)
dic.update({ 'a': 100, 'b': 200 })
print(dic)
dic.update(c=300, d=400)
print(dic)

# int as key
dic = { 1: 100 }
print(dic)

# tuple as key
dic = { (1, 2): 3, 'a': 1 }
print(dic, dic.get((1, 2)))

dic = {}.setdefault(None)
if dic:
    print('dictionary has key value pairs')
else:
    print('Empty dictionary')
print(dic)

# to create a new dictionary with the same keys of another dic with a default val
dic = dict.fromkeys({ ('a', 'b'): 100 }, 0.)
print(dic)

# shallow copy
dic = { 'main': 100, 'sub': { 1: 10, 2: {20: 100} } }
print(dic)
dic2 = dict.copy(dic)
dic2['main'] = 100000
dic2['sub'][1] = 500
print(dic2, '\n', dic)



# create a new dict from two collections
dic = dict(zip(['a', 'b'], [10, 20, 30]))
print(dic)

# removes item by key provided
# or raises KeyError if default value is not provided
value = dic.pop('a', None)
print(value, dic)

dic.update(d = 12, a = 10, f = 23)
print(dic)

# removes last item and returns its key value in tuple
d = dic.popitem()
print(dic, d)

# dictionary comprehension method
print({ k: v for k, v in {1: 100, 2:200, 3: { 11: 110, 12: { 13: 130 } }}.items() })
print({ k: v for k, v in {1: 100, 2:200}.items() if k in [1, 3] })

# Counter module
from collections import Counter
colors = ['blue', 'red', 'green', 'yellow']
counter = Counter(colors)
print(counter, counter['orange'])
counter['white'] = counter['white'] + 1
counter['white'] += 1
print(counter)

# most common elements / repeated elements
counter.update({'yellow', 'yellow', 'white'})
print(counter.most_common())
# n most common elements
from time import time
print(time()/(1000*1000*64))
print(
    counter.most_common(2), 
    counter.most_common(2)[1].__getitem__(0), 
    counter.most_common(2)[1].__getitem__(1)
)
print(time()/(1000*1000*64))

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

