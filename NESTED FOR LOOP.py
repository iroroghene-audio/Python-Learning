numbers = [2, 2, 2, 2, 5]

for x in numbers:
    count = "" #resets the variable after each iteration
    for y in range(x):
        
        count += 'x'
    print(count)