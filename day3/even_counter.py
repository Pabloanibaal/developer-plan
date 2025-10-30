#Day 3 - Even number counter

numbers = [2,7,4,9,12,15,18]
count = 0

for n in numbers:
    if n % 2 ==0:
        count += 1

print(f"There are {count} even numbers in the list.")