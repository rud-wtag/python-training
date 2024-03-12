# # multiple variable assign
# a, b, c = 1, 20.2, "GeeksforGeeks"
# print("multiple variable assign", a, b, c)

# # reading user input ( no matter input user enter input return it as str)
# a = input("Please enter a number: ")
# print(f"you have entered this number { a } and you have entered a {type(a)} data")


# # define a function and calling it
# def test():
#     return "hello for the test"


# print(test())

# # will throw an error
# a, b = 10, "geeks"
# print(a + b)

# # global keyword

# x = 15


# def func():
#     global x
#     x = 16


# func()

# print(x)

"""
types of data structure in python
    - Numeric
    - Text Type
    - Sequence Type (Python list, Python tuple, Python range)
    - Boolean
    - Set
    - Dictionary
"""

a = range(1, 3)
print(a, type(a))

a = "test"
print(a, type(a))

a = "test"
print(a, type(a))

"""
- python list may not be homogeneous, can hold an object or another list thi container
"""

a = [{"name": "x", "age": 23}, [1, 2, 3]]

print(a, type(a), type(a[0]), type(a[1]))


class Student:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def getStudentData(self) -> dict:
    return {"name": self.name, "age": self.age}


test = Student("Mr.x", 23)

print(test.name)
