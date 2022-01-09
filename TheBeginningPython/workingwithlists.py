# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#  print(f"{magician}, wow. That was so pepelol")
# print("So uh that was it.... it's not in the for loop pepeslap")

# for value in range(1,6):
#  print(value)

# listme = list(range(2,11,2))
# print(listme)

# huh = []
# for value in range(1,11):
#     square = value ** 2
#     huh.append(square)
# print(huh)
#or
huh = [value**2 for value in (range(1,11))]
print(huh)

# print(huh[2:7])

# for value in huh[:3]:
#     print(value)

better = huh[:]
print(better)
