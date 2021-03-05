total = []
count = dict()
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
for emails in total:
	count[emails] = count.get(emails, 0) + 1
bigcount = None
bigword = None
for word,count in count.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print(bigword, bigcount)
