# Week 1.3, Session 1: For loop equivalent to a list comprehension
not_fish2=[]
animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)

for item in animals:
    if item != 'goldfish':
        not_fish2.append(item)
print(not_fish2)

# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same

