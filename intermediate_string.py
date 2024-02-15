s = 'Monty Python'
print(s[0:4]) #spelled- S sub 0 through 4

s = 'Monty Python' #printing out eveything up to the 2nd place
print(s[:2])

print()
a = 'Hello'
b = a + 'There'
print(b)

d = 'There'
c = a + ' ' + d
print(c)

print()
fruit = 'banana' #finding letter a in the word
if 'a' in fruit :
    print('Fount it!')

print()
#String Library
greet = 'Hello Bob'
print(greet)
zap =  greet.lower() #.lower() - lower case
print(zap)
print('Hi There'.lower())
nn = greet.upper() #.upper() - upper case
print(nn)
rep = greet.replace('Bob', 'Lera') #searching the replacing
print(rep)
repl = greet.replace('o', 'X')
print(repl)
greet = "      Hello Bob     "
rem = greet.lstrip() #removing whitespace at the left
print(rem)
remo = greet.rstrip() #removing whitespace at the right
print(remo)
remov = greet.strip() #removing both beginning and ending whitespace
print(remov)

print()
fruit = 'banana' #finding the position of the substring
pos = fruit.find('na') #na is the substring
print(pos)

print()
line = 'Please have a nice day'
pre = line.startswith('Please') #ask if line starts from Please
print(pre)
pref = line.startswith('p')
print(pref)

print()
data = 'From dskdksuhfksfnksjjnb@gmail.com Sat Jan Fab 19:38'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos) #finding the place of the whitespace
print(sppos)
host = data[atpos+1 : sppos] #printing out everything between @ and whitespace
print(host)
