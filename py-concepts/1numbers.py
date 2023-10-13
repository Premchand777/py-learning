# ============== NUMBERS ===============

# underscores in numbers
num1 = 1_00_000 # py version 3.6+
print(num1, '\n')

# / always returns float
print(6 / 2, 1 + 5.0, 2 ** 7.0, '\n')

# BMDAS
#       4A   1B   5S  2M  3D
print(5 + (1 + 7) - 2 * 6 / 2)

# multiple variables assignments
x = 1
y = 1
z = 1
print(x, y, z)
a, b, c = 2, 2, 2
# a, b, c = 2 --> won't work TypeError will be raised
# ya = 40, yb = 50 --> won't work Invalid syntax error will be raised
print(a, b, c)
xa, xb, xc = 10, 20, 30
print(xa, xb, xc, '\n')
print(int(True), int(False)) # to convert True to 1, False to 0



# binaryStrings = ["010", "100", "011", "101", "001", "110", "111", "100", "110", "010", "111"]
# dec = []

# for binary in binaryStrings:
#     dec.append(int(binary, 2))
# dec.sort(reverse=True)

# print(list(set(dec)))

# print('hello {}, how are you!'.format(input("name: ")))

# x = 10
# y = -10
# z = 32355242
# print(x, y, z)

# # Binary - base 2 , 0b or 0B
# # Octal - base 8 , 0o or 0O
# # Hex - base 16 , 0x or 0X
# print(0b1010, 0o1010, 0x1010, 0xAF)

# # floating point numbers
# print(10.2, -10.2, 1.2343)

# # scientific notation
# print(52e5, 3.4e-3)

# # maximum floating points 1.8 x 10**308
# print(1.79e+308, 1.79e+309)

# # minimum floating points 5.0 x 10**-324
# print(5e-324, 5e-325)

# #  complex numbers = real_part + imaginary_part
# a = 2j
# b = 3 + 4j
# print(a, b, a.real, b.real, a.imag, b.imag, 0.2+0.1)

# # integers are whole numbers
# # py calls any number with a decimal point and a float so carefully deal with float numbers. ex: 0.2 + 0.1 is not 0.3 its 0.30000000000000004

# # use modulus % for reminder results

# # Floor division
# print(11 / 5, 11 // 5) # cutting off floating points

# # Py Built in Functions for Numbers

# print(abs(-45))

# print(round(1.23454, 2))

# x = 148
# y = 3.1902664856
# z = 234.678
# a = -999.999
# print(abs(a))
# print(int(a))
# print(int(abs(a)))
# print(round(y, 4))
# print(bin(x), oct(x), hex(x))
# print(max(x, a, y, z))
# print(min(x, a, y, z))

# print(type(a))

# print(type(str(x)))

# Math module

import math as MATH
PI = 3.455474574576789
x = 83
y =7
z =-345678.989456

print(MATH.sqrt(x))

print(MATH.factorial(y))

# math.floor gives the value of largest integer less than or equal to the supplied value
print(MATH.floor(z))

print(MATH.degrees(y))

print(MATH.radians(401.07045659157626))

print(MATH.isnan(False))

# Formatting Numbers
# formatting with f-strings
unit_price = 123543.7832
qty = 30
print( f"subtotal: {qty * unit_price}" )
print( f"subtotal: {qty * unit_price:,.5f}" )

# formatting percent numbers
print(f"sales tax rate: {0.065:.2%}")
print(f"sales tax rate: {0.95:.2%}")

# multi line format strings
print(f"""
subtotal: {qty * unit_price:,.2f},
tax_rate: {0.022:.2%}
""")

print(f'''test{1000000000000:,.2f}''', 11 // 5) # 11 // 5 = 2.2 => 2