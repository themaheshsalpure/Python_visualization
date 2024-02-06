# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:18:24 2023

@author: ASUS
"""


#📌 ------------------------------------------------------------------

import matplotlib.pyplot as plt

x = plt.plot([8,3,0,6,8,45,2,9])
plt.show(x)


#📌 ------------------------------------------------------------------

'''
using list comprehension in the matplotlib

'''
rang = (1,7)
x = plt.plot([x*1.5 for x in rang])
plt.plot(x)


y = plt.plot([y*2 for y in rang])
plt.show(y)


#📌 ------------------------------------------------------------------

'''
Adding the grid in the graph by using plt.grid(True)

'''
z = plt.plot([y/5 for y in rang])
plt.grid(True)
plt.show(z)


#📌 ------------------------------------------------------------------

import numpy as np
x = np.arrange(1,5)
y = plt.plot([x, x*1.5, x, x*3.0, x, x/3.0 ])
plt.show(y)

#📌 ------------------------------------------------------------------

import numpy as np
x = np.arrange(1,5)
y = plt.plot([x, x*1.5, x, x*3.0, x, x/3.0 ])
# plt.show(y)
plt.axis()





import matplotlib.pyplot as plt

rang = (1,8)
plt.plot([i for i in rang])
# plt.show(x)


plt.axis()               # show the current axis limit
plt.axis([0,9,1,4])
plt.show()


plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph by MS')


'''
Adding the legend 

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,5)
plt.plot(x,x*2,label='Normal')

plt.plot(x,x*3.0,label='Fast')

plt.plot(x,x/3.0,label='Slow')


plt.legend()
plt.show()






'''
Adding the colour to the lines 

'''
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 3)
plt.plot(y, 'y')
plt.plot(y+1, 'm')
plt.plot(y+2, 'c')
plt.show()


'''
specifying the style for the lines 

'''
y = np.arange(1, 3)
plt.plot(y, '--', y+1, '-.', y+2, ':')
plt.show()



'''
addding the control marker styles 

'''

import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 3, 0.2)
plt.plot(y, 'x', y+0.5, 'o', y+1, 'D', y+1.5, '^', y+2, 's')
plt.show()



'''
creating a histogram

'''
import matplotlib.pyplot as plt
import numpy as np


y = np.random.randn(1000)
plt.hist(y)
plt.show() 



'''
creating a bar graph

'''
import matplotlib.pyplot as plt
import numpy as np

plt.bar([1,2,3], [3,2,5])
plt.show()



'''
creating an scattered graph

'''
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y)
plt.plot()






import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y, c=x, s=y)
plt.plot()




import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100)
y = np.random.randn(1000)
z = np.linspace(-4, 4)
plt.plot(z)
plt.text(5, -3, 'Mahesh')
plt.plot()































































