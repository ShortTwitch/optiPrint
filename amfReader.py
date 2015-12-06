import xml.etree.ElementTree as ET
from ClassFormat import *
from normals import *

def parse_materials(root):
    materials = {}
    for material in root.findall('material'):
        name = material.find('metadata').text
        color = material.find('color')
        rgb = [color.find('r').text, color.find('g').text, color.find('b').text]
        materials[material.get('id')] = {
            "name" : name,
            "color" : rgb
        }
    return materials

def parse_vertices(root):
    vertices = {}
    for i, vertex in enumerate(root.iter('vertex')):
        cds = vertex.find('coordinates')
        x,y,z = cds.find('x').text, cds.find('y').text, cds.find('z').text
        v = Vertex(x, y, z)
        vertices[i] = v
    return vertices

def parse_faces(root):
    faces = []
    vertices = parse_vertices(root)
    materials = parse_materials(root)
    for volume in root.iter('volume'):
        mid = volume.get('materialid') #Use to identify color later
        for face in volume.findall('triangle'):
            v1 = int(face.find('v1').text)
            v2 = int(face.find('v2').text)
            v3 = int(face.find('v3').text)
            m = materials[mid]
            f = Face(vertices[v1], vertices[v2], vertices[v3], m)
            faces.append(f)
    return faces

def read_amf(filename):
    tree = None
    with open(filename) as f:
        tree = ET.parse(f)
    return tree.getroot()    
    
def main():
    filename = input("Enter AMF File : ")
    root = read_amf(filename)
    faces = parse_faces(root)
    get_and_separate_norms(faces)
    
    
if __name__ == '__main__':
    main()
