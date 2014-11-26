from __future__ import division
from visual import *
from visual.graph import *
import math

myscene = display(background = color.black)

#define electron
electron = sphere(pos=vector(1,0,0),radius=0.2,
                  color=color.red, make_trail = true)


#constants
##N = 100 #coil turns in toroid
##I = 2 #current of coils in toroid
IN = 15000000
mu_naught = 4e-7 * pi
qelectron = 1.6e-19
melectron = 9.1e-31

t = 0 #time
dt = 1e-100 #time step

velectron = 10*vector(1,1,0)
Efield = vector(0,0,0)
Bfield = vector(0,0,0)
pelectron = velectron / melectron


#loop to move electron
while true:
    r = mag(electron.pos) #distance from center of toroid
    theta = atan(electron.pos.y/electron.pos.x)
    Bfield = ((mu_naught * IN)/(2 * pi * r))*vector(-sin(theta), cos(theta), 0)
    
    Fe = qelectron*Efield
    Fb = cross(qelectron * velectron, Bfield)
    Fnet = Fe + Fb

    rate(10)
    pelectron = pelectron + Fnet*dt
    velectron = pelectron/melectron
    electron.pos=electron.pos+velectron*dt

    print(electron.pos)
    t=t+dt

