fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:

        # oldcount = di.get(w,0) #if the key is not there, the count is zero

        di[w]=di.get(w,0) + 1 #idiom: retrieve/create/update counter

#print(di)

#to find the most common word
largest = -1
theword = None
for k,v in di.items() :
    if v > largest:
        largest = v
        theword = k #capture/remember the key that was largest

print(f'The largest {theword, largest} was found')