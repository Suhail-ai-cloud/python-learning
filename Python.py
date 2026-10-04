# # Name="suhail"
# # Age=21
# # Dream_Job="Machine Learning"
# # print(Name,Age,Dream_Job)

# # Name="suhail"
# # Age=21
# # Country="india"
# # Programming_Language="Python"
# # Dream_Company="Google"
# # Dream_Salary=100000
# # Favorite_AI_Field="Machine Learning"
# # Hours_You_Study_Daily=2

# # print("Name:",Name)
# # print("Age:",Age)
# # print("Country:",Country)
# # print("Programming Language:",Programming_Language)
# # print("Dream Company:",Dream_Company)
# # print("Dream Salary:",Dream_Salary)
# # print("Favorite AI Field:",Favorite_AI_Field)
# # print("Hours You Study Daily:",Hours_You_Study_Daily)


# Name="Suhail"
# Age=21
# Height=5.9
# Weight=70.0
# Favorite_Programming_Language="Python"
# Is_Learning_AI=True
# Current_Semester=4

# print("Name:",Name,"type:",type(Name))
# print("Age:",Age,"type:",type(Age))
# print("Height:",Height,"type:",type(Height))
# print("Weight:",Weight,"type:",type(Weight))
# print("Favorite Programming Language:",Favorite_Programming_Language,"type:",type(Favorite_Programming_Language))
# print("Is Learning AI:",Is_Learning_AI,"type:",type(Is_Learning_AI))
# print("Current Semester:",Current_Semester,"type:",type(Current_Semester))

##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 2
##########################################################################################################################################################
##########################################################################################################################################################

# print(True == 1)
# print(False == 0)

# print(isinstance(True,int))

# List(orderd,muteble,allow duplicates,can contain diffrent data types,indexed)

# list=[1,2,3,4,5,5,5,6,6,6,1,1,1]
# list[0]=10
# print(list)

#tuple(orderd,immutable,allow duplicates,can contain diffrent data types,indexed)

# tuple=(1,2,3,4,5,5,5,6,6,6,1,1,1)
# tuple[0]=10
# print(tuple)

# Sets(unordered,mutable,does not allow duplicates,can contain diffrent data types,not indexed)
# set={1,2,3,45,5,5,56,6,7,7,1,8,8,7,7,7,7}
# print(set)

# Dictionaries(unordered,mutable,allow duplicates,can contain diffrent data types,not indexed)
# dic={"name":"suhail","age":21,"country":"india","language":"python"}
# print(dic["name"])
# print("hi")

# 1

# Create variables containing:

# your name
# age
# height
# student status

# Print their types.

# name="Suhail"
# age=21
# height=180
# student_status=True
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(student_status))

# 2# Create three integers and calculate:

# sum
# difference
# multiplication
# division

# a=10,b=5,c=2
# sum=a+b+c
# difference=a-b-c
# multiplication=a*b*c
# division=a/b/c

# 3

# Create a string and print:

# first character
# last character
# length

# string="I Love python"
# print("first letter:",string[0])
# print("last letter:",string[-1])
# print("length:",len(string))

# 4

# Create a list containing five programming languages.

# Print:

# first language
# last language
# number of languages

# list=["python","C-programming","C++","java","javascript"]
# print("first language is:",list[0])
# print("last language is:",list[-1])
# print("number of languages is:",len(list))

# 5

# Create a tuple containing three coordinates.

# Access each coordinate

# touple=(1.000,2.000,3.000)
# cordinate_x=touple[0]
# cordinate_y=touple[1]
# cordinate_z=touple[2]

# print(cordinate_y)

# 6

# Create a set containing duplicate numbers.

# Observe what happens.

# set={1,2,3,4,5,1,2,3,4,5}
# print(set)
# remove all dupolicate contain the uniqe numbers only

# 7

# Create a dictionary representing a user.

# Include:

# name
# age
# email
# role

# Access each value

# user={"name":"Suhail","age":21,"email":"suhail@email.com","role":"Student"}

