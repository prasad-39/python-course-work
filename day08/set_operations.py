Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> # Creating a set
>>> s = set()
>>> type(s)
<class 'set'>

>>> s = {}
>>> type(s)
<class 'dict'>

>>> # Empty set must be created using set()
>>> # {} creates an empty dictionary.

>>> s = {4, 3, 5, 4, 2, 2354353, 43, 54, 4336, 4, 4, 4, 4, 4, 4, 23, 55, 44, 56, 77, 99}
>>> type(s)
<class 'set'>
>>> s
{2, 3, 4, 5, 99, 43, 44, 77, 4336, 2354353, 55, 54, 23, 56}

>>> # add()
>>> s.add(1)
>>> s
{1, 2, 3, 4, 5, 99, 43, 44, 77, 4336, 2354353, 55, 54, 23, 56}

>>> s.add(12.3)
>>> s
{1, 2, 3, 4, 5, 99, 43, 44, 77, 12.3, 4336, 2354353, 55, 54, 23, 56}

>>> s.add('program')
>>> s
{1, 2, 3, 4, 5, 99, 43, 44, 77, 12.3, 4336, 2354353, 55, 54, 23, 56, 'program'}

>>> # Sets cannot contain mutable data types
>>> s.add([2, 2, 2, 3])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add([2, 2, 2, 3])
TypeError: unhashable type: 'list'

>>> s.add({3, 3, 45, 6, 7})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add({3, 3, 45, 6, 7})
TypeError: unhashable type: 'set'

>>> s.add({'name': 'prasad'})
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.add({'name': 'prasad'})
TypeError: unhashable type: 'dict'

>>> # Immutable data types can be added to a set
>>> s.add((34, 45, 66, 78))
>>> s
{1, 2, 3, 4, 5, 99, 43, 44, 77, 12.3, 4336, 2354353, (34, 45, 66, 78), 55, 54, 23, 56, 'program'}

>>> s.add(False)
>>> s
{False, 1, 2, 3, 4, 5, 12.3, (34, 45, 66, 78), 23, 43, 44, 2354353, 54, 55, 56, 77, 'program', 99, 4336}


>>> # Set operations
>>> a = {1, 2, 3, 4, 5}
>>> b = {3, 4, 5, 7, 8}

>>> 2 in a
True

>>> 3 not in a
False

>>> # Union
>>> a | b
{1, 2, 3, 4, 5, 7, 8}

>>> # Intersection
>>> a & b
{3, 4, 5}

>>> # Difference
>>> a - b
{1, 2}

>>> b - a
{8, 7}

>>> # Subset
>>> {1} <= a
True

>>> {1, 2, 3} <= a
True

>>> {7, 8} <= b
True

>>> # Superset
>>> a >= {1}
True

>>> a >= {1, 2, 3}
True

>>> # Disjoint sets
>>> m = {2, 3, 4}
>>> n = {5, 6, 7}
>>> n.isdisjoint(m)
True


>>> # Built-in functions with sets
>>> s = {33, 44, 53, 32, 533, 5, 3, 5, 2, 4, 2}
>>> sorted(a)
[1, 2, 3, 4, 5]

>>> max(s)
533

>>> min(s)
2

>>> len(s)
9

>>> # Sets do not support indexing
>>> s.index(32)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.index(32)
AttributeError: 'set' object has no attribute 'index'

>>> sum(s)
709

>>> any(s)
True


>>> # Assignment and copy
>>> a = {1, 2, 3}
>>> b = a
>>> b.add(4)

>>> a
{1, 2, 3, 4}

>>> b
{1, 2, 3, 4}

>>> # b and a refer to the same set
>>> c = a.copy()
>>> c
{1, 2, 3, 4}

>>> a.add(23)
>>> a.add(67)

>>> a
{1, 2, 3, 4, 67, 23}

>>> b
{1, 2, 3, 4, 67, 23}

>>> # clear()
>>> b.clear()
>>> b
set()


>>> # remove() and discard()
>>> s = {33, 44, 53, 32, 533, 5, 3, 5, 2, 4, 2}
>>> s
{32, 33, 2, 3, 4, 5, 44, 533, 53}

>>> s.remove(3)
>>> s
{32, 33, 2, 4, 5, 44, 533, 53}

>>> s.discard(4)
>>> s
{32, 33, 2, 5, 44, 533, 53}

>>> # discard() does not raise an error if the element is not present
>>> s.discard(112233)

>>> # remove() raises KeyError if the element is not present
>>> s.remove(112233)
Traceback (most recent call last):
  File "<pyshell#76", line 1, in <module>
    s.remove(112233)
KeyError: 112233


>>> # Frozenset
>>> a = frozenset({98, 67, 65, 34, 32})
>>> a
frozenset({32, 34, 65, 67, 98})

>>> # Frozenset is an immutable set
>>> a.add(23)
Traceback (most recent call last):
  File "<pyshell#82", line 1, in <module>
    a.add(23)
AttributeError: 'frozenset' object has no attribute 'add'

>>> a.clear()
Traceback (most recent call last):
  File "<pyshell#83", line 1, in <module>
    a.clear()
AttributeError: 'frozenset' object has no attribute 'clear'

>>> # Frozenset cannot be modified using add(), remove(), discard(), or clear().
>>> # However, a frozenset can be deleted using del.
>>> del a