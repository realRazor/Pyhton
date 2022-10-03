numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
repeat_numbers = {}
for i in numbers:
    if i not in repeat_numbers:  # if index of numbers is not in repeat_numbers dict, then execute
        repeat_numbers[i] = 0
    repeat_numbers[i] += 1  # if there is in repeat_numbers, then add 1 (counting how many times repeat).
most_frequent = max(repeat_numbers, key=repeat_numbers.get)
frequency = max(repeat_numbers.values())
print(repeat_numbers)
print(f"the most frequent is {most_frequent} and it was {frequency} times repeated")

#  The other solution is below
# numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
# rpt = 0
# frqnt = 0
# for x in numbers:
#   if numbers.count(x) > rpt:
#     rpt = numbers.count(x)
#     frqnt = x
# print(f"the most frequent number is {frqnt} and it was {rpt} times repeated")
