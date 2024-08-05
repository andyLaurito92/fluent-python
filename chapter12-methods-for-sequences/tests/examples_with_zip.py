"""
Examples on using zip
"""

print("Returns a zip object")
res = zip([1, 2, 3], [4, 5, 6])
print(help(res))
list(res)

list(zip(range(3), "ABC"))

"""
Zip can be used for transposing matrixes
"""

mymatrix = [(1, 2, 3), (4, 5, 6)]

"""
Every row is sent as argument to the zip function, making the i-th element a tuple
consisting of all values in the column. This tuple corresponds to the i-th row of the
transpose matrix
"""
transpose = list(zip(*mymatrix))
print(transpose)
