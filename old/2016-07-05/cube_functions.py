#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

@author: bjorn
"""

def cube_volume(x):
    ''' This function returns the volume of a cube with the edge x.

        Cubes look like this:

               e-------f
              /|      /|
             / |     / |
            a--|----b  |
            |  g----|--h
            | /     | /
            c-------d


            a->b = x
            a->c = x
            a->e = x

            Volume = x*x*x


    '''
    volume = x*x*x

    return volume


def space_diagonal(x):
    sd = (x*x*x)**0.5
    return sd


def cube_area(x):
    area = 6*x*x
    return area



if __name__ is "__main__":

    assert cube_volume(10)  == 1000

    assert cube_volume(100) == 1000000

    assert space_diagonal(9) ==27.0

    assert cube_area(10) == 600



