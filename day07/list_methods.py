Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> # Creating a list
>>> l = []
>>> l = list()
>>> type(l)
<class 'list'>

>>> # List can contain different data types
>>> l = [1, 2, 3, 4, 'str', False, [2, 3, 4, 5], (3, 3, 3, 3, 3), {5, 3, 4, 42, 11}]
>>> l
[1, 2, 3, 4, 'str', False, [2, 3, 4, 5], (3, 3, 3, 3, 3), {3, 4, 5, 42, 11}]

>>> # List allows duplicate elements
>>> l = [1, 2, 2, 3, 3, 3]
>>> l
[1, 2, 2, 3, 3, 3]

>>> # Indexing
>>> a = [44, 55, 66, 6677, 88, 99]
>>> a
[44, 55, 66, 6677, 88, 99]
>>> a[2]
66
>>> a[3]
6677

>>> # Lists are indexed using square brackets
>>> a(2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a(2)
TypeError: 'list' object is not callable

>>> # List concatenation
>>> a = [3, 4, 5]
>>> b = [3, 7, 8]
>>> a + b
[3, 4, 5, 3, 7, 8]

>>> # List repetition
>>> a * 3
[3, 4, 5, 3, 4, 5, 3, 4, 5]

>>> a * 10
[3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]

>>> # Slicing
>>> a[:-1]
[3, 4]

>>> a[1:]
[4, 5]

>>> a[::-1]
[5, 4, 3]

>>> # Membership operators
>>> 4 in a
True

>>> 23 not in a
True

>>> 5 in a
True

>>> # Length
>>> len(a)
3


>>> # List methods
>>> a = [22, 33, 44, 55, 66, 77, 77, 88]
>>> a
[22, 33, 44, 55, 66, 77, 77, 88]

>>> # insert()
>>> a.insert(5, 99)
>>> a
[22, 33, 44, 55, 66, 99, 77, 77, 88]

>>> # Lists do not have a push() method
>>> a.push(111)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>

>>> # append()
>>> a.append(111)
>>> a
[22, 33, 44, 55, 66, 99, 77, 77, 88, 111]

>>> # insert() at a specific position
>>> a.insert(4, 22)
>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111]

>>> # extend()
>>> a.extend([22, 9, 80, 70])
>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9, 80, 70]

>>> # pop()
>>> a.pop()
70

>>> a.pop()
80

>>> # copy()
>>> a.copy()
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9]

>>> b = a.copy()
>>> b
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9]

>>> a.pop()
9

>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22]

>>> b
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9]


>>> # Assignment creates another reference to the same list
>>> b = a
>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22]

>>> b
[22, 33, 44, 55, 22, 66, 77, 77, 88, 111, 22]

>>> a.pop()
22

>>> b
[22, 33, 44, 55, 22, 66, 77, 77, 88, 111]

>>> id(a)
1367735287112

>>> id(b)
1367735287112


>>> # del
>>> del a[0:3]
>>> a
[55, 22, 66, 77, 77, 88, 111]

>>> # del removes the variable completely
>>> del b


>>> # pop() removes an element using its index
>>> a.pop(0)
55

>>> # remove() removes a specific value
>>> a.remove(77)
>>> a
[22, 66, 77, 88, 111]

>>> # remove() accepts only one argument
>>> a.remove(77, 88)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.remove(77, 88)
TypeError: remove() takes exactly one argument (2 given)

>>> # clear() removes all elements
>>> a.clear()
>>> a
[]

>>> # sort() and sorted()
>>> a = [50, 20, 80, 10, 40]

>>> a.sort()
>>> a
[10, 20, 40, 50, 80]

>>> # sorted() returns a new sorted list
>>> a = [50, 20, 80, 10, 40]
>>> sorted(a)
[10, 20, 40, 50, 80]

>>> a
[50, 20, 80, 10, 40]

>>> # Difference between sort() and sorted()
>>> # sort() changes the original list.
>>> # sorted() does not change the original list.