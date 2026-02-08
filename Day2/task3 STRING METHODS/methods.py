text = "      hello, world     "

print(text.strip())
print(text.title())
print(text.split(", ")) # split("at") returns a list 
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.replace("world", "Python")) # replace("from", "to")
print(text.count("o"))
print(text.title())

# NOTE: Strings are "immutable" all these mesthods returns a new string