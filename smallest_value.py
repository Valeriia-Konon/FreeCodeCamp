smallest_so_far = None
print('Before')
for value in [-9, -41, -12, -3, -75, -100, -5] :
    if smallest_so_far is None : # IS similar to == but stronger
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print(smallest_so_far, value)
print('After', smallest_so_far)