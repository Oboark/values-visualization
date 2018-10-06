import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import MaxNLocator
import seaborn as sns
sns.set()

"""
DATA
"""

labels = ['Social', 'School', 'Downtime', 'Productive', 'Procrastionation', 'Sleep']

# setup week data placeholder
week = [np.zeros(24) for i in range(8)]
week = np.array(week)
week = week.astype(int)

# wednesday
week[0][0:8] = 5
week[0][8:10] = 0
week[0][10:11] = 1
week[0][11:13] = 3
week[0][13:15] = 1
week[0][15:18] = 4
week[0][18:19] = 5
week[0][19:21] = 4
week[0][21:24] = 3
# thursday
week[1][0:1] = 3
week[1][1:2] = 0
week[1][2:4] = 3
week[1][4:9] = 5
week[1][9:10] = 0
week[1][10:11] = 1
week[1][11:13] = 3
week[1][13:14] = 1
week[1][14:16] = 0
week[1][16:18] = 0
week[1][18:20] = 5
week[1][20:21] = 3
week[1][21:24] = 3
# friday
week[2][0:2] = 4
week[2][2:9] = 5
week[2][9:11] = 1
week[2][11:13] = 1
week[2][13:14] = 1
week[2][14:16] = 0
week[2][16:19] = 5
week[2][19:21] = 3
week[2][21:22] = 4
week[2][22:24] = 3
# saturday
week[3][0:1] = 3
week[3][1:2] = 3
week[3][2:3] = 4
week[3][3:12] = 5
week[3][12:16] = 4
week[3][16:18] = 4
week[3][18:24] = 3
# sunday
week[4][0:1] = 4
week[4][1:2] = 3
week[4][2:7] = 5
week[4][7:8] = 0
week[4][8:11] = 5
week[4][11:14] = 3
week[4][14:19] = 0
week[4][19:24] = 3
# mond
week[5][0:2] = 4
week[5][2:10] = 5
week[5][10:20] = 4
week[5][20:24] = 3
# tuesday
week[6][0:1] = 3
week[6][1:9] = 5
week[6][9:10] = 0
week[6][10:11] = 1
week[6][11:12] = 3
week[6][12:14] = 1
week[6][14:16] = 0
week[6][16:17] = 3
week[6][17:20] = 5
week[6][20:22] = 4
week[6][22:24] = 0
# wednesday
week[7][0:3] = 3
week[7][3:5] = 0
week[7][5:9] = 5

"""
PLOTTING
"""

# setup image figure
fig = plt.figure()
ax1 = fig.add_subplot(111)

# plot
plt.title("My Week")
plt.xlabel("Hours")
im = ax1.imshow(week, interpolation='nearest', cmap='RdYlBu', aspect=3)

# setup legend
values = np.unique(week.ravel())
colors = [ im.cmap(im.norm(value)) for value in values] 
patches = [ mpatches.Patch(color=colors[i], label=labels[values[i]]) for i in range(len(values))]
plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# setup ticks
plt.yticks(np.arange(8), ('Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed'))
plt.xticks(np.arange(24), np.arange(24))

# setup hours
hours = []
hours.append([np.count_nonzero(i == 0) for i in [j for j in week]])
hours.append([np.count_nonzero(i == 3) for i in [j for j in week]])
hours.append([np.count_nonzero(i == 4) for i in [j for j in week]])
hours.append([np.count_nonzero(i == 5) for i in [j for j in week]])

# plot hours
socfig, socplot  = plt.subplots()
socplot.plot([sum(hours[0])/len(hours[0]) for i in range(8)], color='peachpuff')
socplot.plot(hours[0], color='coral')
plt.xticks(np.arange(8), ('Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed'))
plt.yticks(np.arange(24), np.arange(24))
plt.title("Social")
plt.ylabel("Hours")

prodfig, prodplot = plt.subplots()
prodplot.plot([sum(hours[1])/len(hours[1]) for i in range(8)], color='pink')
prodplot.plot(hours[1], color='hotpink')
plt.xticks(np.arange(8), ('Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed'))
plt.yticks(np.arange(24), np.arange(24))
plt.title("Productivity")
plt.ylabel("Hours")

wasfig, wasplot = plt.subplots()
wasplot.plot([sum(hours[2])/len(hours[2]) for i in range(8)], color='lightslategray')
wasplot.plot(hours[2], color='lightsteelblue')
plt.xticks(np.arange(8), ('Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed'))
plt.yticks(np.arange(24), np.arange(24))
plt.title("Procrastination")
plt.ylabel("Hours")

slpfig, slpplot = plt.subplots()
slpplot.plot([sum(hours[3])/len(hours[3]) for i in range(8)], color='midnightblue')
slpplot.plot(hours[3], color='darkblue')
plt.xticks(np.arange(8), ('Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed'))
plt.yticks(np.arange(24), np.arange(24))
plt.title("Sleep")
plt.ylabel("Hours")

# show
plt.show()