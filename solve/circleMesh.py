import normalTree as nt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import numpy as np
from scipy.spatial import ConvexHull

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
        self.areasum += n.area
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

def plot_normals(normals, ax):
    for normal in normals:
        ax.scatter(normal.x, normal.y, normal.z, color = 'r')
    
    ax.set_title("Weighted Normals Graph")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')
    
def separate_norms(normals, count = 5000, displayNorms = True, displayCones = True):    
    
    circles = []
    lookup = nt.NormalLookup(normals)
    print "Computed NormalLookup Table"
    for normal in normals:
        circle = Sphere(normal.x, normal.y, normal.z, .707)
        neighbors = lookup.normalsWithinRange(normal, .707)
        for neighbor in neighbors:
            circle.addNormal(neighbor)
        circles.append(circle)
        
    print "Computed All Cone of Shames"
        
    answer = circles[0]
    for circle in circles:
        if circle.areasum < answer.areasum:
            answer = circle
    
    print("Answer : ({}, {}, {})\n".format(answer.x, answer.y, answer.z))
    print("Value is : {}".format(answer.areasum));
    
    print("Printing Now....................")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_normals(normals, ax)
    
    x, y, z = create_sphere(answer.x, answer.y, answer.z, .707)
    ax.plot_wireframe(x, y, z, color = 'b')
    
    plt.show()
    
    
def convexHullTest(vertices):
    pointsList = []
    
    for vertex in vertices:
        x, y, z = vertex.x, vertex.y, vertex.z
        xyzList = [x, y, z]
        pointsList.append(xyzList)
    
    pointsList = np.array(pointsList)
    
    print ("\n There are {} vertices.\n".format(pointsList.size / 3))
    
    cv = ConvexHull(pointsList)
    
    hull_points = cv.vertices
    
    print(hull_points)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for vertex in vertices:
        ax.scatter(vertex.x, vertex.y, vertex.z, color = 'r')
    
    for simplex in cv.simplices:
        ax.scatter(pointsList[simplex, 0],
                   pointsList[simplex, 1],
                   pointsList[simplex, 2], color = 'b' )
    plt.show()
    
    
    
    
    
    
    