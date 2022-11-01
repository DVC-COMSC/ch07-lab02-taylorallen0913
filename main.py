import random

numbers = []

for i in range(10):
    numbers.append(random.randint(0, 1000))

smallest_index = 0

for i in range(len(numbers)):
    if numbers[i] < numbers[smallest_index]:
        smallest_index = i

print(numbers[smallest_index])

print(smallest_index)

print(min(numbers))

print(numbers.index(min(numbers)))