# name=user["name"]
# age=user["age"]
# email=user["email"]
# role=user["role"]

# 8

# Convert:

# "100"
# "3.14"
# 100
# True

# into appropriate types.


# a=int("100")
# b=float("3.14")
# c=str(100)
# d=int(True) #-->out put 1
# c=str(True)#-->out put True

# 9

# Create a mutable list and modify one element


# list=[1,2,3,4,5,6]
# list[0]=2
# print(list)

# 10

# Create a string and try to modify one character.

# Observe the result

# string="hello world"
# 1)new_str=string[:5]+"new line"+string[5:]
# new_str=list(string)
# new_str[6]="Hey"
# text_list="".join(new_str)


# # string[2]="z"
# print(text_list)

# print(0.1 + 0.2 == 0.3)

# print(7 / 2)
# print(7 // 2)
# print(7 % 2)

# print(-7 / 2)
# print(-7 // 2)
# print(-7 % 2)

# print(2 ** 5)
# print(3 ** 3)

##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 3
##########################################################################################################################################################
##########################################################################################################################################################
# a = 0.1
# b = 0.2
# c = 0.3

# print(a.hex())
# print(b.hex())
# print(c.hex())

# print((a + b).hex())


# a = 0.1
# b = 0.2
# c = 0.3

# print(a + b == c)
# print(abs((a + b) - c))

# import math

# print(math.isclose(0.1 + 0.2, 0.3))

# x = float("inf")

# print(x > 1000000)\

# x=0.1
# y=0.2
# xy=0.3
# z=x+y
# print(xy == z)


# x=0.5
# y=0.6
# xy=1.1
# z=x+y
# print(xy == z)

# a = 10
# b = 10.0
# c = 10 + 0j
# d = 10 / 2
# e = 10 // 2

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
# print(e, type(e))


# 10 <class 'int'>
# 10.0 <class 'float'>
# (10+0j) <class 'complex'>
# 5.0 <class 'float'>
# 5 <class 'int'>

# print(-20//6)

# str="Hello World and Dash"
# # new_str=str[:5]+"Suhail"+"welcome"+str[5:]
# # print(str[::-1])
# new_str="l"+str[1:]
# print(new_str)

# text="Text need to write"
# # splited_text=text.split()
# # joined_text="    ".join(splited_text)
# # new_joined_text="    "+joined_text[0:]
# # print(new_joined_text)
# # striped_text=new_joined_text.strip()
# # print(striped_text)
# # new_text=text.replace("Text","suhail")
# # print(new_text.find("o"),new_text)
# print("suhail" in text)
# text_1="Hello\tworld"
# new=text_1.encode("utf-8")
# print(type(new) )

# text = "  Python is powerful and Python is easy to learn  "

# Your program should calculate/display:

# The cleaned text using strip()
# The number of characters using len()
# The number of words using split()
# Whether "Python" exists in the text
# How many times "Python" appears
# The text converted to uppercase
# The text converted to lowercase
# Replace "Python" with "AI"
# Create a sentence using an f-string containing the word count

# text = "  Python is powerful and Python is easy to learn  "

# cleaned_text=text.strip()
# number_of_chars=len(text)
# splited_text=cleaned_text.split()
# check_presentse_pyhton="python" in text
# times_of_python=text.count("python")
# uppercase=cleaned_text.upper()
# lowercase=cleaned_text.lower()

# replace_word=cleaned_text.replace("python","ai")

# name="suhail"

# print(f"A boy named {name} is learning python")

##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 4
##########################################################################################################################################################
##########################################################################################################################################################

# x="Suhail"
# y=[1,2,3,4]
# z=2

# string_method=x.upper()
# y.insert(2,10)
# y_method=y
# print(y_method)
# print(y_method is y)

# Boolien

# name= [0]
# if name:
#     print(f"name existes Name is {name}")
# else :
#      print("not exist")
# List

