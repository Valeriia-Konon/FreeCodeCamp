purse = dict()
purse['money'] = 32
purse['candy'] = 3
purse['mouse'] = 73
print(purse)

purse['candy'] = purse['candy'] + 2
print(purse)

print()
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)

print() #applications
counts = dict()
names = ['csev', 'cwen', 'csev', 'cwen', 'zqian']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)
print(x)

counts = dict()
names = ['csev', 'cwen', 'csev', 'cwen', 'zqian']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

print()
count = dict()
line = input('Enter a line of text: ')
words = line.split()

print(f'Words: {words}')
print('Counting...')
for word in words:
    count[word] = count.get(word, 0) + 1
print(f'Counts: {count}')
