from render import Render

from obj import Obj

from utils import color

my_bmp_file = Render()
my_bmp_file.glInit()
my_bmp_file.glCreateWindow(800,600)
my_bmp_file.glClearColor(0,0,0)
my_bmp_file.glColor(1,1,1)

p1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), 
        (230, 360), (250, 380), (220, 385), (205, 410), (193, 383),]

p2 = [(321, 335), (288, 286), (339, 251), (374, 302),]

p3 = [(377, 249), (411, 197), (436, 249),]

p4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
        (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), 
        (580, 230),(597, 215), (552, 214), (517, 144), (466, 180),]

p5 = [(682, 175), (708, 120), (735, 148), (739, 170),]

# my_bmp_file.drawPolygons(p1)
# my_bmp_file.drawPolygons(p2)
# my_bmp_file.drawPolygons(p3)
# my_bmp_file.drawPolygons(p4)
# my_bmp_file.drawPolygons(p5)

my_bmp_file.fillPoly(p1,color(255,255,100))
my_bmp_file.fillPoly(p2,color(0,255,0))
my_bmp_file.fillPoly(p3,color(255,0,0))
my_bmp_file.fillPoly(p4,color(13,200,100))
my_bmp_file.fillPoly(p5,color(0,0,204))



my_bmp_file.glFinish('polygons.bmp')
