# a = str(input('Enter: '))
# print(a[3])
# print(a[-2])
# print(a[:5])
# print(a[:-2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[::-2])
# print(len(a))
# ------------------------------------------------------------------------------------------02
# a = str(input('Enter: '))
# print(a.count(' ') + 1)
# ------------------------------------------------------------------------------------------03
# a = str(input('Enter: '))
# print(a[ (len(a) + 1) // 2:] +a[:(len(a) +1 ) // 2])
# print(a[3])
# ----------------------------------------------------------------------------------------04
# a = str(input('Enter: '))
# if a.count('f') == 1:
#     print(a.find('f'))
# if a.count('f') >= 2:
#     print(a.find('f'), a.rfind('f'))
# ----------------------------------------------------------------------------------------05

# a = str(input('Enter: '))
# print(a.replace('1', 'one'))

#-----------------------------------------------------------------------------------------06

# a = str(input('Enter: '))
# print(a.replace('@', ''))

# ----------------------------------------------------------------------------------------07

# a = str(input('Enter: '))
# a = a.replace('h', 'H', a.count('h') -1 )
# print(a.replace('H', 'h', 1))

# -----------------------------------------------------------------------------------------08

# a = int(input('Enter ''a'': '))
# b = int(input('Enter ''b'': '))
# if (a > b):
#     print(b)
# elif (a < b):
#     print(a)

# ------------------------------------------------------------------------------------------09

# a = int(input('Enter: '))
# sign = 0
# if (a > 0):
#     sign = 1
# elif (a < 0):
#     sign = -1
# else:
#     sign = 0
# print(sign)

# ------------------------------------------------------------------------------------------10

# x1 = int(input(''))
# x2 = int(input(''))
# y1 = int(input(''))
# y2 = int(input(''))
# if 1<=x1<=8 and 1<=x2<=8 and 1<=y1<=8 and 1<=y2<=8:
#     if (x1 +y1)%2==(x2 + y2)%2:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('You`re number not defined system ')

# -------------------------------------------------------------------------------------11
# a = int(input('Enter: '))
# if (a % 4 == 0) and (a % 100 != 0) and (a % 400 == 0):
#     print('Yes')
# else:
#     print('No')

# --------------------------------------------------------------------------------------12

# a = int(input('Enter: '))
# b = int(input('Enter: '))
# c = int(input('Enter: '))
# if (a==b==c):
#     print('3')
# elif (a == b) or (a == c) or (c==b):
#     print('2')
# elif ( a != b != c):
#     print('0')

# ======================================================================================13

# x1 = int(input(''))
# x2 = int(input(''))
# y1 = int(input(''))
# y2 = int(input(''))
# if 1<=x1<=8 and 1<=x2<=8 and 1<=y1<=8 and 1<=y2<=8:
#     if x2==x1 or y2==y1:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('You`re number not defined system ')

# =======================================================================================14
# n = int(input(''))
# m = int(input(''))
# k = int(input(''))
# if k // n*m and (k // n == 0) or (k//m == 0):
#     print('Yes')
# else:
#     print('No')

# ========================================================================================15

# N = int(input(''))
# M = int(input(''))
# x = int(input(''))
# y = int(input(''))
# if (N > M):
#     N, M = M, N
# elif (x >= N // 2):
#     x = N - x
# elif (y >= M // 2):
#     y = M - y
# elif (x < y):
#     print(x)
# else:
#     print(y)