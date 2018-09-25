# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:24:32 2018

@author: Radoica Draškić
"""
import matplotlib.pyplot as plt
import os
import numpy as np


class Test:
    """
    Class for holding informations
    about test case.
    """
    def __init__(self, num_of_points, points):
        self.num_of_points = num_of_points
        self.points = points


def draw_polygon(points, name):
    """
    Draws a polygon and saves image
    in specified directory.
    """
    coord = [x for x in points]
    coord.append(coord[0])          #repeat the first 
                                    #point to create a 'closed loop'
    
    xs, ys = zip(*coord)            #create lists of x and y values
    plt.plot(xs, ys, marker='o')
    plt.axis('off')
    left = np.min(xs)
    right = np.max(xs)
    bottom = np.min(ys)
    top = np.max(ys)
    font = {'size': 16}
    plt.text(left - 0.15 * (right - left), 
             bottom - 0.15 * (top - bottom), 
             r'$' + 'Area = ' + str(polygon_area(points)) + '$', 
             fontdict=font)
    plt.savefig(name)
    plt.gcf().clear()
    
    
def read_data():
    """
    Reads test data.
    """
    folder = "test primeri"    
    tests = []
    for root, _, files in os.walk(folder):
        for file in files:
            content = open(os.path.join(root, file), 'r').readlines()
            num_of_points = int(content[0])
            points = []
            for i in range(num_of_points):
                points.append(
                    [float(x) for x in content[i + 1].split(" ")])
            test = Test(num_of_points, points)
            tests.append(test)
    return tests


def ccw(a, b, c):
    """
    Checks if points a, b and c
    are in counter-clockwise order.
    """
    result = (c[0] - b[0]) * (a[1] - b[1]) - (c[1] - b[1]) * (a[0] - b[0])
    if result < 0: 
        return -1
    if result > 0:
        return 1
    return 0


def intersect(a, b, c, d):
    """
    Checks if segments given by a-b and c-d
    intersect.
    """
    if ccw(a, c, d) == ccw(b, c, d):
        return False
    elif ccw(a, b, c) == ccw(a, b, d):
        return False   
    else:
        return True
    

def check_intersection(points, i, j):
    """
    Checks for intersection for two points
    in given array of points.
    """
    return intersect(points[i], points[(i + 1) % len(points)], 
                     points[j], points[(j + 1) % len(points)])
    

def find_intersection(points):
    """
    Searches for intersection in given polygon.
    """
    for i in range(len(points)):
            for j in range(2, len(points) - 2):
                inter = check_intersection(
                        points, i, (i + j) % len(points))
                if inter:
                    return [min(i, (i + j) % len(points)),
                                max(i, (i + j) % len(points))]


def create_simple_polygon(points):
    """
    Creates simple polygon from provided list
    of polygon vertices by swapping intersecting
    edges while they exist.
    """
    while True:
        intersection = find_intersection(points)                    
        if intersection:
            first = []
            for i in range(intersection[0] + 1, 
                           intersection[1] + 1):
                first.append(points[i])
            second = []
            for i in range(intersection[1] + 1, len(points)):
                second.append(points[i])
            for i in range(intersection[0] + 1):
                second.append(points[i])
            for i in range(len(second)):
                first.append(second[len(second) - i - 1])
            points = first
        else:
            break
    return points


def polygon_area(points):
    """
    Calculates the polygon area.
    """
    area = 0
    for i in range(len(points)):
        area += points[i][0] * points[(i + 1) % len(points)][1]
        area -= points[i][1] * points[(i + 1) % len(points)][0]
    return abs(area / 2)


def find_permutation(start, end):
    perm = []
    for e in end:
        cnt = 1
        for s in start:
            if s[0] == e[0] and s[1] == e[1]:
                perm.append(cnt)
                break
            cnt += 1
    return perm
