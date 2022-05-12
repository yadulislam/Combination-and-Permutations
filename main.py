import itertools
my_list = ["Rock","Paper","Scissors"]
combination = itertools.combinations(my_list,2)#order does not matter
permutations = itertools.permutations(my_list, 2)#order matters.
for c in combination:
    print(c)


for p in permutations:
    print(list(p))
word = "not"
my_letter = "ton"
combination = itertools.combinations(my_letter, 3)
permutations = itertools.permutations(my_letter, 3)
for c in combination:#dosen't care about order.
    print(c)
for p in permutations:
    if ''.join(p) == word:#check every single combination with order.
        print("match found.")
        break