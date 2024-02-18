import re
hand = open('clown.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line) #0-9. from 1 to 10 digits or dots
    if len(stuff) !=1 : continue #not equal to 1
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))