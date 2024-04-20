import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
# DONE BY OMAR ALI KANDIL

def generatedata(size): #generating our data set
    return [random.randint(1,100)for _ in range(size)]

#
def updateplot(data,bars,iteration): #data is our data set, bars are the heights of elements in the plot
    #iteration is the number of iterations done in bubble sort which equates to n^2 while n is the size of the dataset
    #iteration is the text that will be displayed in the visulization
    for bar,val in zip(bars,data):
        bar.set_height(val)
        iteration[0]+=1
        text.set_text('number of operations{}'.format(iteration[0]))

def bubble_sort(data):
    n=len(data)
    if n==1:
        return
    else:
        for i in range(n):
            for j in range(0,n-i-1):
                if data[j] >data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
                    yield data

def main():
    iteration = [0]
    size=100
    data = generatedata(size)
    fig, ax= plt.subplots()
    ax.set_title('bubble sort visulizations')
    global text
    text= ax.text(0.02, 0.95, "", transform=ax.transAxes)
    bar_rects = ax.bar(range(len(data)), data, align="edge") # Initialize a bar plot
    anim=animation.FuncAnimation(fig,func=updateplot,fargs=(bar_rects,iteration),frames=bubble_sort(data),interval=1,repeat=False)
    #FuncAnimation  takes a figure >fig , frames which are the dataset to plot
    #a func that updates the plot postions and or heights
    plt.show()

main()