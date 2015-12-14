import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from numpy import random, cos, sin, sqrt, pi

class Sphere(object):
    
    def __init__(self, x, y, z, radius):        
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.normals = []    
        self.areasum = 0
        
    def addNormal(self, n):
        self.normals.append(n)
        self.areasum += n.area

def create_sphere(xCenter, yCenter, zCenter, r):
    #draw sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x=np.cos(u)*np.sin(v)
    y=np.sin(u)*np.sin(v)
    z=np.cos(v)
    # shift and scale sphere
    x = r*x + xCenter
    y = r*y + yCenter
    z = r*z + zCenter
    return (x,y,z)

def rand_sphere(n):
  """n points distributed evenly on the surface of a unit sphere""" 
  z = 2 * random.rand(n) - 1   # uniform in -1, 1
  t = 2 * pi * random.rand(n)   # uniform in 0, 2*pi
  x = sqrt(1 - z**2) * cos(t)
  y = sqrt(1 - z**2) * sin(t)
  return x, y, z

def separate_norms(normals, count=100, displayNorms = True, displayCones = False):    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')    
    
    xs, ys, zs = rand_sphere(count)

    circles = []
    for i in range(count):
        x, y, z = xs[i], ys[i], zs[i]
        circles.append( Sphere(x, y, z, .707) )
    
    for circle in circles:
        for normal in normals:
            cx = circle.x
            cy = circle.y
            cz = circle.z
            if cx + .707 > normal.x and cx - .707 < normal.x:
                if cy + .707 > normal.y and cy - .707 < normal.y:
                    if cz + .707 > normal.z and cz - .707 < normal.z:
                        circle.addNormal(normal)
    circles = sorted(circles, key = lambda x : x.areasum, reverse=False)
    answer = circles[0]
    
    if displayCones:
        for circle in circles:
            (x, y, z) = create_sphere(circle.x, circle.y, circle.z, .707)
            ax.plot_wireframe(x, y, z, alpha = .2, color="blue")

    
    (x, y, z) = create_sphere(answer.x, answer.y, answer.z, .707)
    ax.plot_wireframe(x, y, z, alpha = .2, color="black")
    
    if displayNorms:
        for n in normals:
            x = n.x #* n.area
            y = n.y #* n.area
            z = n.z #* n.area
            ax.scatter(x,y,z, c="r")
        
    ax.set_title("Weighted Normals Graph")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')
    
    plt.show()