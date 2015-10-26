import random 

def randword(cv):
	randword = {'c' : "bcdfghjklmnpqrstuvwxyz", 'v' : "aeiou"}
	for i in cv:
		if i.lower() in keys:
			randword = randword + str(random.choice(keys[i.lower()]))
		else:
			break
	else: 
		return randword
	return None

while True: 
	pattern = randword(input("Enter pattern: "))
	if not pattern is None: 
		print(pattern, "\n")
	else:
		print("Only enter c or v characters.\n")
