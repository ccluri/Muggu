import pylab as pl
import numpy as np

from pendulum import Pendulum

iterations = 3600
angle = 0.1

values_x1 = np.zeros([iterations])
values_y1 = np.zeros([iterations])
values_x2 = np.zeros([iterations])
values_y2 = np.zeros([iterations])

pend1 = Pendulum(0.0, 0.0, 0.5) 
pend1_x, pend1_y = pend1.get_current()
pend2 = Pendulum(pend1_x, pend1_y, 0.3, 0.7)

for ii in range(iterations):
    values_x1[ii], values_y1[ii] = pend1.step_angle(angle)
    pend2.update_pivot(values_x1[ii], values_y1[ii])
    # ensure no slipping.
    values_x2[ii], values_y2[ii] = pend2.step_angle(angle* -(pend1.length/pend2.length))

pl.figure(figsize=[10,10])
pl.subplot(1,1,1)
pl.plot(values_x1, values_y1)
pl.hold(True)
pl.plot(values_x2, values_y2)
pl.show()
