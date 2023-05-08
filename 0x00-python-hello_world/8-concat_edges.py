#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
py_ = str[:6]
oop = str[39:67]
str = oop + " " + str[-22:-18] + " " + py_
print(str)
