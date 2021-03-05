total = []
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for lines in handle:
	if "From " not in lines:
		continue
	else:
		lines = lines.strip()
		lnes = lines.split()
		email = lnes[1]
		total.append(email)
print(total)
