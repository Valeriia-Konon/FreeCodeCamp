#Outputting a letter of the word
fruit = 'banana'
letter = fruit[1]
print(letter)

#Printing the specific letter of the word
x = 3
w = fruit[x - 1]
print(w)

#Printing the length of the word in No.
print(len(fruit)) #len = length

#Printing numbers out + letters
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#Counting 'a' letter in the word
word = 'orange'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)