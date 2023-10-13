# =============== STRINGS ================

name = "K 'Prem'"
print(name,'\n')

# multi-line string
sentence = '''My name is premchand.
I live in Hyderabad.
I work in a Software Company.'''
print(sentence, '\n')

# string concatenation works only for str to str type
# string concatenation
print(name + '..... \n' + sentence, '\n')

# string concatenation with int
print(name + ' ' + str(27), '\n') # convert int to str, otherwise TypeError will be raised

# letter cases
print('premchand'.upper(), 'KODALI'.lower(), 'heLlo'.capitalize(), 'HELLO worLd'.casefold(), '\n')

# f-strings - f{} - f means forward (sting substitutions)
print(f'Welcome {name}.....')
print(f"WELCOME {name}, {sentence}", '\n')

n = 'KPC {}.'
n = n.format('SE') # doesn't modify original string. returns new modified string
print(n)
print("OK OKAY {}".format(name), "HAI {name}".format(name = 'PremChand..'), "HEY {n}".format(n = 'Chandu..'), '\n')

# str strip
print(' haha '.lstrip(), ' haha  '.rstrip(), ' haha '.strip())
print( ' haha  '.rstrip())
print(' haha '.strip(), '\n')

print(len(name), len(''), len(' '))
print('C' in 'PremChand', 'C' in 'Premchand', 'K' not in 'Prem', '#' * 7)
print('Premchand'[0], 'Premchand'[-1], 'Premchand'[0:len('Premchand')], 'Premchand'[4:9])
print('Premchand'[0:9:2]) # print every 2 char after starting latter
print(min('premchand'), max('premchand'))
print('PreMcHanD'.swapcase(), 'Premchand'.find('a'), 'abcdeeeeefg'.count('e'), '\n')
