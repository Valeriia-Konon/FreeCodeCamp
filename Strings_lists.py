abc = 'With three words'
stuff = abc.split() #breaking a string into parts and creates a list
print(stuff)
for w in stuff:
    print(w)

print()
line = 'A lot             of spaces; one;two;three'
etc = line.split() #splitting a line
print(etc)
thing = line.split(';')
print(thing)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]
print(n)