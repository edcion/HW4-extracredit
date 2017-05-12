from visual import *
import math

#range for the widnow
dispRange = 0.22
#create the window
window = display(range = dispRange, center = (dispRange/2, dispRange/2, 0),
                 title = "Voltage From An L Shaped Wire")
#length of each side of the wire
L = 0.15 #m
#width of the wire
W = 0.01 #m
#charge of the wire
Q = 50.0 * 10 ** -6 #C
#1/4*pi*epsilon not
k = 8.99 * 10 ** 9 #N*m^2/C^2
#voltage point multiplier
M = 9 ** -10


#create the wire
end = 1000
dq = Q/end #C
for r in range(end):
    #position up the wire from 0
    position = (L/end) * r
    #side of the wire parallel to the x axis
    dqx = sphere(color = color.yellow, radius = W, pos = vector(position, 0, 0))
    #account for the first spot only once
    if r != 0:
        #side of the wire parallel to the y axis
        dqy = sphere(color = color.yellow, radius = W,
                     pos = vector(0, position, 0))
#label for the points
label = text(text = "Sphere radius is voltage * 9 ^ -10",
             pos = (0,-0.05,0), height = 0.015, depth = 0.0001)

for x in range(21):
    for y in range(21):

        #keep track of the voltage from each dq
        voltage = 0.0 #J/C
        for r in range(end):
            rate(100000)
            #grid position
            gridPos = vector(x*0.01,y*0.01,0) #m
            #position up the wire from 0
            position = (L/end) * r
            #dqs parallel to the x axis
            dqxpos = vector(position, 0, 0)
            if dqxpos != gridPos:
                #find the voltage for this dq
                voltage += k*dq/mag(gridPos - dqxpos)
            #account for the first spot only once
            if r != 0:
                #dqs parallel to the y axis
                dqypos = vector(0, position, 0)
                if dqypos != gridPos:
                    #find the voltage for this dq
                    voltage += k*dq/mag(gridPos - dqypos)
        #radius based on the voltage at that point
        gridPointRadius = voltage * M
        #don't make spheres cover up the wire
        if gridPointRadius <= W:
            #make a sphere for each point in the grid
            gridPoint = sphere(pos = gridPos, radius = gridPointRadius)
            if gridPos == vector(0.1,0.12,0):
                print "Voltage at point ",gridPos,": ",voltage," J/C"
