Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> # strip(), lstrip(), rstrip()
>>> s = '         python   programming          '
>>> s.strip()
'python   programming'
>>> s.lstrip()
'python   programming          '
>>> s.rstrip()
'         python   programming'

>>> # replace()
>>> s.replace(' ', '')
'pythonprogramming'

>>> # split() and rsplit()
>>> s = 'java-python-flask-mysql-fastapi'
>>> s.split('-')
['java', 'python', 'flask', 'mysql', 'fastapi']
>>> s.rsplit('-')
['java', 'python', 'flask', 'mysql', 'fastapi']
>>> s.rsplit('-', 2)
['java-python-flask', 'mysql', 'fastapi']
>>> s.split('-', 2)
['java', 'python', 'flask-mysql-fastapi']

>>> # Multiline string
>>> l = '''python
... java
... sql
... flask'''
>>> l
'python\njava\nsql\nflask'

>>> # splitlines()
>>> l.splitlines()
['python', 'java', 'sql', 'flask']

>>> # join()
>>> ''.join(l)
'python\njava\nsql\nflask'

>>> c = ['python', 'java', 'sql', 'flask']
>>> ''.join(c)
'pythonjavasqlflask'
>>> '-'.join(c)
'python-java-sql-flask'
>>> '@'.join(('1', '2', '3'))
'1@2@3'

>>> # partition()
>>> d = 'helloworld.pythonfile'
>>> d.partition('.')
('helloworld', '.', 'pythonfile')

>>> d = 'hello-pythonfile'
>>> d.partition('-')
('hello', '-', 'pythonfile')

>>> # rpartition()
>>> d.rpartition('n')
('hello-pytho', 'n', 'file')

>>> # startswith() and endswith()
>>> a = 'string.png'
>>> a.startswith('S')
False
>>> a.startswith('s')
True
>>> a.endswith('g')
True

>>> # Case checking
>>> a.islower()
True
>>> 'HELLO'.isupper()
True

>>> # isalnum()
>>> 'hellow112'.isalnum()
True
>>> a.isalnum()
False

>>> # isspace()
>>> a.isspace()
False
>>> ' '.isspace()
True
>>> s = 'python program'
>>> s.isspace()
False

>>> # istitle()
>>> s.istitle()
False
>>> 'Hello World'.istitle()
True

>>> # String containing only special characters
>>> m = 'H@##$$%^^'
>>> m.isupper()
True
>>> m.islower()
False
>>> m.isalnum()
False

>>> # String containing uppercase, lowercase and special characters
>>> m = 'Haa@##$$%^^'
>>> m.islower()
False
>>> m.isupper()
False

>>> # isidentifier()
>>> '_______'.isidentifier()
True
>>> 'python123'.isidentifier()
True
>>> '123python'.isidentifier()
False

>>> # isdecimal()
>>> '442232323'.isdecimal()
True

>>> # isdigit()
>>> '223311'.isdigit()
True

>>> # isnumeric()
>>> '34897'.isnumeric()
True

>>> # Difference between isdecimal(), isdigit() and isnumeric()
>>> # isdecimal() checks for decimal characters.
>>> # isdigit() checks for digit characters.
>>> # isnumeric() checks for numeric characters.