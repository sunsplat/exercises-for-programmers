QUOTES = {}

quote = input("What is the quote? ")
name = input("Who said it? ")

if name in QUOTES:
    QUOTES[name].append(quote)
else:
    QUOTES[name] = [quote]

print(f"{name} says, \"{quote}\"")
