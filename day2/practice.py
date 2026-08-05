Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Prasad/OneDrive/Desktop/python-course work/day2/keywords.py 
Traceback (most recent call last):
  File "C:/Users/Prasad/OneDrive/Desktop/python-course work/day2/keywords.py", line 1, in <module>
    import keywords
  File "C:/Users/Prasad/OneDrive/Desktop/python-course work/day2\keywords.py", line 3, in <module>
    print(keyword.kwlist)
NameError: name 'keyword' is not defined
>>> 
 RESTART: C:/Users/Prasad/OneDrive/Desktop/python-course work/day2/keywords.py 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> 
