# 1. Create an empty list called `task_list`
# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'
# 3. Print out `task_list`
# 4. Remove the last task
# 5. Print out `task_list`
# 6. Print out the number of elements in `task_list`

task_list = []

cheat_list = ["Make Dinner", "Eat Dinner", "Get into bed", "Sleep"]

task_list = cheat_list

print(task_list)

task_list.pop()

print(task_list)
length = len(task_list)
print(length)