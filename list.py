test = ["Brian", "Nadia", "Cammy", "Louise", "Chris", "Shuna"]

for t in test:
    print(t)

fruits = ["apple", "banana", "grape", "orange"]

print(fruits[0])

num_items = len(fruits)
print(num_items)

fruits.append("pear")
print(fruits)

for f in fruits:
    fruits.remove(f)
    print(fruits)

print(fruits)