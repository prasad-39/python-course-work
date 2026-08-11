Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s='         python   programming          '
>>> s.strip()
'python   programming'
>>> s.lstrip()
'python   programming          '
>>> s.rstrip()
'         python   programming'
>>> s.replace(' ','')
'pythonprogramming'
>>> s='java-python-flask-mysql-fastapi'
>>> s.split(-)
SyntaxError: invalid syntax
>>> s.split('-')
['java', 'python', 'flask', 'mysql', 'fastapi']
>>> s.rsplit('-')
['java', 'python', 'flask', 'mysql', 'fastapi']
>>> s.rsplit('-',2)
['java-python-flask', 'mysql', 'fastapi']
>>> s.split('-',2)
['java', 'python', 'flask-mysql-fastapi']
>>> l='python
SyntaxError: EOL while scanning string literal
>>> l='''python
java
sql
flask''''
SyntaxError: EOL while scanning string literal
>>> l='''python
java
sql
flask'''
>>> l
'python\njava\nsql\nflask'
>>> l.splitlines()
['python', 'java', 'sql', 'flask']
>>> ''.join(l)
'python\njava\nsql\nflask'
>>> c=['python','java','sql','flask']
>>> ''.join(c)
'pythonjavasqlflask'
>>> '-'.join(c)
'python-java-sql-flask'
>>> '@'.join(('1','2','3'))
'1@2@3'
>>> a.partition('-')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.partition('-')
NameError: name 'a' is not defined
>>> d='helloworld.pythonfile'
>>> d.partition('.')
('helloworld', '.', 'pythonfile')
>>> d='hello-pythonfile''
SyntaxError: EOL while scanning string literal
>>> 
>>> d='hello-pythonfile'
>>> d.partition('-')
('hello', '-', 'pythonfile')
>>> d.rpartition('n')
('hello-pytho', 'n', 'file')
>>> a='string.png'
>>> a.startswith('S')
False
>>> a.startswith('s')
True
>>> a.endswith('g')
True
>>> a.islower()
True
>>> a.isalphanum()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'
>>> a.isalphanum()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'
>>> 'helloworld'.isalphanum()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    'helloworld'.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'
>>> 'HELLO'.isupper()
True
>>> 'hellow112'.isalnum()
True
>>> a.isalnum()
False
>>> a.isspace()
False
>>> ' '.isspace()
True
>>> s='python program'
>>> s.isspace()
False
>>> s.istitle()
False
>>> 'H@##$$%^^'.istitle()
True
>>> m='H@##$$%^^'
>>> m.isupper()
True
>>> m.islower()
False
>>> m.isalnum()
False
>>> m='Haa@##$$%^^'
>>> m.islower()
False
>>> m.isupper()
False
>>> '_______'.isidentifier()
True
>>> '442232323'.isdecimal()
True
>>> '223311'.isdigit()
True
>>> '34987'.numeric()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    '34987'.numeric()
AttributeError: 'str' object has no attribute 'numeric'
>>> '34897'.isnumeric()
True
>>> 
