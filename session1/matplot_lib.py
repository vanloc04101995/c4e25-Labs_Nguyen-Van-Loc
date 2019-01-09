from matplotlib import pyplot

# data
machine_counts= [18,4,2]
#Labels
machine_names = ["PC","MAC","LINUX"]
#draw
pyplot.pie(machine_counts, labels=machine_names, autopct="%.1f%%", shadow= True, explode=[0,0.1,0])
pyplot.title("PC, MAC and LINUX useage")
pyplot.axis("equal")
#show
pyplot.show()