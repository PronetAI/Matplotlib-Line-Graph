y=[]
val=0
def y_calculator(x):
  #5 is the slope 
  #3 is the y intercept
    return (5*x)+3
for var in x:
    val=y_calculator(var)
    y.append(val)
plt.plot(x,y,".-",color="blue")
plt.show()
