import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from numpy import random, cos, sin, sqrt, pi
from math import pi, sin, cos, atan

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
        if not(n.x == self.x and n.y == self.y and n.z == self.z):
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

def rand_sphere(n, start_theta, end_theta, start_phi, end_phi):
    """n points distributed evenly on the surface of a unit sphere"""
    
    theta_diff = end_theta - start_theta
    theta = (random.rand(n) * theta_diff) + start_theta
    
    phi_diff = end_phi - start_phi
    phi = (random.rand(n) * phi_diff) + start_phi
    
    r = 1
    
    return polar_to_cartesian(r, theta, phi)

def polar_to_cartesian(rs, thetas, phis):
    xs = rs * np.sin(phis) * np.cos(thetas)
    ys = rs * np.sin(phis) * np.sin(thetas)
    zs = rs * np.cos(phis)
    return xs, ys, zs

def cartesian_to_polar(x, y, z):
    theta = atan(sqrt(x**2 + y**2) / z)
    phi = atan(y/z)
    return theta, phi

def graph_circles(circles, best):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for circle in circles:
        ax.scatter(circle.x, circle.y, circle.z, color="blue")
    ax.scatter(best.x, best.y, best.z, color="red")
    
    ax.set_title("Weighted Normals Graph")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')
    
    plt.show()

def separate_norms(normals, count = 1000, displayNorms = True, displayCones = True):    
    
    start_theta = start_phi = 0
    end_theta = end_phi = 2 * pi
    multiplier = .1
    answer = None
    for i in range(0, 4):
        xs, ys, zs = rand_sphere(count, start_theta, end_theta,
                                 start_phi, end_phi)
    
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
        #graph_circles(circles, answer)

        theta, phi = cartesian_to_polar(answer.x, answer.y, answer.z)
        start_theta = theta - multiplier
        end_theta = theta + multiplier
        start_phi = phi + multiplier
        end_phi = phi - multiplier
        multiplier *= multiplier
        
    print("Answer : ({}, {}, {})\n".format(answer.x, answer.y, answer.z))
            
    
    
    
    