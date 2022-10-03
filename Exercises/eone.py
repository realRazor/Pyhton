# # Hello world, I'm starting a journey.
# print("It was nice to meet you")
# print("")  # This is single-line comment
# print(3+5)
# print("......")
# print("......")
# print("......")
# x = 35  # The number of house of customers
# y = 22  # The number of house of customers' daughter
# print(x+y)
# a = " talha  "
# b = 33
# c = " yeşilyurt "
# print(a, b, c)
# fn = input("Please enter your name: ")
# sn = input("Please enter your second name: ")
# ln = input("Please enter your lastname: ")
# output = 'Hello, {2} {0} {1}'.format(fn.capitalize(), sn.capitalize(), ln.upper())
# print(output)

# op = f'Hello, {fn} {sn} {ln}'
# print(op)
# print("{} {} {} {} {} {} {} {} {} {} {}".format('Good', 'teacher', 'know', 'how', 'to', 'bring', 'out', 'the', 'best', 'in', 'students'))
# phrase = "I have %d %s and %.2f brothers" % (4, "children", 5)
# print(phrase)
# sentence = "I have a lot of money"
# print("%.10s" % sentence)
# print('%(name)s %(surname)s has %(caramount)d nice cars' % {'name':"Talha", 'surname': "Yeşilyurt", 'caramount':3})
# car = "Mercedes"
# dream = "Developer"
# city = "London"
# message = (f"Hi my dream is to become a {dream}."
#            f" "f"I wanna live in {city}. "
#            f"In my dream car is {car}")
# print(message)
# name = "Talha"
# job = "Developer"
# domain = "Web3 and Blockchain"
# message = f"Hello My name is {name}. "\
#     f"My job is {job}.\n"\
#     f"My dream is to become a {domain} in the future."
# print(message)

# prc = 7/100
# coin = 1000
# m = (prc * coin) + coin
# t = (prc * m) + m
# w = (prc * t) + t
# th = (prc * w) + w
# fr = (prc * th) + th
# st = (prc * fr) + fr
# s = (prc * st) + st
# total = s
# print(total)
#
# print(total)
# def faktoriyel(n):
#     if n == 0:
#         return 1
#     else:
#         sonuç = n * faktoriyel(n-1)
#         print(sonuç)
#         return sonuç
# faktoriyel(7)

def capital_indexes(name):
    for i in range(len(name)):
        if name[i] == name.upper(name[i]):
            print(i)
print(capital_indexes("HeLlO"))













