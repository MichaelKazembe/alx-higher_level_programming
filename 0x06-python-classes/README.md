## 0x06. Python - Classes and Objects

**What you should learn from this project**

       At the end of this project you are expected to be able to
       explain to anyone, without the help of Google:

* Why Python programming is awesome (don’t forget to tweet today,
  with the hashtag #pythoniscool :))
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* advanced:

**advanced:**

* How to dynamically create arbitrary new attributes for existing
  instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an
  instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

**Exercises**

**0. My first square**

     Write an empty class Square that defines a square:

You are not allowed to import any module
guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$

* You are not allowed to import any module

**1. Square with size**

     Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/0x06$ 

**2. Size validation**

     Write a class Square that defines a square by:
     (based on 1-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
* size must be an integer, otherwise raise a TypeError exception
  with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message * size must be >= 0
* You are not allowed to import any module

**3. Area of a square**

     Write a class Square that defines a square by:
     (based on 2-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
  * size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
  * if size is less than 0, raise a ValueError exception with
    the message size must be >= 0
* Public instance method: def area(self): that returns the
  current square area
* You are not allowed to import any module

**4. Access and update private attribute**

     Write a class Square that defines a square by:
     (based on 3-square.py)

* Private instance attribute: size:
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception
      with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with
      the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current
  square area
* You are not allowed to import any module

**5. Printing a square**

     Write a class Square that defines a square by:
     (based on 4-square.py)

* Private instance attribute: size:
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError
      exception with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with
      the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current
  square area
* Public instance method: def my_print(self): that prints in stdout
  the square with the character #:
  * if size is equal to 0, print an empty line
* You are not allowed to import any module

**6. Coordinates of a square**

     Write a class Square that defines a square by:
     (based on 5-square.py)

* Private instance attribute: size:
  * property def size(self): to retrieve it
  * property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception
      with the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the
      message size must be >= 0
* Private instance attribute: position:
  * property def position(self): to retrieve it
  * property setter def position(self, value): to set it:
    * position must be a tuple of 2 positive integers, otherwise
      raise a TypeError exception with the message position must
      be a tuple of 2 positive integers
* Instantiation with optional size and optional position:
  def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current
  square area
* Public instance method: def my_print(self): that prints in stdout
  the square with the character #:
  * if size is equal to 0, print an empty line
  * position should be use by using space
* You are not allowed to import any module
