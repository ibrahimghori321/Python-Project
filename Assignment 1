# -----------------------------------------------------------
#  PYTHON ASSIGNMENT – NESTED LIST QUESTIONS (SOLVED)
#  All 25 Questions Solved in One File
#  Prepared for GitHub Upload
# -----------------------------------------------------------


print("\nQ1: Print every element of nested list")
a = [[1, 2], [3, 4], [5]]
for row in a:
    for num in row:
        print(num)


print("\nQ2: Count total iterations")
nums = [[10, 20, 30], [40], [50, 60]]
count = 0
for row in nums:
    for num in row:
        count += 1
print("Total iterations =", count)


print("\nQ3: Sum of all numbers in nested list")
x = [[2, 4], [6, 8, 10]]
total = 0
for row in x:
    for num in row:
        total += num
print("Sum =", total)


print("\nQ4: Print row and column index for matrix")
matrix = [[1, 0], [0, 1]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"Row {i}, Col {j} =", matrix[i][j])


print("\nQ5: Print only even numbers")
data = [[5], [6, 7], [8, 9, 10]]
for row in data:
    for num in row:
        if num % 2 == 0:
            print(num)


print("\nQ6: Maximum value in nested list")
nums = [[3, 7], [2, 9, 1], [8]]
mx = nums[0][0]
for row in nums:
    for num in row:
        if num > mx:
            mx = num
print("Max =", mx)


print("\nQ7: Count elements greater than 5")
lst = [[1, 6], [7, 2], [10]]
count = 0
for row in lst:
    for num in row:
        if num > 5:
            count += 1
print("Count =", count)


print("\nQ8: Convert elements to square")
x = [[2, 3], [4], [5, 6]]
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = x[i][j] ** 2
print("Squared list =", x)


print("\nQ9: Print each name length")
names = [['Ali', 'Sara'], ['Ahmed'], ['Saif', 'Zara']]
for row in names:
    for name in row:
        print(name, "=", len(name))


print("\nQ10: Print index path of each element")
grid = [[1, 2, 3], [4, 5, 6]]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(f"{grid[i][j]} → [{i}][{j}]")


print("\nQ11: Print elements using while loop")
a = [[4, 5], [6, 7, 8]]
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j])
        j += 1
    i += 1


print("\nQ12: Count total elements using while loop")
nums = [[1], [2, 3], [4, 5, 6]]
i = 0
count = 0
while i < len(nums):
    j = 0
    while j < len(nums[i]):
        count += 1
        j += 1
    i += 1
print("Total elements =", count)


print("\nQ13: Reverse print using while loop")
lst = [[10, 20], [30], [40, 50]]
i = len(lst) - 1
while i >= 0:
    j = len(lst[i]) - 1
    while j >= 0:
        print(lst[i][j])
        j -= 1
    i -= 1


print("\nQ14: Find sum of each row using while")
x = [[3, 3], [2, 2, 2], [1]]
i = 0
while i < len(x):
    j = 0
    s = 0
    while j < len(x[i]):
        s += x[i][j]
        j += 1
    print("Row sum =", s)
    i += 1


print("\nQ15: Print odd numbers using while loop")
data = [[9], [8, 7], [6, 5, 4]]
i = 0
while i < len(data):
    j = 0
    while j < len(data[i]):
        if data[i][j] % 2 != 0:
            print(data[i][j])
        j += 1
    i += 1


print("\nQ16: Find minimum value using while")
lst = [[12, 5], [3, 9, 1]]
mn = lst[0][0]
i = 0
while i < len(lst):
    j = 0
    while j < len(lst[i]):
        if lst[i][j] < mn:
            mn = lst[i][j]
        j += 1
    i += 1
print("Minimum =", mn)


print("\nQ17: Count numbers divisible by 3")
nums = [[3, 6], [2, 9], [12]]
count = 0
for row in nums:
    for num in row:
        if num % 3 == 0:
            count += 1
print("Count =", count)


print("\nQ18: Print element positions")
matrix = [[5], [6, 7], [8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"({i}, {j}) =", matrix[i][j])


print("\nQ19: Multiply all numbers inside nested list")
x = [[1, 2], [3], [4, 5]]
product = 1
for row in x:
    for num in row:
        product *= num
print("Product =", product)


print("\nQ20: Convert values to cube")
nested = [[2], [3, 4], [5]]
for i in range(len(nested)):
    for j in range(len(nested[i])):
        nested[i][j] = nested[i][j] ** 3
print("Cubes =", nested)


print("\nQ21: Count levels deep")
a = [1, [2, [3, [4]]]]
levels = 1
temp = a
while isinstance(temp, list) and len(temp) > 1:
    temp = temp[1]
    levels += 1
print("Levels deep =", levels)


print("\nQ22: Flatten nested list one level")
x = [[1, 2], [3], [4, 5]]
flat = []
for row in x:
    for num in row:
        flat.append(num)
print(flat)


print("\nQ23: Print only elements that are not lists")
data = [[1, [2, 3]], [4, 5]]
for row in data:
    for item in row:
        if not isinstance(item, list):
            print(item)


print("\nQ24: Sum of each row and total sum")
grid = [[2, 4, 6], [1, 3], [5]]
total = 0
for row in grid:
    s = sum(row)
    print("Row sum =", s)
    total += s
print("Total sum =", total)


print("\nQ25: Print length of each list and total")
items = [['a', 'b'], ['c'], ['d', 'e', 'f']]
total = 0
for row in items:
    print("Length =", len(row))
    total += len(row)
print("Total length =", total)