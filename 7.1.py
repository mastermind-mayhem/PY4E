# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, "r")
for f in fh:
    f = f.strip()
    f = f.upper()
    print(f)
