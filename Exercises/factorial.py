# def factorial(n):
#     if n==1 or n ==0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(7))
def capital_indexes(s):
    indexes = []
    for i in range(len(s)):
        if s[i] == s[i].upper():
            indexes.append(s[i])
    return indexes

print(capital_indexes("Names"));