# a=[1,2,3,4,5,6]
# b=a
# c=b.insert(1,10)
# print(c is b )
# # print(f"A is :{a}\n B is :{b}\nC is :{c}")
# # why is none and False am not copyes am refeerd c as to b and vaues changed


##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 5
##########################################################################################################################################################
##########################################################################################################################################################

# a=[1,2,3,4,5,6,6]
# b=set(a[::-1])
# print(type(b))
# print(b)

# b={1,2,3,4,5,6,6}
# # b.add(10)
# # print(b)
# b.discard(10)
# print(b)

# A= {1, 2, 3, 4, 5}
# B={4,5,6,7,8,9}
# # union
# c= A | B
# print(c)
# intesrsection
# d=A&B
# print(d)
# diffrence
# e=B-A
# print(e)
# symmetric diffrce
# f=A^B
# print(f)

##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 6
##########################################################################################################################################################
##########################################################################################################################################################
# dictionary
# a={"name":"suhail","age":21,"role":"admin"}
# b=a["name"]
# print(b)
# a["addres"]="house 50"
# c=a["addres"]
# d=a["mail"]
# d=a.get("mail")
# print(d)
# a["age"]=20
# print(a.keys())
# print(a)
# b=a.pop("age")
# print(a)
# print(b)
# if "name" in a:
#     print("You are correct..")
#     b=a.get("name")
#     print(b)
# else:
#     print("You're wrong")
# b=a.items()
# print(a is b)
# print(a)
# print(b)

# student={
#     "name":"Suhail",
#          "age":21,
#          "Standard":"Plus One",
#          "contact":{
#              "phone":9746805981,
#              "email":"suhail@gmail.com"
#          }
#          }

# student["contact"]["phone"]=9562804749
# print(student)
# for keys,values in student.items():
#     print(keys,values)
# for keys,values in student["contact"].items():
#     print(keys,values)



##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 7
##########################################################################################################################################################
##########################################################################################################################################################
# TYPE CONVERTION 

# A=1.99
# b=int(A)
# print(b)
# a=10
# b=float(a)
# print(a)
# a=21
# b="my age i " + str(a)
# print(b)

# name="Suhail"
# c=["a","b","c","s","u"]
# b=list(name.lower())
# for c in b:
#     if c in b:
#         b.remove(c)
#         print(b)
#     else:
#         print("HI")

# Convert age from str → int.
# Remove duplicate skills using a set.
# Convert the unique skills back into a list.
# Add "Machine Learning" to the skills.
# Extract the state from location.
# Check whether "Python" is in the skills.
# Create a sentence using an f-string, such as:
# "Suhail is 21 years old and knows Python."
# Print the final dictionary.

# student = {
#     "name": "Suhail",
#     "age": "21",
#     "skills": ["Python", "Django", "Python", "AI"],
#     "location": ("Kerala", "India"),
#     "is_student": True
# }
# student["age"]=int(student["age"])

# student["skills"]=set(student["skills"])
# student["skills"]=list(student["skills"])
# student["skills"].append("Machine Learning")
# location=student["location"][0]
# skills=student['skills']
# skill="Python"
# yes=skill in skills
# name=student["name"]
# age=student["age"]
# if yes :
#     print(f"{name} is {age} years old and {name} knows python")
# else:
#     print(f"{name} is {age} years old and HE don't know python")

# print(student)

# 𝗢𝗣𝗘𝗥𝗔𝗧𝗢𝗥𝗦
# x = 30
# y = 20

# result = y and x
# print(result)  


##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 8
##########################################################################################################################################################
##########################################################################################################################################
# CONDITIONAL STATEMENTS

# age = 18
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# name=input("Enter your name: ")

# if name == "Suhail":
#     print("Hello, Suhail!")
# elif name == "Alice":
#     print("Hello, Alice!")
# elif name == "Bob":
#     print("Hello, Bob!")
# else:
#     print("Hello, stranger!")

