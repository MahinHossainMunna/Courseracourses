name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) + 1

bcount = None
bword = None
for k, v in count.items():
    if bcount == None or v > bcount:
        bword = k
        bcount = v
print(bword, bcount)
