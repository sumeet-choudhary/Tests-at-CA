# Q1) Write Datatypes
# sequence
list = [1, 2, 0.5]
set = {2, 3, 0.1}
tuple = (3, 5, 4, 3)
str = "sumeet"
x = list(range(10))
# numeric
int = 1, 2, 3
float = 0.5, 0.2
complex = 1 + 2j
bool
# mapping/dictionary
data = {1: 'navin', 2: 'sumeet'}

# Q2) using list comprehension find all of the numbers from 1–1000 that are divisible by 8
for i in range(1, 10001, 1):
    if (i % 8 == 0):
        print(i,"Divisible by 8")

# Q3) Sum of number digits in List
# test_list = [12, 67, 98, 34]
a = [12, 67, 98, 34]
print(sum(a))

# Q4) print last element"34" of test_list
a = [12, 67, 98, 34]
x = a[3]
print(x)

# Q5) reverse test_list
a = [12, 67, 89, 34]
b =
print(b)

# Q6) create list with different data type
list = [1, 0.5, 'sumeet', [1, 2, 3, 4, 6]]
x = list[2]
a = list[2][4]
print(x)
print(a)

# Q7) test_list1 = ["a", "b", "ab", "b", 2, 2, 45, 45, "ab" ]
# create new list with only unique elements
a = ["a", "b", "ab", "b", 2, 2, 45, 45, "ab"]
x = set(a)
print(x)

# Q8) name = "sumeet"
# create dict where key is my alphabet and value is count of occurrence
# dict= {"s": 1, "u": 1, "m": 1, "e": 2, "t": 1}
