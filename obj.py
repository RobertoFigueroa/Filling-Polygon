# Carga un archivo OBJ

class Obj(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.read()

        for face in self.vertices:
            print(face)

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)

                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                elif prefix == 'vn': #normal
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'vt': #textura
                    self.texcoords.append(list(map(float,value.split(' '))))
                elif prefix == 'f': #faces
                    faceLine = []
                    for vert in value.split(' '):
                        if vert != ' ' and vert != '':
                            faceLine.append(list(map(int, vert.split('/'))))
                    self.faces.append(faceLine)

