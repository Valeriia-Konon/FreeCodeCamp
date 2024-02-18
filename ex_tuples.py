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

tmp = list()
for k,v in di.items():
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)

#print('Flipped', tmp)

tmp = sorted(tmp, reverse=True) #reverse=True - vice versa
#print('Sorted: ', tmp[:5])

for v,k in tmp[:5] :
    print(k,v)