#!python3

list = [0, 1, 2, 3, 4]
reverse = []

for i in range(len(list)):
    reverse.append(list[(len(list))-i-1])

print(list)
print(reverse)