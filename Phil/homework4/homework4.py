foodList = ["chocolate", "wonton", "ramen", "curry", "cookies"]
print(foodList[1])
print(foodList[-1])
foodList.append("bananas")
foodList.insert(0, "apple")
foodList.remove("wonton")
print(len(foodList))
for f in foodList:
    print(f.upper())
newFoodList = foodList[0]+foodList[-1]
if "potatoes" in foodList:
    print("A potato!")
else:
    print("No potato!")


numbers = []
for i in range(21):
    numbers.append(i)

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    lst = lst[::-1]
    return lst[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print(step3)

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

for i in numbers[2]:
    print(i)
print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(nums):
    sum = 0
    for lst in nums:
        for n in lst:
            sum += n
    return sum

def creator():
    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(5 * i + j + 1)
    return matrix

def firstEditor(matrix):
    for lst in matrix:
        for i in range(len(lst)):
            if lst[i] % 3 == 0:
                lst[i] = "?"

def secondEditor(matrix):
    sum = 0
    for lst in matrix:
        for i in lst:
            if i != "?":
                sum += i
    return sum

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
ages.pop("Mariam")
for n in ages:
    print(n, ages[n])


mat = creator()
firstEditor(mat)
sum = secondEditor(mat)
print(mat, sum)
