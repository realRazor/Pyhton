numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
repeat_numbers = []
for i in numbers:
    value = numbers.count(i)
    repeat_numbers.append(value)
print(repeat_numbers)
mostfrequent = repeat_numbers.index(max(repeat_numbers))
print(f"the most frequent element is {numbers[mostfrequent]} and it was {max(repeat_numbers)} repeated")
