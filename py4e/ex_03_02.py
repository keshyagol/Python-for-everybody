sh=input("enter hours:")
sr=input("enter rate:")
try:
    fh=float(sh)
    fr=float(sr)
except:
    print("Error, please enter numeric input")
    quit()

print(fh,fr)
if fh>40:
    reg=fr*fh
    opt=(fh-40.0)*(fr*0.5)
    xp=reg+opt
else:
    xp=fh*fr
print("pay:",xp)
