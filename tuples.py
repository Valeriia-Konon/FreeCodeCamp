(x, y) = (4, 'fred')
print(y)

#tuples and dict
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

#sorting lists of tuples
d = {'a':10, 'b':1, 'c':22}
print(d.items())
sort = sorted(d.items())
print(sort)
for k,v in sorted(d.items()):
    print(k,v)

#sorting by value
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

print()
#shorter version
g = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))