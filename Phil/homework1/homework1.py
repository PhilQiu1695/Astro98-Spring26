#File: homework1.py

# --- Variables and Data Types ---

a = 10 #int
b = 1.5#float
c = 3j#complex
d = "hello" #string
e = [1, 2, 3] #list of ints
f = {"name": "Ellen", "favorite fruit": "strawberry"} #dictionary
g = (1, 2) #tuple
h = ["apple", "banana", "strawberry"] #list of strings
i = True #boolean
j = None #nonetype
k = [True, "blue", 12] #list of bool, str, int
l = str(14) #string
m = 1e4 #float


lst = [a, b, c, d, e, f, g, h, i, j, k, l, m]
for i in lst:
    print(i)
    print(type(i))

#9 data types: int, str, dict, list, tuple, bool, float, nonetype, complex


# --- Booleans ---
print(10 > 9) #True
print(10 == 9) #False
print(10 <= 9) #False
print(bool("abc")) #True
print(bool(123)) #True
print(bool(["apple", "cherry", "banana"])) #True
print(bool(True)) #True
print(bool(False)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(" ")) #True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print((True and False))#False
print((True and True))#True
print((False and False))#False
print((True or False))#True
print((True or True))#True
print((False or False))#False
print((not(False)))#True
print((not(True)))#False

#3. bool([0]) :not an empty list
#4. False and True and True: one false in and expression makes everything False

# --- Operators ---
print(10 + 5) #15 addition
print(10 - 5)# 5 subtraction
print(2 * 4) #8 multiplication
print(5 % 2) #1 modulus
print(3 ** 2) #9 power
print(15 // 2) #7 floor division

print(5 == 2) #False equality
print(10 != 10) #False inequality
print(2 < 5) # True smaller
print(12 > 5) # True larger
print(5 <= 6) #True smaller or equal
print(1 >= 10) #False larger or equal

x = 5
x += 5
x -= 4
x *= 3

#1. and returns if both are true (bool(1 and 0))
#2. or returns whether at least one is true(False or False)
#3. not turns the following boolean value to the opposite(not 1)

#1. Always return float vs rounds down to lower int
#2.giving quotient vs remainder
#3. %, 10%3 == 1
#4. update a variable by applying an operation to it

# --- Strings ---
my_string = "hello"
print(my_string) #hello
print(my_string[0])#h
print(my_string[1])#e
print(my_string[2])#l
print(my_string[3])#l
print(my_string[4])#o
print(my_string[-1])#o
print(my_string[1:3])#el
print(my_string[0:5:2])#hlo
print(len(my_string))#5
print(my_string + "goodbye")#hellogoodbye
print(my_string * 7) #hellohellohellohellohellohellohello

#1.extract a portion of a string using[start:stop:step]
#2.Hello, my name is Oski
#3.Hello, my name is Oski
#4.f strings are more flexible


# 1. cd change directory,cd Desktop
# 2. ls list out files, ls
# 3. ls -a list all files including hidden ones, ls -a
# 4. mkdir make directory, mkdir Phil
# 5. cat display contents of file, cat phil.py
# 6. pwd print working directory,  pwd
# 7. cd .. change directory to previous, cd ..
# 8. cd . stays in current directory, cd .
# 9. cd ∼ change directory to home, cd ~
# 10. cp copies files, cp a.txt b.txt
# 11. mv moves file, mv a.txt homework1
# 12. rm (be careful with this one) deletes files, rm a.txt
# 13. clear clears terminal screen, clear
# 14. grep, search for string in file, grep "a" a.txt

# 1. du: display disk usage in directory, du.   history n: shows last n commands, history 6. head: displays first 10 lines of a file, head a.txt
# 2. ls shows visible files, -a shows hidden as well
# 3. a hidden file starts with a . and users don't need to see them or edit them usually
# 4. ls -S: sorts directories by size, ls -lh: displays file size in human readable format, du -h: shows total disk usage for specified files or directories