# MATCH CASE STATEMENTS
# match name:
#     case "Suhail":
#         print("Hello, Suhail!")
#     case "Alice":
#         print("Hello, Alice!")
#     case "Bob":
#         print("Hello, Bob!")
#     case _:
#         print("Hello, stranger!")

#  _      ____   ____  _____   _____ 

# | |    / __ \ / __ \|  __ \ / ____|
# | |   | |  | | |  | | |__) | (___  
# | |   | |  | | |  | |  ___/ \___ \ 
# | |___| |__| | |__| | |     ____) |
# |______\____/ \____/|_|    |_____/ 
                                   
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for number in numbers:
#     if number % 2 ==1:
#         odd.append(number)
#         numbers.pop(number)
        
#     else:
#         even.append(number)
# print(numbers)
# print(even)
# print(odd)

# student = {
#     "name": "Suhail",
#     "age": 21
# }

# for key,value in student.items():
#     print(key,value)

# for i in range(0,500,50):
#     print(i)

# numbers = [20, 60, 40, 80, 90,1,2,3,4,5,6,7,8,9,10]
# count=0
# for num in numbers:
#     if num %2 == 0:
#         count=count+1

# print(count)
# user_data = {
#     "username": "suhail",
#     "email": "user@example.com",
#     "role": "developer"
# }
# for key ,values  in user_data.items():
#     print(f"{key}:{values}")

# students = {
#     "student1": {
#         "name": "Ali",
#         "marks": 85
#     },
#     "student2": {
#         "name": "Sara",
#         "marks": 92
#     }
# }

# for student_id,student in students.items():
#     print(student_id)
#     print(student["name"])
#     print(student["marks"])
\

##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 9
##########################################################################################################################################################
##########################################################################################################################################
# age=100
# while age <18 or age>0:
#     print(age)
#     age = age +1
#     break

# students_database = {
#     "student_01": {
#         "name": "Arjun Nair",
#         "age": 16,
#         "gender": "Male",
#         "class": "10th Grade"
#     },
#     "student_02": {
#         "name": "Ananya Sharma",
#         "age": 15,
#         "gender": "Female",
#         "class": "10th Grade"
#     },
#     "student_03": {
#         "name": "Rohan Das",
#         "age": 17,
#         "gender": "Male",
#         "class": "11th Grade"
#     },
#     "student_04": {
#         "name": "Priya Patel",
#         "age": 16,
#         "gender": "Female",
#         "class": "11th Grade"
#     },
#     "student_05": {
#         "name": "Kabir Singh",
#         "age": 15,
#         "gender": "Male",
#         "class": "10th Grade"
#     },
#     "student_06": {
#         "name": "Diya Menon",
#         "age": 17,
#         "gender": "Female",
#         "class": "12th Grade"
#     },
#     "student_07": {
#         "name": "Aman Verma",
#         "age": 18,
#         "gender": "Male",
#         "class": "12th Grade"
#     },
#     "student_08": {
#         "name": "Sneha Reddy",
#         "age": 16,
#         "gender": "Female",
#         "class": "11th Grade"
#     },
#     "student_09": {
#         "name": "Vikram Malhotra",
#         "age": 15,
#         "gender": "Male",
#         "class": "10th Grade"
#     },
#     "student_10": {
#         "name": "Isha Gupta",
#         "age": 17,
#         "gender": "Female",
#         "class": "12th Grade"
#     }
# }
# count=0
# for key,value in students_database.items():
#     if value["age"] >=16:
#         count=count+1
        
# print(count )


##########################################################################################################################################################
##########################################################################################################################################################
#                                                           Day 10
##########################################################################################################################################################
##########################################################################################################################################

# continue
# numbers=[1,2,3,4,5,6,6,7,8]
# for number in numbers:
#     if number ==6:
#         continue
#     print(f"the half of {number} is {number/2}")

#                                                           Day 11
##########################################################################################################################################################
##########################################################################################################################################
# break,continue,pass

# numbers=[1,2,3,4,5,6,6,7,8]
# for number in numbers:
#     if number ==6:
#         break
#     print(f"the half of {number} is {number/2}")

