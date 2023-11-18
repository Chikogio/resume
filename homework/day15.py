#N1 What is these function used  to display text in Python?
print("The text display function in Python is called print")

#N2 In Python, which data type is used to store a whole number?
age = 16
print(type(age))

#N3 Which of the following data types is used to store text in Python?
name = "gio"
print(type(name))

#N4 What is the result of the expression 10 + 5 * 2 in Python?
print(10 + 5 * 2)

#N5 Which of the following is the correct way to assign the value 42 to a variable named answer in Python?
answer = 42
print(answer)

#N6 What is the process of identifying and fixing errors in a program called?
print("the process of identifying and fixing errors in a program called is called debbuging")

#N7 Which is commonly used in Python for naming variables and functions, where words are separated by underscore?
name1 = "elene"
name2 = "gio"
print(name1)
print(name2)
#N8 What is the primary purpose of adding comments to your Python code?
# Writing a code explanation so that the code is not confusing and helps my partner (or anyone who sees the code) understand the code

#N9 How can you take user input in Python?
name3 = input("your name: ")
print(name3)

#N10 Which of the following is not a built-in data type in Python?

#N11 What function can be used to check the data type of a variable in Python?
last_name = "chikovani"
print(type(last_name))

#N12 How can you convert an integer to a string in Python?
age1 = 45
str_age = str(age1)
print(str_age)
print(type(age1))
print(type(str_age))

#N13 What is the term for converting one data type into another in Python?
x = 15
y = "gio"
print(x, y)
print(str(x) + " " + y)

#N14 Which operator is used to check if two values are equal in Python?
print(1 == 1)

#N15 What is the result of the logical AND operation between True and False in Python?
print(3 == 3) #True
print(5 == 2) #False

#N16 What will the expression (5 > 3) and (10 < 20) evaluate to in Python?
print((5 > 3) and (10 < 20)) #True

#N17 In Python, what is used to make decisions and execute different code blocks based on conditions?
if 5 > 1:
    print(":)")
else:
    print(":(")

#N18 Which type of loop is used to iterate over a sequence (e.g., a list or string) in Python?
for x1 in range (2, 20, 4):
    print(x1)

#N19 What type of loop is used when you want to repeat a block of code as long as a condition is true?
x2 = 1
while 3 > 1:
    print("<3")
    x2 += 1
    if x2 >= 1:
        break

#N20 What does the range() function in Python return?
x3 = []
for i in range(1, 10, 2):
    x3.append(i)
print(x3)

#N21 Which keyword is used to start an "if" statement in Python?
if 10 == 1:
    print(":)")
else:
    print(":(")

#N22 What is the purpose of the "else" statement in Python's "if-else" construct?
if 10 == 2:
    print(":)")
else:
    print(":(")

#N23 Which data structure is used to store an ordered collection of items in Python?
list = [1, 2, 3, 4]
print(list)

#N24 In Python, which index represents the first element of a sequence?
list1 = [1, 2, 3, 4]
print(list1, [2])

#N25 How can you access the third element of a list in Python?
list2 = [0, 1, 2, 3, 4, ]
print(list2[3])

#N26 What does slicing allow you to do with a sequence in Python?
list3 = [0, 1, 2, 3, 4, ]
print(list3[1:3])

#N27 How can you extract a subsequence of a list from index 2 to index 5 (5 must be included) in Python?
list4 = [0, 1, 2, 3, 4, ]
print(list4[2:5])

#N28 What does the "step" value in slicing indicate? 
for x1 in range (0, 10, 2):
                      #^step
    print(x1)

#N29 What is a reusable block of code in Python that performs a specific task called?
def x2():
    print("hi")
x2()
x2()
x2()

#N30 In Python, what are the values passed to a function called?
def x3(z):
   #  ^ argument
    print(z)
x3(z = 10)

#N31 Which string method is used to convert a string to uppercase in Python?
last_name1 = "chikovani"
last_name2 = last_name1.upper()
print(last_name2)

#N32 What list method is used to add an element to the end of a list in Python?
names = ["nika", "gio", "elene", "achi", "sandro"]
names.append("gurami")
print(names)

#N33 In Python, which keyword is used to define a new function?
def num(x4):
    print(x4)
num(x4 = 10)

#N34 What keyword is used to return a value from a function in Python?
def num_func(x5):
    return x5
num_func(x5 = 10)