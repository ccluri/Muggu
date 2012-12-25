import pylab as pl
import numpy as np

from pendulum import Pendulum

iterations = 50
posValues_x1 = np.zeros([iterations])
posValues_y1 = np.zeros([iterations])

pend1 = Pendulum(0.0,0.0,0.5)
for ii in range(iterations):
    posValues_x1[ii],posValues_y1[ii] = pend1.stepAngle()

pl.figure(figsize=[10,10])
pl.subplot(1,1,1)
pl.plot(posValues_x1,posValues_y1)
pl.show()
