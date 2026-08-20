Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> # Creating a tuple
>>> t = ()
>>> t = tuple()
>>> t = (1, 2, 3, 4)
>>> t
(1, 2, 3, 4)
>>> # A single element in parentheses is not a tuple
>>> t = (1)
>>> t
1
>>> # It is considered as an integer
>>> t = (1,)
>>> t
(1,)
>>> type(t)
<class 'tuple'>
>>> # Tuple can contain different data types
>>> t = (1, 2, 3, (4, 5, 6), "hello")
>>> t
(1, 2, 3, (4, 5, 6), 'hello')
>>> type(t)
<class 'tuple'>

>>> # Tuple concatenation
>>> (11, 22, 33) + (55, 66, 77)
(11, 22, 33, 55, 66, 77)
>>> # Tuple repetition
>>> (77, 7, 22, 32, 32) * 8
(77, 7, 22, 32, 32, 77, 7, 22, 32, 32, 77, 7, 22, 32, 32, 77, 7, 22, 32, 32, 77, 7, 22, 32, 32, 77, 7, 22, 32, 32, 77, 7, 22, 32, 32, 77, 7, 22, 32, 32)

>>> # Indexing
>>> t = (1, 2, 3, (4, 5, 6), 'hello')
>>> t[1]
2
>>> # Slicing
>>> t[::-1]
('hello', (4, 5, 6), 3, 2, 1)
>>> t[:3]
(1, 2, 3)
>>> t[-1:-3:-1]
('hello', (4, 5, 6))
>>> # Membership operators
>>> '2' in t
False
>>> 2 in t
True
>>> 5 not in t
True
>>> (4, 5, 6) in t
True

>>> # Built-in functions
>>> t = (22, 33, 99, 88, 79, 87, 11, 2, 3, 4)
>>> sorted(t)
[2, 3, 4, 11, 22, 33, 79, 87, 88, 99]
>>> max(t)
99
>>> min(t)
2
>>> len(t)
10
>>> t.index(11)
6

>>> # Tuple can contain mutable objects
>>> t = (34, 34, 233, 54, 23, [2, 34, 4, 5], 89)
>>> t[5].append(6)
>>> t
(34, 34, 233, 54, 23, [2, 34, 4, 5, 6], 89)
>>> t.count(34)
2

>>> # any()
>>> t = ()
>>> type(t)
<class 'tuple'>
>>> any(t)
False
>>> t = (2, 2, 23)
>>> any(t)
True
>>> # sum()
>>> sum(t)
27
>>> # all()
>>> all(t)
True
>>> t = ()
>>> all(t)
True

>>> # Tuple immutability and mutable elements
>>> t = (34, 34, 233, 54, 23, [2, 34, 4, 5], 89)
>>> id(t)
2814208284256
>>> t[5].append(88)
>>> t
(34, 34, 233, 54, 23, [2, 34, 4, 5, 88], 89)
>>> id(t)
2814208284256
>>> # The tuple itself is immutable.
>>> # However, mutable objects such as lists inside a tuple can be modified.
>>> # The tuple's memory identity remains the same.