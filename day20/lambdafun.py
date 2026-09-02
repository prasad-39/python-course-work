'''
var  = lambda arg:exp
'''
'''
wish=lambda name:f'welcome to the course  {name}'
print(wish('prasad'))
print(wish('vinod'))

gst=lambda price:price+price*0.18
print(gst(300))
print(gst(4500))

avg=lambda a,b,c:(a+b+c)/3
print(avg(2,3,4))
print(avg(8,9,7))

iseven=lambda a:'even' if a%2==0  else 'odd'
print(iseven(3))

largest=lambda a,b,c:a if a>b else(b if b>c else c)
print(largest(3,4,2))
print(largest(5,33,2))

isvowel=lambda a: 'vowel' if a in 'aeiouAEIOU' else 'cons'
print(isvowel('b'))
print(isvowel('a'))

#lambda with map 

l=[2,3,4,5,67,77]
update=list(map(lambda i:i+10,l))
print(update)

t=(234,345,786,545,345,567,567,5645,4444)
discount=list(map(lambda i:i-i*0.3,t))
print(discount)


l=[2,3,45,5,6,7,87,653,343,44]
update=list(filter(lambda i:i%2!=0,l))
print(update)

t=(34,343,545,656,57,56,4,43,565,76,754,53,446534,35,455656,33,3445)
update=list(filter(lambda i:i>1000,t))
print(update)
'''
l=['prasad@gmail.com','prasad@yahoo.com','prasad@codegnan.com',]
domain=list(map(lambda i:i.split('@')[1],l))
print(domain)


from functools import reduce
l=[2,34,3,23,422,32]
res=reduce(lambda sum,i:sum+i,l)
print(res)

mul=reduce(lambda pro,i:pro*i,l)
print(mul)

seats={'s1':True,
       's2':False,
       's3':True,
       's4':False,
       's5':True}
avl=list(filter(lambda i:seats[i]==True,seats))
print(avl)


products={
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':50
}
res=list(filter(lambda i: products[i]>50,products))
print(res)

print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))

