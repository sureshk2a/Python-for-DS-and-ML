import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
#functional method - single plot
# plt.plot(x,y)
# plt.xlabel("X Label")
# plt.ylabel("Y Label")
# plt.title("Title")
#plt.show()

#subplots - 2 charts (sub plot)
# plt.subplot(1,2,1)
# plt.plot(x,y,"r")
# plt.subplot(1,2,2)
# plt.plot(y,x,"b")
# plt.show()

#object oriented - create figure objects and apply values to it - SINGLE GRAPH
#fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8]) #left, bottom, width, heigth
# axes.set_xlabel("X label")
# axes.set_ylabel("Y label")
# axes.set_title("Title")
# axes.plot(x,y)
# plt.show()

#object oriented - create figure objects and apply values to it - TWO GRAPH (subplot)
#fig = plt.figure()
# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.5,0.4,0.2])
# axes1.plot(x,y)
# axes1.set_title("bigPlot")
# axes2.plot(y,x)
# axes2.set_title("smallPlot")
# plt.show()

#subplots with multiple rows and avioding interactions
# fig,axes = plt.subplots(nrows=1,ncols=2)
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()
# plt.show()


#Figure size and DPI
# fig = plt.figure(figsize=(8,2)) #width and height
# ax = fig.add_axes([0,0,1,1])
# fig.savefig("mypic.jpg",dpi=200)
# ax.plot(x,y)
# plt.show()

#2 axes in single grpah
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,x**2,label="X squared")
# ax.plot(x,x**3,label="X Cubed")
# ax.legend() #set the label
# plt.show()

#Plot Appearance
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y,color="#FF8C00",linewidth=2,linestyle="--")
# ax.set_xlim([0,1])
# ax.set_ylim([0,2])
# plt.show()

#Special Plot Types
# n = 20
# Z = np.random.uniform(0,1,n)
# plt.pie(Z)
# plt.show()



