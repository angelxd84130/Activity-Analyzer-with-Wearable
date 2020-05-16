import matplotlib.pyplot as plt
import pandas as pd
x = ["Still", "Walking", "Run", "Bike", "Car", "Bus", "Train", "Subway"]
# 270617_1/ Counter({0: 1216891, 8: 911943, 7: 897124, 1: 193588, 4: 123014, 2: 53941, 3: 0, 5: 0, 6: 0})
# 260617/ Counter({0: 1814595, 6: 913184, 1: 424521, 4: 373607, 2: 361645, 3: 10549, 5: 0, 7: 0, 8: 0})
# 220617_3/ Counter({0: 2819190, 5: 993161, 2: 388469, 1: 250542, 3: 122923, 6: 70516, 4: 0, 7: 0, 8: 0})
y3 = [250542, 388469, 122923, 0, 993161, 70516, 0, 0]
y2 = [424521, 361645, 10549, 373607, 0, 913184, 0, 0]
y1 = [193588, 53941, 0, 123014, 0, 0, 897124, 911943]
y = [[193588, 424521, 250542],
     [53941, 361645, 388469],
     [0, 10549, 122923],
     [123014, 373607, 0],
     [0, 0, 993161],
     [0, 913184, 70516],
     [897124, 0, 0],
     [911943, 0, 0]]
width = 0.4
y_choose = [424521, 361645, 122923, 373607, 993161, 913184, 897124, 911943]
#plt.bar([i-width/2 for i in range(1, 9)], y1, width=width, label="270617")
#plt.bar([i+width/2 for i in range(1, 9)], y2, width=width, label="260617")
#import numpy as np
#df = pd.DataFrame(y_choose, columns=["choose"])
#df.plot(kind='bar', grid=True, colormap='rainbow')
a = plt.bar(x, y_choose)
a[0].set_color("g")
a[1].set_color("g")
a[2].set_color("r")
a[3].set_color("g")
a[4].set_color("r")
a[5].set_color("g")
a[6].set_color("purple")
a[7].set_color("purple")
plt.ylabel("examples(every 10ms)")
plt.xlabel("labels")
plt.title("activies")
plt.xticks([i for i in range(8)], x)
plt.legend
plt.show()