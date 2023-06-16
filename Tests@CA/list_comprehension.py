# -----LIST COMPREHENSION-----

# Basic meaning of list comprehension in 3 parts= [expression for _ in iteration]
# Importance positioning of if-else in list comprehension=
#1) use if statements after for loop to filter the values (Filter) OR
#2) use if-else statements before for loop to apply condition to required elements and also print other remaining elements in the list (Map)

# nums = [3,8,1,9,4,3,6]
# names = ["sumeet","amit","navin","sumeet","rachi"]

# --> to print nums using list comprehension:
# list1 = [i for i in nums]
# print(list1)

# --> to print names using list comprehension:
# list1 = [i for i in names]
# print(list1)

# --> to print square of elements in given list using LC
# list1 = [i*i for i in nums]
# print(list1)

# --> to print uppercase to all elements using LC
# list1 = [i.upper() for i in names]
# print(list1)

# --> to print a list where multiply '3' with 5 using LC
# list1 = [i*5 for i in nums if i==3] #wrong way
# list2 = [i*5 if i==3 else i for i in nums] #Important point - We can only have if-else to the left of for loop and only if to the right of for loop
# print(list1)
# print(list2)

# --> Sir question - create list with multiples of 7 where element is not grater than 777
# list3 = [i for i in range(1,778) if i%7==0]
# print(list3)

# --> Sir question - remove navin from list and in next list replace sumeet with ramesh
# list1 = [i for i in names if i!="navin"]
# list2 = ["ramesh" if i=="sumeet" else i for i in names]
# list3 = ["ramesh" if i=="sumeet" else i for i in names if i!="navin"] #both together
# print(names)
# print(list1)
# print(list2)
# print(list3)

# Nested if

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# nums = [1,2,3,4]

# mix = [(i,j) for i in nums for j in fruits] #printing both with 2 for loop
# mix = [(i,j) for i in nums if i>2 for j in fruits if j!="banana"] #printing both with some if conditions inside for loop (nested loop)
# mix = [(i,j) for i in nums if i>1 and i!=3 for j in fruits if j!="banana" and j!="kiwi"] #printing both with some if as well as and conditions inside for loop (nested loop)
# print(mix)

#VERY IMPORTANT QUESTIONS FOR BEST PRACTICE:

#(Q1) Find all of the numbers from 1-1000 that are divisible by 7
# list = [i for i in range(1,1001) if i%7==0]
# print(list)

#(Q2) Find all of the numbers from 1-1000 that have a 3 in them
# list = [i for i in range(1,1001) if '3' in str(i)]
# print(list)

#(Q3) Count the number of spaces in a string
# string = " My name is Sumeet and my age is 21   "
# list1 = [i for i in string if i==" "]
# print(len(list1))

#(Q4) Consonants in a string
# string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# list1 = [i for i in string if i not in ('a','e','i','o','u',' ')]
# print(list1)

#(Q5) Get index and value from list
# items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
# list1 = [i for i in enumerate(items)]
# print(list1)

#(Q6) Find common numbers in two lists of numbers
# list1 = [1, 2, 3, 4]
# list2 = [2, 3, 4, 5]
# list3 = [i for i in list1 if i in list2]
# print(list3)

#(Q7) Find numbers in sentence
# sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list1 = [i for i in sentence if i in ('0','1','2','3','4','5','6','7','8','9')]
# print(list1)
#idk this method
# words = sentence.split()
# result = [number for number in words if not number.isalpha() ]
# print(result)

#(Q8) Determine even or odd in list of numbers
# result = ['even' if n%2 == 0 else 'odd' for n in range(20)]
# print(result)

#(Q9) Common number tuples
# list1 = [1, 2, 3,4,5,6,7,8,9]
# list2 = [2, 7, 1, 12]
# list3 = [(i,j) for i in list1 for j in list2 if i==j]
# print(list3)

#(Q10) Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)
# result = [number for number in range(1,100) if True in [True for x in range(2,10) if number % x == 0]]
# print(result)


# -----DICTIONARY COMPREHENSION-----


# dictionary comprehension = create dictionaries using an expression and can replace for loops and certain lambda functions

# IMPORTANT DICTIONARY THINGS
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
#                 (key)  (value)
#                   |       |
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# -------------------------------------------------------------------------
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------------------------------------------------------
# def check_temp(value):
    # if value >= 70:
        # return "HOT"
    # elif 69 >= value >= 40:
        # return "WARM"
    # else:
        # return "COLD"


# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)
