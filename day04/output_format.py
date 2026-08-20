Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=12.5
>>> c="hello"
>>> print(a,b,c)
10 12.5 hello
>>> print('a=',b,'b=',b,'c=',c)
a= 12.5 b= 12.5 c= hello
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
12.5
c=
hello
>>> print('a=',a,'b=',b,'c=',sep='\t',end='Hehe')
a=	10	b=	12.5	c=Hehe
>>> print('a=',a,'b=',b,'c='c,sep='\t',end='Hehe')
SyntaxError: invalid syntax
>>> print('a=',a,'b=',b,'c=',c,sep='\t',end='Hehe')
a=	10	b=	12.5	c=	helloHehe
>>> print('c=',c,end='this is the end' )
c= hellothis is the end
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.5 c=hello
>>> print('a={} b={} c={}'.format(a,c,b))
a=10 b=hello c=12.5
>>> 
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.5 c=hello
>>> print('a={} b={} c={}'.format(c,a,c))
a=hello b=10 c=hello
>>> print('a={} b={} c={}'.format(a,a,a))
a=10 b=10 c=10
>>> 
