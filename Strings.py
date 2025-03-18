#Strings
sentence = "  "
#builtin functionality
#functions
print(sentence)
print(sentence.upper())  #call a function
print(sentence.lower())
print(sentence.title())
print(sentence.count("dog"))

sentence="she was"
print(sentence.title())
if sentence.isspace() or sentence.isdigit() or sentence.isnumeric():
    print("Invalid")
else:
    print("Valid")