import numpy as np
import pylab as pl

class Pendulum():
    '''Here is a pendulum under zero gravity, The idea is to attach \
    multiple pendulums to each others end to obtain spirograph like \
    figures.'''

    def __init__(self, pivot_x, pivot_y, length, k=1.0):
        'pivot point is the points at which pendulum is fastened    \
        length is the pendulum length, k is a point on line of      \
        pendulum k=0 means pivot point, k=1 is the bob'
        self.pivot_x = pivot_x
        self.pivot_y = pivot_y
        self.length = length
        self.current_x = pivot_x + length
        self.current_y = 0.0
        self.k = k    

    def get_current(self):
        'gives the position of the bob'
        return self.current_x, self.current_y

    def update_pivot(self, pivot_x, pivot_y):
        'updates the position of the pivot'
        self.pivot_x = pivot_x
        self.pivot_y = pivot_y
        
    def step_angle(self, angle=0.1):
        'steps the angle of the pendulum along the pivot this  \
        is same as rotating bob about pivot by angle. Returns  \
        point of interest'
        temp_x = (self.current_x-self.pivot_x)*np.cos(angle) - \
                 (self.current_y-self.pivot_y)*np.sin(angle) + \
                 self.pivot_x
        temp_y = (self.current_x-self.pivot_x)*np.sin(angle) + \
                 (self.current_y-self.pivot_y)*np.cos(angle) + \
                 self.pivot_y
        self.current_x = temp_x
        self.current_y = temp_y
        return (self.current_x*self.k + self.pivot_x*(1-self.k), \
                self.current_y*self.k + self.pivot_y*(1-self.k))

if __name__ == '__main__':
    iterations = 3600
    angle = 0.1

    values_x1 = np.zeros([iterations])
    values_y1 = np.zeros([iterations])
    values_x2 = np.zeros([iterations])
    values_y2 = np.zeros([iterations])

    pend1 = Pendulum(0.0, 0.0, 0.5) 
    pend1_x, pend1_y = pend1.get_current()
    pend2 = Pendulum(pend1_x, pend1_y, 0.3, 0.6)
    
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
