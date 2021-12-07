'''
Author Name :  Jeong mi Park
Instructor : Robin Andrew From Linkedin Learning
Modified : Dec 06, 2021.
Description : Python Data Structures (A Game-Based Approach) - Create Stack Class to learn Data Structures and Algorithms
'''

# Stack class to store and retrieve data
class Stack:
    # constructor for Stack class
    def __init__(self):
        self.items = []

    # Check if the Stack is empty
    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)
    # pop method return data and remove data.
    def pop(self):
        return self.items.pop()

    # peek method return data without removing it
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    # __str__ method in Python represents the class objects as a string. (it can be used for classes)
    # __str__ method should be defined to read and outputs all the members of the class
    # __str__ method is called when print(),str() functions are invoked
    # if we did not define __str__ then it will call the __repr__ method instead
    # __repr__ method returns a string that describes the pointer of the object by default (if is is not defined by the programmer)
    def __str__(self):
        return str(self.items)

# Simple test for Stack class
if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s)

    print(s.size())
