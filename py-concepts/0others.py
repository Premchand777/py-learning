
print(1 and 1, 1 and 0, True and True, True and False)
print(1 or 1, 1 or 0, True or True, True or False)
print(not True, not False)
print(True <= 1, False >= 1, 7 // 5, 6 ** 2)

# joining multiple lines without the issue of new line terminator 
if True and True \
    and 1 and 1 \
        and 'a' and 'b':
            print('ok')
            
# to write 2 statements in a single line
print('a');print('b')

from pprint import pprint
pprint({1: 1, 2: 2}, width=1)

str1 = 99
str2 = 'OK %o' 
print(str2 % 12)
print("Welcome %o" % str1)
print("Actual Number = %d" %15)
print("Exponential equivalent of the number = %e" %15)
print("Float of the number = %f" %15)
print("Hexadecimal equivalent of the number = %x" %15)

# Precision Width and Field Width:
# Field width is the width of the entire number and precision is the width towards the right. 
# One can alter these widths based on the requirements.
# The default Precision Width is set to 6.
print("%f" % 5.1234567890)
print("%.5f" % 5.1234567890)
print("%9.5f" % 5.1234567890)
print("%015.5f" % 5.1234567890)
# For proper alignment, a space can be left blank in the field width so that when a negative number is used, proper alignment is maintained.
print("% 9f" % 5.1234567890)
print("% 9f" % -5.1234567890)
# '+' sign can be returned at the beginning of a positive number by adding a + sign at the beginning of the field width.
print("%+9f" % 5.1234567890)
print("% 9f" % -5.1234567890)

print("%-9.4f" % 5.1234567890);print("%9.4f" % 5.1234567890)

# swapping variables
v1 = 1
v2 = 2
print(v1, v2)
v1, v2 = v2, v1
print(v1, v2)

# `global` variable
def _global():
    global g
    g = 'Ok'
    
def _global2():
    _global()
    print(g)

_global2()
print(g)

# single line if
n = 150
print(n)
#if n is greater than 500, n is multiplied by 7, otherwise n is divided by 7
result = n * 7 if n > 500 else n / 7
print(result)
