# a = 'sdfsdfds234234234./098767890][;'
# print(type(a))

# a = 53453543543.00
# print(type(a))

# a = int(input())
# print(a)


# a = 2
# b = 2
# print(a ** b)


# a = 4.5
# b = 2
# print(a % b)


#
# a = int(input())
# b = int(input())
#
# if pow(a, 2) == b:
#     print(a, '*', a, '=', b)
# elif pow(b, 2) == a:
#     print(b, '*', b, '=', a)
# else:
#     print('None')


a = int(input())
if a % 2 == 0 and a % 3 == 0 and a % 5 == 0:
    print('A')
elif a % 2 != 0 and a % 3 != 0 and a % 5 != 0:
    print('N')
elif a % 2 == 0:
    print('GDSG')