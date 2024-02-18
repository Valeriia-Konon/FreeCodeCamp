names = ["Harry", "Rob", "Ron", "Leon"]

for name in names:
    print(name)

name = "Leon"
for character in name:
    print(character)


#ex from saylor.org
price = 119 # in dollars
discount = 30 # in percent %
print("A $%d jacket at %d%% discount is now priced at %f" % (price,discount,price*0.7))