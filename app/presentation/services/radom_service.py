# from functools import reduce
# import csv

# set_a = {"col", "mex", "bol"}
# set_be = {"pe", "bol"}

# !union
# set_c = set_a.union(set_be)
# print(set_c)  # {'col', 'mex', 'pe', 'bol'}
# print(set_a | set_be)  # {'col', 'mex', 'pe', 'bol'}


# !intersection
# set_c = set_a.intersection(set_be)
# print(set_c)  # {'bol'}
# print(set_a & set_be)  # {'bol'}


# !difference
# set_c = set_a.difference(set_be)
# print(set_c)  # {'col', 'mex'}
# print(set_a - set_be)  # {'col', 'mex'}


# !symetric difference
# set_c = set_a.symmetric_difference(set_be)
# print(set_c)  # {'col', 'mex', 'pe'}


# countries = {"MX", "COL", "ARG", "USA"}
# northAm = {"USA", "CANADA"}
# centralAm = {"MX", "GT", "BZ"}
# southAm = {"COL", "BZ", "ARG"}
# new_set = countries | northAm | centralAm | southAm
# print(new_set)

# !list comprehension
# numbers = [i * 2 for i in range(1, 10) if i % 2 == 0]
# print(numbers)


# !dictionary comprehension
# dict_2 = {i: i * 2 for i in range(1, 11)}
# print(dict_2)

# dict = {}
# for i in range(1, 11):
#     dict[i] = i * 2
# print(dict)

# import random
# countries = ["MX", "COL", "ARG", "USA"]
# population = {country: random.randint(1, 100) for country in countries}
# print(population)

# names = ["nico", "zule", "santi"]
# ages = [20, 30, 40]
# dict = {name: age for (name, age) in zip(names, ages) if age >= 30}
# print(dict)

# text = "hello"
# unique = {c: c.upper() for c in text if c in "aeiou"}

# person = {"name": "pepe", "age": 22}
# age, name = person.values()
# print(age, name)

# !reduce
# print(reduce(lambda acc, number: acc + number, [1, 2, 3]))


#!iterators
# sirven para trabajar con un gran cantidad de datos ya que hace carga perezosa

# interator = iter([1, 2, 3])
# print(next(interator))
# print(next(interator))



# !read files

# with open("paises.csv") as paises:
#     content = paises.read()
#     print(content)

# with open("../../store/paises.csv", newline="") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
