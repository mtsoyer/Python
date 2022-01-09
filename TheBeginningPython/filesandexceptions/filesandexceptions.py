#content = ""
# with open("py_digits.txt") as file_object:
#	for line in file_object:
#		content += line.rstrip()
#	print(content)
#	for line in file_object:
#		print(line.rstrip())
#	contents = file_object.read()
# print(contents.rstrip())
#content = ""
# with open("pi_million_digits.txt") as pi:
#	for line in pi:
#		content += line.rstrip()
#birth = input("Check if your birthday in the form of mmddyy is within the first million of PI ")
# if birth in content:
#	print(f" {birth} was found!")
# else:
#	print("Youre too rare")

# with open("WhoandTime.txt", "a") as writer:
#	who = input("Hey. Who are you? ")
#	writer.write(f"{who} \n")
#	when = input("When are you coming, tomorrow? ")
#	writer.write(f"{when} \n")

# while True:
#	first = input("Enter your first digit into the calculator. Press Q to quit ")
#	if first.title() == "Q":
#		break
#	second = input("Enter your first digit into the calculator. Press Q to quit ")
#	if second.title() == "Q":
#		break
#	try:
#		quot = int(first) / int(second)
#	except ZeroDivisionError:
#		print("Can't divide by 0")
#	else:
#		print(quot)

# def countwords(name):
#  	content = " "
#  	try:
# 			with open(name, encoding='utf-8') as a:
# 				content  += a.read()
#  	except FileNotFoundError:
# 		 print("The file doesnt exist")
#  	else:
# 		 count = content.split()
# 		 num = len(count)
# 		 print(f" Alice.txt has {num} words")

# name = ['alice.txt', 'siddhartha.txt', 'mody_dick.txt', 'little_women.txt']
# for file in name:
# 	countwords(file)

# def countwords(name):
#  	content = " "
#  	try:
# 			with open(name, encoding='UTF-8') as a:
# 				content  += a.read()
#  	except FileNotFoundError:
# 		 pass
#  	else:
# 		 count = content.split()
# 		 num = len(count)
# 		 print(f" {name} has {num} words")

# # countwords("C:\\Users\\Motheo\\Documents\\Python\\TheBeginningPython\\filesandexceptions\\little_women.txt")
# countwords("little_women.txt")

# import json

# num = [2, 3, 4 , 5]
# with open("numbers.json", 'w') as file:
#     json.dump(num, file)

# with open("numbers.json") as file:
#     print(json.load(file))

# import json

# username = ""
# try:
#     with open("username.json") as uj:
#         username = json.load(uj)
#         print(f"Welcome back, {username}")
# except FileNotFoundError:
#     username = input("Hey, you're new here. What's your name? ")
#     with open("username.json", "w") as uj:
#         json.dump(username, uj)

# import json


# def getuser():
#     try:
#         with open("username.json") as uj:
#             username = json.load(uj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username


# def introduce():
#     username = input("Hey, who are you? ")
#     with open("username.json", "w") as uj:
#         json.dump(username, uj)


# def greetuser():
#     username = getuser()
#     if username:
#         print(f"Hello {username}")
#     else:
#         introduce()


# greetuser()
