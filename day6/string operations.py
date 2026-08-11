Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n='prasad'
>>> n
'prasad'
>>> n="prasad"
>>> n
'prasad'
>>> type(n)
<class 'str'>
>>> firstname='prasad'
>>> lastname='Gurram'
>>> firstname
'prasad'
>>> lastname
'Gurram'
>>> firstname+lastname
'prasadGurram'
>>> a='apple'
>>> a*10
'appleappleappleappleappleappleappleappleappleapple'
>>> firstname*10
'prasadprasadprasadprasadprasadprasadprasadprasadprasadprasad'
>>> firstname+10
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    firstname+10
TypeError: can only concatenate str (not "int") to str
>>> firstname+'10'
'prasad10'
>>> '*'*10
'**********'
>>> #indexing
>>> avengers='thor spiderman ironman hulk'
>>> avengers[0:3]
'tho'
>>> avengers[0:4]
'thor'
>>> avengers[0:4  , 5:15]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    avengers[0:4  , 5:15]
TypeError: string indices must be integers
>>> avengers[0:4,5:15]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    avengers[0:4,5:15]
TypeError: string indices must be integers
>>> avengers[5:15]
'spiderman '
>>> avengers[-1:-5]
''
>>> avengers[-1:-5]
''
>>> avengers[-1:-6]
''
>>> avengers[-6:-1]
'n hul'
>>> avengers[:-8]
'thor spiderman iron'
>>> avengers[-1:-5:-1]
'kluh'
>>> 'thor' in avengers
True
>>> spiderman not in avengers
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    spiderman not in avengers
NameError: name 'spiderman' is not defined
>>> 'spiderman' not in avengers
False
>>> #methods of string
>>> s='spiderman'
>>> len(s)
9
>>> crd(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    crd(s)
NameError: name 'crd' is not defined
>>> ord(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    ord(s)
TypeError: ord() expected a character, but string of length 9 found
>>> chr(s)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    chr(s)
TypeError: an integer is required (got type str)
>>> ord(m)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ord(m)
NameError: name 'm' is not defined
>>> ord('m')
109
>>> chr(5050)
'Ꮊ'
>>> chr(30)
'\x1e'
>>> chr(78)
'N'
>>> ord('n')
110
>>> sorted(s)
['a', 'd', 'e', 'i', 'm', 'n', 'p', 'r', 's']
>>> sorted(avengers)
[' ', ' ', ' ', 'a', 'a', 'd', 'e', 'h', 'h', 'i', 'i', 'k', 'l', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 'r', 's', 't', 'u']
>>> max(s)
's'
>>> min(s)
'a'
>>> max(avengers)
'u'
>>> #case convertion
>>> s='hello i am prasad'
>>> s.upper()
'HELLO I AM PRASAD'
>>> s.lower()
'hello i am prasad'
>>> s.title()
'Hello I Am Prasad'
>>> s.capitalize()
'Hello i am prasad'
>>> s.swapcase()
'HELLO I AM PRASAD'
>>> s='hELLO prasad'
>>> s.swapcse()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.swapcse()
AttributeError: 'str' object has no attribute 'swapcse'
>>> s.swapcase()
'Hello PRASAD'
>>> s.casefold()
'hello prasad'
>>> s.center()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s.center()
TypeError: center() takes at least 1 argument (0 given)
>>> s.center(30)
'         hELLO prasad         '
>>> s.center(60,'-')
'------------------------hELLO prasad------------------------'
>>> s.center(80,'*')
'**********************************hELLO prasad**********************************'
>>> s.ljust(40)
'hELLO prasad                            '
>>> s.rjust(30)
'                  hELLO prasad'
>>> '23233'.zfill(12)
'000000023233'
>>> '2'.zfill(20)
'00000000000000000002'
>>> 'app'.zfill(10)
'0000000app'
>>> 10.zfill(10)
SyntaxError: invalid syntax
>>> s='prasad'
>>> s='python programming '
>>> s.index('p')
0
>>> s.index('programming')
7
>>> s.rindex(n)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.rindex(n)
ValueError: substring not found
>>> s.rindex('n')
16
>>> s.find('p')
0
>>> s.find(2)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s.find(2)
TypeError: must be str, not int
>>> s.find('python')
0
\
>>> s.find('z')
-1
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> #major difference b/w index and find is exception handling
>>> s='thor is powerful character in avengers '
>>> s.maketrans('thor','spiderman')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.maketrans('thor','spiderman')
ValueError: the first two maketrans arguments must have equal length
>>> s.maketrans('thor','hulk')
{116: 104, 104: 117, 111: 108, 114: 107}
>>> s.translate(maketrans('thor','hulk'))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.translate(maketrans('thor','hulk'))
NameError: name 'maketrans' is not defined
>>> s.translate(s.maketrans('thor','hulk'))
'hulk is plwekful cuakachek in avengeks '
>>> text='hello'
>>> text.encode()
b'hello'
>>> b'hello'.decode()
'hello'
>>> text.encode('hiden')
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    text.encode('hiden')
LookupError: unknown encoding: hiden
>>> 
