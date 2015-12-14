import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import ClassFormat as CF

def _parse_materials(root):
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

def _parse_vertices(root):
    vertices = {}
    for i, vertex in enumerate(root.iter('vertex')):
        cds = vertex.find('coordinates')
        x,y,z = cds.find('x').text, cds.find('y').text, cds.find('z').text
        v = CF.Vertex(x, y, z)
        vertices[i] = v
    return vertices

def _parse_faces(root):
    faces = []
    vertices = _parse_vertices(root)
    materials = _parse_materials(root)
    for volume in root.iter('volume'):
        mid = volume.get('materialid') #Use to identify color later
        for face in volume.findall('triangle'):
            v1 = int(face.find('v1').text)
            v2 = int(face.find('v2').text)
            v3 = int(face.find('v3').text)
            m = 0
            if mid in materials:
                m = materials[mid]
            f = CF.Face(vertices[v1], vertices[v2], vertices[v3], m)
            faces.append(f)
    return faces

def read_amf(filename):
    faces = None
    normals = None
    with open("amf/" + filename) as f:
        try:
            tree = ET.parse(f)
            root = tree.getroot()
            faces = _parse_faces(root)
            normals = CF.faces_to_normals(faces)
        except ParseError:
            print("Error trying to parse .amf file : amf/{}".format(filename))
            print("Check if file exists and try again")
    return faces, normals
