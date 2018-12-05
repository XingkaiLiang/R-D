import collections
d=collections.OrderedDict()

e['124']=124
e['123']=25
e['1']=23
#>>> e
#{'1': 23, '123': 25, '124': 124}
d['124']=124
d['123']=25
d['1']=23
#>>> d
#OrderedDict([('124', 124), ('123', 25), ('1', 23)])
#>>> for i in e:
#...     print i,e[i]
#...
#1 23
#123 25
#124 124
#>>> for key in d:
#...     print key,d[key]
#...
#124 124
#123 25
#1 23
