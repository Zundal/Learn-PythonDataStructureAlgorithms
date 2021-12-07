'''
Author Name :  Jeong mi Park
Instructor : Robin Andrew From Linkedin Learning
Modified : Dec 06, 2021.
Description : Python Data Structures (A Game-Based Approach) - Utilize the stack class reverse the string message.
'''

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# A simple solution for reversing string
for i in string:
    s.push(i)

# Check stack is empty repeat return data from the stack until the stack is empty
while not s.is_empty():
    reversed_string += s.pop()

# output result message
print(reversed_string)
