# Write a Python program to convert a tuple to a string.
def convertTuple(tuple):
    str = ''
    for i in tuple:
        str = str + i
    return str

tuple = ('a', 'n', 't')
str = convertTuple(tuple)
print(str)
