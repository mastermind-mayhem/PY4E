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
		email = lnes[5]
		# print(email)
		hours = email.split(":")
		hours = hours[0]
		total.append(hours)
#print(total)
for emails in total:
	count[emails] = count.get(emails, 0) + 1
x = sorted(count.items())
for k,v in x:
	print(k, v)
