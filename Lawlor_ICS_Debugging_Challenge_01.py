# Grace Lawlor
# Debugging Challenge #1
# 01/30/2020

# Code pulled from the short programs I used to solve the Python Challenge problems

# Ideally, the program should print the words "cat" and "dog"
# SYNTAX ERROR COUNT: 4

text = "a_r"
# empty string variable that can be added to later
message = ''
for x in text:
    # figure out the corresponding ASCII value of each character and add 2 to it
    # convert the new ASCII values back into characters and assemble those characters into a new message
    message = message + chr((ord(x) + 2)

# print the new message
print(message)

# another empty string variable that can be added to later
message2 = ''
fhand = open('Debugging1.txt')
for x in fhand:
    # convert each line of the text document to a string so that it can be iterated through
    line = str(x)
    for y in line:
        # if python finds any letters hidden among the various symbols found in the text document, assemble them into a new message
        if y = 'a' or y == 'b' or y == 'c' or y == 'd' or y == 'e' or y == 'f' or y == 'g' or y == 'h' or y == 'i' or y == 'j'
                or y == 'k' or y == 'l' or y == 'm' or y == 'n' or y == 'o' or y == 'p' or y == 'q' or y == 'r' or y == 's' or
                y == 't' or y == 'u' or y == 'v' or y == 'w' or y == 'x' or y == 'y' or y == 'z':
            message2 = message2 + y

# print the second new message
print(message2)
