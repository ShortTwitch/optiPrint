import numpy
from stl import stl
import ClassFormat as CF

def read_stl(filename):
    faces = None
    normals = None
    try:
        mesh = stl.StlMesh("stl/" + filename)
        faces = []
        for i in range(len(mesh.normals)):
            v1 = CF.Vertex(mesh.v0[i][0], mesh.v0[i][1], mesh.v0[i][2])
            v2 = CF.Vertex(mesh.v1[i][0], mesh.v1[i][1], mesh.v1[i][2])
            v3 = CF.Vertex(mesh.v2[i][0], mesh.v2[i][1], mesh.v2[i][2])
            fc = CF.Face(v1, v2, v3)
            faces.append(fc)
        normals = CF.faces_to_normals(faces)
    except IOError:
        print("Error trying to parse .stl file : stl/{}".format(filename))
        print("Check if file exists and try again")
        
    return faces, normals
        
    
