add = None
total = 0
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
		continue
    else:
        line = line.strip()
        sline = float(line[line.index(": ")+2:])
        if add == None:
            add = sline
            total = total+1
        else:
            add = add + sline
            total = total+1
total = add/total
total = str(total)
print("Average spam confidence: "+total)
