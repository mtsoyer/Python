# dictionarys
# a = {"color" : "green", "number":2}
# print(a["color"])
# print(a)
# a["position"] = 3
# print(a)
# for key, value in a.items():
#    print(f" Key: {key}")
#    print(f" Value: {value}")

# for key in sorted(set(a.values)):
#    print(key)
#
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for l in aliens:
#	print(aliens)

# or
# alien = []
# for aliens in range(20):
#	newaliens = {'color': 'green', 'points': 5}
#	alien.append(newaliens)
# for v in range(5):
#	print(alien[v])

# print(f"The total number of aliens is {len(alien)}")

# for v in alien[0:3]:
#	if v["color"] == "green":
#		v["color"] = "purple"
#		v["points"] = 10
#		print(v)

# pizza = {"toppings": "peperoni", "pizzaSC": [5, "pan"]}

# print(f"You wanted a {pizza['toppings']} with")

# for n in pizza["pizzaSC"]:
#     print(f"{n}")

# favouritelanguages = {"jen": ["python", "ruby"], "sarah": [
#     "c sharp"], "phil": ["python", "haskell"]}
# for names, values in favouritelanguages.items():
# 	print("\n")
# 	print(f"{names} favourite languages were")
# 	for anothervalue in values:
# 		print(f"{anothervalue}")

user = {"Banana": {"Name": "Hellberg", "Age": "20", "Date_Added": 2016},
        "anna": {"Name": "Anna", "Age": 17, "Date_Added": 2019},}
for key, value in user.items():
	print(f"{key}'s name is {value['Name']} and age is {value['Age']} and joined in {value['Date_Added']} ")
	
