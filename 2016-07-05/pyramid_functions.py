#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cube_functions import cube_volume


def pyramid_volume(number_of_layers, edge):

    # This function returns the total volume a pyramid of cubic blocks
    # The size of the edge block is edge meters (float).
    # The number of layers are given by the int number_of_layers
    #
    #
   
    volume = 0

    for layer in range(number_of_layers+1):
        volume = volume + (layer * layer) * cube_volume(edge)

    return volume


def pyramid_weight(L, x):

    limestone_density = 2500 # kg/m3

    pw = pyramid_volume(L, x) * limestone_density

    return pw/1000

if __name__ is "__main__":
    print("cheops pyramid weigh around", pyramid_weight(210, 0.8), "metric tons")


