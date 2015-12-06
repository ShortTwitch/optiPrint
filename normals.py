from ClassFormat import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

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
    print "There are {} normals.".format(len(normals))
    for n in normals:
        print n
    start = [0] * len(normals)
    
    xs = [(n.x * n.area) for n in normals]
    ys = [(n.y * n.area) for n in normals]
    zs = [(n.z * n.area) for n in normals]
    
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.quiver(start, start, start, xs, ys, zs, length=.1)
    plt.show()
    
