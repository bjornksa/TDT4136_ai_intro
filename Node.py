import numpy as np


class Node():
    def __init__(self, parent, pos, endpos, g):
        self.pos = pos
        self.parent = parent

        self.g = g
        self.h = abs(endpos[0] - pos[0]) + abs(endpos[1] - pos[1])
        # Heuristic given by manhattan distance from goal

        self.f = self.g + self.h
        self.children = []

    def get_adjacent(self):
        adj = []

        up = [self.pos[0], self.pos[1] + 1]
        down = [self.pos[0], self.pos[1] -1]
        right = [self.pos[0] + 1, self.pos[1]]
        left = [self.pos[0] - 1, self.pos[1]]

        return [up, down, right, left]

    def set_parent(self, node):
        self.parent = node

    def propogate(self, parent):
        """ Update value of g in all child nodes"""

        if self.g <= parent.g:
            return

        self.g = parent.g
        self.f = self.g + self.h
        for child in self.children:
            child.propogate(self)

