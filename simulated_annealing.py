# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:24:52 2018

@author: Radoica Draškić
"""
import random
import math
from utils import *


MAX_T = 10000000
ALPHA = 0.9
EPSILON = 1


def mutate(points):
    """
    Mutates polygon by swapping two verices.
    """
    new_points = [x for x in points]
    i = random.randint(0, len(new_points) - 1)
    j = random.randint(0, len(new_points) - 1)
    while i == j:
        j = random.randint(0, len(new_points) - 1)
    tmp = new_points[i]
    new_points[i] = new_points[j % len(points)]
    new_points[j % len(points)] = tmp
    return new_points


def calc_probability(temperature, area):
    """
    Calculates the probability of acceptance.
    """
    if temperature == 0:
        return 0
    return math.exp(-1 * area / temperature)


def simulated_annealing(points):
    """
    Runs simulated annealing for given
    points and set global parameters.
    """
    temperature = MAX_T
    best = points
    best_area = polygon_area(points)
    while temperature >= EPSILON:
        area = polygon_area(points)
        new_points = mutate(points)
        new_points = create_simple_polygon(new_points)
        new_area = polygon_area(new_points)
        prob = random.uniform(0, 1)
        if new_area < best_area:
            best = new_points
        if new_area < area or \
            prob < calc_probability(temperature, new_area - area):
            points = new_points
        temperature *= ALPHA
    if polygon_area(points) < polygon_area(best):
        best = points
    return points, best
