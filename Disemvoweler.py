text = raw_input("Enter string: ").replace(" ","")
vowels = ["a", "e", "i", "o", "u"]
print "".join(letter for letter in text if letter not in vowels)
print "".join(letter for letter in text if letter in vowels)
