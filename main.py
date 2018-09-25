# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:20:03 2018

@author: Radoica Draškić
"""
from simulated_annealing import *
from utils import *
import os


if __name__ == '__main__':
    tests = read_data()
    
    for k in range(5):
        print("ITERATION # " + str(k))
        for i in range(len(tests)):
            points = tests[i].points
            start = points
            points = create_simple_polygon(points)
            draw_polygon(points, os.path.join(
                    'images', str(k) + str(i) + '_start.png'))
            points, best = simulated_annealing(points)
            print('TEST CASE: ' + str(i))
            print('BEST: ' + str(polygon_area(best)), end=' ')
            for j in find_permutation(start, best):
                print(j, end=' ')
            print('')
            print('END:  ' + str(polygon_area(points)), end=' ')
            for j in find_permutation(start, points):
                print(j, end=' ')
            print('\n')
            draw_polygon(points, os.path.join(
                    'images', str(k) + str(i) + '_end.png'))
            draw_polygon(best, os.path.join(
                    'images', str(k) + str(i) + '_best.png'))
        print('')