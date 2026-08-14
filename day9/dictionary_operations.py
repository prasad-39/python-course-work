Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #dictionary operations
>>> d={}
>>> type(d)
<class 'dict'>
>>> d={1:2,4:5,8:9,3:9}
>>> d
{1: 2, 4: 5, 8: 9, 3: 9}
>>> d
{1: 2, 4: 5, 8: 9, 3: 9}
>>> del d
>>> d={}
>>> d[1]=1
>>> d[2,3]=3
>>> d['str']=3
>>> d[(1,2,3,3,4)]=4
>>> d[(3+3j)]=5
>>> d[True]=9
>>> del d
>>> d={}
>>> d[1]=23
>>> d[34]='str'
>>> d[45]=12+4j
>>> d[55]=(1,23,44,4)
>>> d[22]=34.21
>>> d[54]=False
>>> d[99]=[3,4,2,23,343,4]
>>> d[98]={2:3,4:4,2:9}
>>> #In keys lists, set, dictionaries are not allowed
>>> d
{1: 23, 34: 'str', 45: (12+4j), 55: (1, 23, 44, 4), 22: 34.21, 54: False, 99: [3, 4, 2, 23, 343, 4], 98: {2: 9, 4: 4}}
>>> d[455]=None
>>> d
{1: 23, 34: 'str', 45: (12+4j), 55: (1, 23, 44, 4), 22: 34.21, 54: False, 99: [3, 4, 2, 23, 343, 4], 98: {2: 9, 4: 4}, 455: None}
>>> info={'name':'prasad','course':'pfs','batch':65}
>>> info['name']
'prasad'
>>> 'prasad' in info
False
>>> 'name' in info
True
>>> info.get('name')
'prasad'
>>> info.get('prasad')
>>> info.get('course')
'pfs'
>>> 'batch' in info
True
>>> 65 in info
False
>>> 'pfs' in info
False
>>> info['phno']=9876543210
>>> info
{'name': 'prasad', 'course': 'pfs', 'batch': 65, 'phno': 9876543210}
>>> info.update({'email':'prasad233232@gmail.com','py':2026})
>>> info
{'name': 'prasad', 'course': 'pfs', 'batch': 65, 'phno': 9876543210, 'email': 'prasad233232@gmail.com', 'py': 2026}
>>> d.clear()
>>> d
{}
>>> #we can't modify the keys in dictionary
>>> info={'name':'prasad','course':'pfs','batch':65}
>>> info.pop('batch')
65
>>> info.pop('course')
'pfs'
>>> info
{'name': 'prasad'}
>>> len(info)
1
>>> info={'name':'prasad','course':'pfs','batch':65}
>>> info
{'name': 'prasad', 'course': 'pfs', 'batch': 65}
>>> info.keys()
dict_keys(['name', 'course', 'batch'])
>>> info.values()
dict_values(['prasad', 'pfs', 65])
>>> info.items()
dict_items([('name', 'prasad'), ('course', 'pfs'), ('batch', 65)])
>>> sorted(info)
['batch', 'course', 'name']
>>> max(info)
'name'
>>> min(data)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    min(data)
NameError: name 'data' is not defined
>>> min(info)
'batch'
>>> d={1:1,2:4,5:5}
>>> m=d
>>> m[4]:4
>>> m
{1: 1, 2: 4, 5: 5}
>>> d
{1: 1, 2: 4, 5: 5}
>>> n=d.copy()
>>> n[5]=8778
>>> n
{1: 1, 2: 4, 5: 8778}
>>> d
{1: 1, 2: 4, 5: 5}
>>> info={'name':'prasad','course':'pfs','batch':65}
>>> info.get('name')
'prasad'
>>> info.setdefault('batch','java')
65
>>> info.setdefault('gender','male')
'male'
>>> info
{'name': 'prasad', 'course': 'pfs', 'batch': 65, 'gender': 'male'}
>>> dict.fromkeys(["python","java","mysql"],33)
{'python': 33, 'java': 33, 'mysql': 33}
>>> 
