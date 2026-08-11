Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4,'str',False,[2,3,4,5],(3,3,3,3,3),{5,3,4,42,11}]
>>> l
[1, 2, 3, 4, 'str', False, [2, 3, 4, 5], (3, 3, 3, 3, 3), {3, 4, 5, 42, 11}]
>>> l=[1,2,2,3,3,3]
>>> l
[1, 2, 2, 3, 3, 3]
>>> a=[44,55,66,6677,88,99]
>>> a
[44, 55, 66, 6677, 88, 99]
>>> a[2]
66
>>> a[3]
6677
>>> a(2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a(2)
TypeError: 'list' object is not callable
>>> a=[3,4,5]
>>> b=[3,7,8]
>>> b=[3,7,8]
>>> a
[3, 4, 5]
>>> a+b
[3, 4, 5, 3, 7, 8]
>>> a*3
[3, 4, 5, 3, 4, 5, 3, 4, 5]
>>> a*10
[3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]
>>> a[:-1]
[3, 4]
>>> a[1:]
[4, 5]
>>> a=[::-1]
SyntaxError: invalid syntax
>>> a[::-1]
[5, 4, 3]
>>> 4 in a
True
>>> 23 not in a
True
>>> 5 in a
True
>>> len(a)
3
>>> #listmethods
>>> a=[22,33,44,55,66,77,77,88]
>>> a
[22, 33, 44, 55, 66, 77, 77, 88]
>>> a.insert(5,99)
>>> a
[22, 33, 44, 55, 66, 99, 77, 77, 88]
>>> a.push(111)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.push(111)
AttributeError: 'list' object has no attribute 'push'
>>> a.append(111)
>>> a
[22, 33, 44, 55, 66, 99, 77, 77, 88, 111]
>>> a.insert(4,22)
>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111]
>>> a.extend([22,09,80,70])
SyntaxError: invalid token
>>> a.extend([22,9,80,70])
>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9, 80, 70]
>>> a.pop()
70
>>> a.pop()
80
>>> a.copy()
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9]
>>> b=a.copy()
>>> b
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9]
>>> a.pop()
9
>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22]
>>> b
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22, 9]
>>> b=a
>>> a
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22]
>>> b
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111, 22]
>>> a.pop()
22
>>> b
[22, 33, 44, 55, 22, 66, 99, 77, 77, 88, 111]
>>> id(a)
1367735287112
>>> id(b)
1367735287112
>>> del a[0:3]
>>> a
[55, 22, 66, 99, 77, 77, 88, 111]
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> a.pop(0)
55
>>> a.remove(99)
>>> a
[22, 66, 77, 77, 88, 111]
>>> a.remove(77,88}
SyntaxError: invalid syntax
>>> 
>>> a.remove(77,88)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.remove(77,88)
TypeError: remove() takes exactly one argument (2 given)
>>> a.clear()
>>> a
[]
>>> a.sort()
>>>sorted(a)
>>>#the difference betwenn sort and sorted is ,sorted doesn't change the original list