from vpython import *
from random import randint
import math
import time

steps = 50 # Steps for transformation
time_anim = 0.1 # Time for rotation (ms)
time_wait = 1 # Wait time before and after transformations (ms)
axis_size = 20
axis_width = 0.1
sphere_rad = 0.5 # Radius of vertex
polygon_rad = 5 # Distance of spheres from origin
resolution = 800 # Size of canvas (resolution*resolution)

def main():
    # Sets canvas
    canvas(width=resolution,height=resolution,background=color.black)

    # Creates axis
    xaxis = arrow(pos = vector(-1*axis_size/2,0,0), axis=vector(axis_size,0,0),shaftwidth=axis_width)
    yaxis = arrow(pos = vector(0,-1*axis_size/2,0), axis=vector(0,axis_size,0),shaftwidth=axis_width)
    time.sleep(3)
    for i in range(3,11):
        dihedral(i)

# Visualizes the D{num_vertices} group
def dihedral(num_vertices):
    # Creates and titles
    title_text = 'D' + str(num_vertices) + ' Group'
    title = text(text=title_text, align='center', pos=vector(0,-1*(axis_size/2+1),0))
    name = text(text='Aakash Dutt', align='right', pos=vector(axis_size/2+1,-1*(axis_size/2+1),0))
    vertices = create_vertices(num_vertices)

    # Creates labels for r^k
    grp_labels = [None]*num_vertices
    grp_label_pos = vector(-3*(axis_size/8),3*(axis_size/8),0)
    grp_labels[0]='e'
    for i in range(1,num_vertices):
        grp_labels[i] = 'r^'+str(i)
    grp_label = text(text=grp_labels[0], align='left', pos=grp_label_pos)

    for i in range(1,num_vertices+1):
        time.sleep(time_wait)
        grp_label.visible = False
        rotate(vertices)
        grp_label = text(text=grp_labels[i%num_vertices], align='left', pos=grp_label_pos)

    time.sleep(time_wait)
    grp_label.visible = False
    flip(vertices)
    grp_labels = [None]*num_vertices
    grp_labels[0]='s'
    grp_label = text(text=grp_labels[0], align='left', pos=grp_label_pos)

    for i in range(1,num_vertices): 
        grp_labels[i] = 'sr^'+str(i)

    for i in range(1,num_vertices+1):
        time.sleep(time_wait)
        grp_label.visible = False
        rotate(vertices)
        grp_label = text(text=grp_labels[i%num_vertices], align='left', pos=grp_label_pos)

    time.sleep(time_wait)
    title.visible = False
    name.visible = False
    grp_label.visible = False
    for i in range(0, len(vertices)):
        vertices[i].visible = False
    

# Creates vertices
def create_vertices(num_vertices):
    vertices = [None]*num_vertices
    angle = 2*pi/(2*num_vertices);
    for i in range(0,num_vertices):
        sphere_color = 1/255*vector(randint(100,255),randint(100,255),randint(100,255))
        sphere_pos = vector(polygon_rad*math.cos(angle),polygon_rad*math.sin(angle),0)
        vertices[i] = sphere(pos=sphere_pos, raidius=sphere_rad, color = sphere_color)
        angle = angle+2*pi/num_vertices;
    return vertices

# Rotates the polygon one turn about the origin
def rotate(beads):
    for t in range(0,steps):
        for i in range(0,len(beads)):
            beads[i].rotate(angle=(2*math.pi/len(beads))/steps, axis=vector(0,0,1), origin=vector(0,0,0))
            time.sleep(time_anim/steps)

# Flips on y axis
def flip(beads):
    time.sleep(time_wait)
    angle = 2*pi/(2*len(beads))
    flip_axis = vector(math.cos(angle),math.sin(angle),0)
    for t in range(0,steps):
        for i in range(0,len(beads)):
            beads[i].rotate(angle=math.pi/steps, axis=flip_axis, origin=vector(0,0,0))
            time.sleep(time_anim/steps)
    time.sleep(time_wait)

if __name__=='__main__':
    main()
