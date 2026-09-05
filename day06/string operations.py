Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information. 

>>> # String
>>> n = 'prasad'
>>> n
'prasad'
>>> n = "prasad"
>>> n
'prasad'
>>> type(n)
<class 'str'>

>>> # String concatenation
>>> firstname = 'prasad'
>>> lastname = 'Gurram'
>>> firstname
'prasad'
>>> lastname
'Gurram'
>>> firstname + lastname
'prasadGurram'
>>> firstname + ' ' + lastname
'prasad Gurram'

>>> # String repetition
>>> a = 'apple'
>>> a * 10
'appleappleappleappleappleappleappleappleappleapple'
>>> firstname * 10
'prasadprasadprasadprasadprasadprasadprasadprasadprasadprasad'
>>> '*' * 10
'**********'
>>> firstname + 10
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    firstname + 10
TypeError: can only concatenate str (not "int") to str
>>> firstname + '10'
'prasad10'

>>> # Indexing and slicing
>>> avengers = 'thor spiderman ironman hulk'
>>> avengers[0]
't'
>>> avengers[0:3]
'tho'
>>> avengers[0:4]
'thor'
>>> avengers[5:15]
'spiderman '
>>> avengers[-1]
'k'
>>> avengers[-6:-1]
'n hul'
>>> avengers[:-8]
'thor spiderman iron'
>>> avengers[-1:-5:-1]
'kluh'

>>> # Membership operators
>>> 'thor' in avengers
True
>>> 'spiderman' not in avengers
False

>>> # String functions
>>> s = 'spiderman'
>>> len(s)
9
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

>>> # Case conversion
>>> s = 'hello i am prasad'
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
>>> s = 'hELLO prasad'
>>> s.swapcase()
'Hello PRASAD'
>>> s.casefold()
'hello prasad'

>>> # String alignment
>>> s.center(30)
'         hELLO prasad         '
>>> s.center(60, '-')
'------------------------hELLO prasad------------------------'
>>> s.center(80, '*')
'**********************************hELLO prasad**********************************'
>>> s.ljust(40)
'hELLO prasad                            '
>>> s.rjust(30)
'                  hELLO prasad'

>>> # zfill()
>>> '23233'.zfill(12)
'000000023233'
>>> '2'.zfill(20)
'00000000000000000002'
>>> 'app'.zfill(10)
'0000000app'

>>> # Searching in strings
>>> s = 'python programming '
>>> s.index('p')
0
>>> s.index('programming')
7
>>> s.rindex('n')
16
>>> s.find('p')
0
>>> s.find('python')
0
>>> s.find('z')
-1
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s.index('z')
ValueError: substring not found

>>> # Difference between index() and find()
>>> # index() raises ValueError when the substring is not found.
>>> # find() returns -1 when the substring is not found.

>>> # maketrans() and translate()
>>> s = 'thor is powerful character in avengers'
>>> s.maketrans('thor', 'hulk')
{116: 104, 104: 117, 111: 108, 114: 107}
>>> s.translate(s.maketrans('thor', 'hulk'))
'hulk is plwekful cuakachek in avengeks'

>>> # Encoding
>>> text = 'hello'
>>> text.encode()
b'hello'
>>> text.encode('utf-8')
b'hello'

>>> # Decoding
>>> b'hello'.decode()
'hello'
>>> b'hello'.decode('utf-8')
'hello'
