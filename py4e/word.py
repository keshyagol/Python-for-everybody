fil=input('Entet the file name :')
op=open(fil)

counts=dict()
for item in op:
    words=item.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None
for k,v in counts.items():
    if bigcount is None or v>bigcount:
        bigword=k
        bigcount=v
print(bigword,bigcount)
