friends = ['Joseph', 'Katerina', 'Sally']
print(len(friends))

print()
friends = ['Joseph', 'Katerina', 'Sally']
for friend in friends:
    print(f"Happy New Year {friend}")

for i in range(len(friends)) :
    friend = friends[i]
    print(f"Happy New Year {friend}")

print()
t = [9, 41, 12, 76, 59, 15]
print(t[1:3])

print()

stuff = list()
stuff.append('book') #append = adding
stuff.append(99)
print(stuff)
stuff.append('cookies')
print(stuff)

print()
friends = ['Joseph', 'Katerina', 'Sally']
friends.sort()
print(friends, friends[2])

print()
nums = [9, 41, 12, 76, 59, 15]
print(max(nums))
print(min(nums))
print(len(nums))
print(sum(nums))
print(sum(nums) / len(nums))

print()
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print(f'Average is {average}')