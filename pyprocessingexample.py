from pyprocessing import *

# playing aroudn with pyprocessing library

def setup():
    size(800, 800)


def draw():

    vector_list = [[76, 125, 145], [82, 125, 146], [77, 126, 147], [82, 131, 150], [82, 127, 151], [87, 129, 141], [90, 125, 143], [88, 127, 144], [78, 130, 148], [83, 139, 151], [81, 139, 155], [80, 138, 152], [81, 132, 157], [79, 129, 159], [79, 126, 151], [79, 127, 158], [82, 129, 165], [80, 127, 162], [81, 133, 159], [79, 131, 157], [84, 137, 159], [82, 136, 150], [81, 134, 155], [83, 134, 162], [79, 129, 147], [83, 134, 159], [82, 132, 163], [85, 125, 170], [90, 116, 200], [86, 121, 188]]

    vector_list_2 = [[81, 131, 161], [81, 130, 161], [81, 131, 161], [80, 133, 159], [81, 135, 158], [81, 136, 158], [81, 136, 156], [80, 135, 157], [82, 132, 161], [82, 131, 165], [82, 130, 161], [81, 130, 163], [81, 130, 160], [81, 131, 162], [82, 131, 163], [82, 131, 164], [82, 132, 164], [82, 132, 161], [82, 134, 162], [82, 134, 162], [82, 134, 162], [82, 133, 163], [82, 133, 163], [83, 132, 166], [82, 132, 164], [82, 133, 161], [82, 133, 162], [82, 134, 163], [82, 133, 163], [82, 134, 165], [82, 133, 165], [82, 133, 163], [81, 135, 161], [82, 135, 161], [82, 133, 163], [80, 132, 160], [82, 133, 164], [82, 130, 164], [83, 130, 167], [82, 130, 163], [81, 132, 161], [81, 132, 161], [81, 132, 162], [82, 132, 163], [82, 132, 162], [81, 134, 160], [81, 133, 161], [81, 132, 161], [82, 129, 165]]

    sum_x = 0
    sum_y = 0
    sum_z = 0

    background(255)

    translate(100, 100, 0) # translate resets where origin is

    for vector in vector_list:
        point(0,0,0)

        v = PVector(vector[0], vector[1], vector[2])

        line(0,0,0, v.x, v.y, v.z)

        translate(v.x, v.y, v.z)

        sum_x += v.x
        sum_y += v.y
        sum_z += v.z

    translate(-sum_x+100, -sum_y, -sum_z) # translate resets where origin is

    point(0,0,0)

    for vector in vector_list_2:
        point(0,0,0)

        v = PVector(vector[0], vector[1], vector[2])

        line(0,0,0, v.x, v.y, v.z)

        translate(v.x, v.y, v.z)

def plot():
    run()

