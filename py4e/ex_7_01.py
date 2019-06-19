fh=open("mbox.txt")
print(fh)
for lx in fh:
    ly=lx.strip()
    print(ly.upper())
