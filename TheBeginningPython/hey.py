example = ["hey","there","is","hello","eat","something"]
example.append("no")
print(f"There is a spider? {example[-1]}")
example.insert(2, "no")
del example[0]
print(example)
popped = example.pop(2)
print(popped)
print(example)
thing = "hello"
example.remove(thing)
print(f" {thing} was removed for being sus")