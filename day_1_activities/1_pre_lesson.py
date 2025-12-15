# this is what we will use for the video intro to dictionaries
# dictionary = a collection of {key:value} pairs
#              ordered and changeable, no duplicates allowed
#You may also never use Numbers

capitals = {"USA": "Washington D.C.", "India":"New Delhi", "China":"Bejing", "Russia":"Moscow"}
print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})
capitals.pop("China") #Removes selected item
capitals.popitem() #Removes the latest item
capitals.clear #Clears the dictionary

keys = capitals.keys

for key in capitals.keys:
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")