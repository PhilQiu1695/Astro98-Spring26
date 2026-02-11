#3.1
def say_goodbye(name):
    print("Goodbye", name)

#3.2
def circle_area(radius):
    print("Area:", 3.14 * radius**2)

#4
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#5
def temp_margin(temps):
    return (min(temps), max(temps))

def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False
    
def fuel_eff(distance, fuel):
    return divide(distance, fuel)

def encrypt(num):
    digits = len(str(num)) - 1
    new_num = num//10 + num % 10 * 10 ** digits
    return new_num

#6
def new_power(x, y):
    num = x
    for i in range(y - 1):
        num = num * x
    return num
        
def for_min(nums):
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return min

def for_max(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max

def while_min(nums):
    min = nums[0]
    while len(nums) > 0:
        if nums[0] < min:
            min = nums[0]
        nums.pop(0)
    return min

def while_max(nums):
    max = nums[0]
    while len(nums) > 0:
        if nums[0] > max:
            max = nums[0]
        nums.pop(0)
    return max

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

number = 123456789
print("The result of summing digits:", sum_digits(number))