chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1},
]

total = 0

for chicken in chickens:
    if chicken["eggs"] > 0:
        print("WE HAVE ALL THE EGGS")
    total += chicken["eggs"]
    chicken["eggs"] = 0

print(f'total eggs collected {total}')