# if number ==6:
#     pass
# if number ==6:
#     print("the number is 6")

# Nested Loops

# for i in range(3):
#     print("outer :",i)
#     for j in range(3):
#         print("inner :",j)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for number in row:
#         print(number)

# for i in range(1,6):
#     for j in range(i):
#         print("1",end=" ")
#     print()

# for i in range(1,11):

#     print(f"{i} * 5 = {i*5}")


# for i in range(1,11):
#     if i == 20:
#         print("20 is here")
#         break
# else:
#     print("not found ")

# numbers = [12, 25, 7, 42, 18, 31]

# for num in numbers:
#     if num == 42:
#         print("found!")
#         break
# else:
#     print("not found")

# function

# def introduce(name):
#     print("My name is ",name)
#     print("I am learning Python")
#     print("I want to become an AI Engineer")


# introduce("suhail")

# def squar(number):
#     return number*2

# print(squar(4))
# rectangle's area

# def calculate_area(width,length):
#     return width*length

# area = calculate_area(10, 5)
# print(area)

# def student_info(name, age, course):
#     print(f"Name : {name}")
#     print(f"age : {age}")
#     print(f"course : {course}")

# student_info(name="suhail",age=21,course="MCA")

# lambda
# mult=lambda a,b : a * b
# print(mult(2,2))

# numbers = [5, 2, 9, 1, 7]

# numbers.sort(key=lambda num:num)

# students = [
#     {"name": "Arjun", "age": 20},
#     {"name": "Suhail", "age": 21},
#     {"name": "Rahul", "age": 19},
#     {"name": "Isha", "age": 22}
# ]


# students.sort(key=lambda student:student["age"])
# print(students)

#                                                           Day 11
##########################################################################################################################################################
##########################################################################################################################################


# high order function

# def add(a,b):
#     return a+b

# def mult(a,b):
#     return a*b

# def claculation(funtion,a,b):
#     return funtion(a,b)

# result=claculation(mult,10,10)
# print(result)

# Docstring

# def multiply(a,b):
#     """this funtion will multiply a dand b toger and return teh answer"""
#     return (a*b)
# print(multiply.__doc__)


# 🧪 Functions Practice — Challenge 1

# Write a function:

# calculate_total(price, quantity)

# It should:

# Multiply price × quantity
# Return the total
# Have a docstring
# Store the returned value in a variable called total
# Print total

# total = calculate_total(250, 3)

# def calculate_total(price,quantity):
#     """This funtion will return total of the purchase"""
#     return price*quantity
# total = calculate_total(250, 3)
# print(total)

# 🧪 Challenge 2 — Multiple logic

# Now write:

# calculate_discount(price, discount_percent)

# It should:

# Calculate the discount amount.
# Subtract the discount from the original price.
# Return the final price.
# Have a docstring.

# def calculate_discount(price,discount_percent):
#     dis_amt= price * discount_percent / 100
#     final_amt=price-dis_amt
#     return final_amt
# print(calculate_discount(1000, 20))


# 🧪 Challenge 3 — Combining functions

# Now let's connect functions together.

# Write these two functions:

# calculate_total(price, quantity)
# calculate_discount(total, discount_percent)

# Then use them like this:

# price → quantity → total → discount → final price


# def calculate_total(price,quantity):
#     """This funtion will return total of the purchase"""
#     return price*quantity


# def calculate_discount(price,discount_percent):
#     dis_amt= price * discount_percent / 100
#     final_amt=price-dis_amt
#     return final_amt

# price = 500
# quantity = 3
# discount_percent = 10

# total = calculate_total(price, quantity)

# final_price = calculate_discount(total, discount_percent)

# 🧩 Functions Mini-Project — Student Result Analyzer

# Let's combine the things you've learned so far:

# Functions
# Parameters
# Arguments
# if / elif / else
# Loops
# return
# Docstrings
# Basic calculations

