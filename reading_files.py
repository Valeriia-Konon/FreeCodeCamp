stuff = 'Hello\nWorld' #new line Character in strings
print(stuff)

#sequence in the file (for)
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

print()
fhand = open('mbox.txt') #counting lines of the file
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

print()
fhand = open('mbox.txt')
inp = fhand.read() #a whole text is in a single string
print(len(inp))
print(inp[:20])

print()
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('To'):
        print(line)

print()
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('To synchronize') :
        continue
    print(line)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print(f'File {fname} cannot be found')
    quit()

count = 0
for line in fhand :
    if line.startswith('To synchronize') :
        count  = count + 1
print(f'There was {count} subject lines in {fname}')

