from copy import copy, deepcopy

countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

# nations = countries[:]
# print(id(nations) == id(countries))
# print(nations[0] == countries[0])

# nations = countries.copy()
# print(id(nations) == id(countries))
# print(nations[0] == countries[0])

# nations = copy(countries)
# print(id(nations) == id(countries))
# print(nations[0] == countries[0])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# copy_matrix = copy(matrix)

# matrix[0][1] = 200
# matrix[1][1] = 500
# matrix[2][1] = 800

# print(matrix, copy_matrix)

# deepcopy_matrix = deepcopy(matrix)

# matrix[0][1] = 200
# matrix[1][1] = 500
# matrix[2][1] = 800

# print(matrix, deepcopy_matrix)

# print((countries))