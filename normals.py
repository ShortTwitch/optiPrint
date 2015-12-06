from ClassFormat import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

def faces_to_normals(faces):
    normals = []
    for face in faces:
        # Perform dot product (or is it cross product?)
        u = face.v2 - face.v1
        v = face.v3 - face.v1
        nx = (u.y * v.z) - (u.z * v.y)
        ny = (u.z * v.x) - (u.x * v.z)
        nz = (u.x * v.y) - (u.y * v.x)
        normals.append(Normal(nx, ny, nz, face.area()))
    return normals

def get_and_separate_norms(faces):
    normals = faces_to_normals(faces)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for n in normals:
        x = n.x * n.area
        y = n.y * n.area
        z = n.z * n.area
        ax.quiver(0,0,0,x,y,z, pivot='tail')
        
    ax.set_title("Weighted Normals Graph")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_zlabel('Z-Axis')
    
    plt.show()