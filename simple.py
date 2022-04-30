# Data
# no such thing as "const", "let" and "var". Its all "let".
a = 10
b = 20
c = 50

# Booleans are capitalized
a_truth = True
# a_lie = False

# Data Storage
# Arrays (called "lists")
empty = []
names = ["kk0", "kk1", "kk2"]
print(names[1])
print("length of names array is " + str(len(names)))
names.append("krystal")
print("length of new names array is " + str(len(names)))


# Conditionals
# Colons indicate the start of a code block, indentation indicates the end of a code block.
if c <= 50 and b == True or c == 100:  # booleans are capitalized "True"/"False"
    print("testing")
elif c == 30:  # No such thing as "===" in python
    print("testing 2")
else:
    print("going to sleep")