# def analyze_student(name, marks):
#         """Analyze a student's marks and return the result."""
#         total=sum(marks)
#         average=total/len(marks)
#         result=""
#         if average >= 90:
#                 result="Excellent"
#         elif average >= 75:
#                 result="Very Good"
#         elif average >= 50:
#                 result="Pass"
#         else:
#                 result="Fail"

#         return name,total,average,result

# result=analyze_student("Suhail", [78, 85, 92, 67, 88])   
# print(result)       
                
                


#                                                           Day 12
##########################################################################################################################################################
##########################################################################################################################################

# imports and modules

# from math import factorial,sqrt

# print(factorial(5))
# print(sqrt(144))

# from math import sqrt

# print(sqrt(144))
# import random

# number_1=random.randint(1,50)
# number_2=random.randint(1,50)
# sum_of_num=sum(number_1,number_2)
# print(sum_of_num)


# import datetime
# now= datetime.datetime.now()
# print(now)

# external modules
# creating an module named main and creating a module named calculator

# File handling 

# with open("learning.txt")as file:
#     for line in file:
#         print(line,end="" )


# with open("learning.txt","a") as file:
#     file.write("I am learning Python.\n")
#     file.write("I am learning File Handling.\n")
#     file.write("I want to become an AI Engineer.\n")
#     file.write("I am also learning AI and Machine Learning.\n")

# JSON javaSript object notation

# import json

# student = {
#     "name": "Suhail",
#     "age": 21,
#     "course": "MCA",
#     "skills": ["Python", "Django", "React"]
# }

# with open("student.json","w") as file:
#     json.dump(student,file,indent=4)

# import json

# with open("student.json","r") as file:
#     data=json.load(file)
# #     print(data)

# print(data["name"])
# print(data["age"])
# print(data["course"])
# print(data["skills"])

# File Handling → Binary Files

# with open("image.png","rb") as file:
#     data=file.read()

# with open("copy.jpg","wb") as file:
#     file.write(data)

# Exeption handlingh 
# Try and Exept

# try:
#     age=int(input("enter you age :"))
#     print("Your age is :",age)
# except:
#     print("Enter a valid number")

# def countoun(number):
#     print(number)
#     if number == 0:
#         return
#     number =number-1
#     countoun(number)

# countoun(5)

# OOP — Object-Oriented Programming

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         pass

# student1=Student("Suhail",21)
# student2=Student("Ashraf",22)

# print(student1.name,student1.age)
# print(student2.name,student2.age)

# Create this yourself:
# - Student class
# - name and age
# - A method called introduce()
# - The method should print something like:
#   "My name is Suhail and I am 21 years old."
# - Create two students
# - Call introduce() for both

# class Student:
#         def __init__(self, name , age):
#                 self.name= name
#                 self.age=age

#         def greetings(self):
#                 print(f"My name is {self.name} and I am {self.age} years old.")

# student1=Student("Suhail",21)
# student1.greetings()


# class Animal:
#     def speak():
#         print("Animal can speak..")

# class Dog(Animal):
#     pass

# jod=Dog()
# jod()
# class Mentor:
#     def name(self):
#         print("mentor com HOD")


# class BCA(Mentor):
#     def students(self):
#         print("here we have 50+ students")

# clz=BCA()
# clz.students()
# clz.name()

# class Mentor:
#     def __init__(self,mentor_name):
#         self.mentor_name=mentor_name

#     def name(self):
#         print(f"{self.mentor_name}  is the mentor")

# class Bca(Mentor):
#     def __init__(self, mentor_name,Bca_count):
#         super().__init__(mentor_name)
#         self.Bca_count=Bca_count

# clg=Bca("rahul",60)
            
# print(clg.name)

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Dog says Woof!")

# result=Dog()
# result.speak()

# Polymorphism

# class Dog:
#     def sound(self):
#         print("Woof")


# class Cat:
#     def sound(self):
#         print("Meow")

# data=[Dog(),Cat()]
# for animal in data:
#     animal.sound()