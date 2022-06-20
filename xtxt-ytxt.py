# Using matplolib, get the values of all x coordinates from x.txt file and values of all y coordinates from y.txt file. Plot them against each other
import matplotilb.pyplot as plt
filex=open("x.txt",'r')
xlist=[]
ylist=[]
for line in filex:
    line=line.strip()
    print(line)
    xlist.append(line)
filex.close()
filey=open("y.txt",'r')
for line in filey:
    line=line.strip()
    print(line)
    ylist.append(line)
filey.close()
plt.plot(xlist,ylist,".-",color="red")
plt.show()
