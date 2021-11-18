
# Created May 2019 by Salvador Galarza and Jack Truckenmiller for use in an object-oriented chess game for Math 240.

import pygame
from GraphErrors import DuplicateEdgeError

black = (0,0,0)
red = (255,0,0)
yellowish = (200, 150, 0)

class Tile :
    def __init__(self, name, x, y):
        self.name = name
        self.width = 90
        self.height = 90
        self.x = x
        self.y = y
        self.color = yellowish
        self.mark = False
        self.piece = None
        self.edges = []
        self.hitbox = [self.x,self.y,self.width,self.height]

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height], 5)

    def collidepoint(self,n,w):
        if (n[0] >= self.hitbox[0] and n[0] <= self.hitbox[0]+self.width) and (n[1] >= self.hitbox[1]) and (n[1] <= self.hitbox[1]+self.height):
            return True

    # Give this tile a new edge, defined by the tile it goes to. If this tile already has an
    # edge to the "new" neighbor, raise a DuplicateEdgeError exception.

    def addNeighbor( self, neighbor ) :

        # If any of this tile's existing edges goes to the new neighbor, raise an exception.
        # Otherwise add the neighbor to this tile's edge list.

        if any( [ e.tile is neighbor for e in self.edges ] ) :
            raise DuplicateEdgeError( self.name + " to " + neighbor.name )
        else :
            self.edges.append( Edge(neighbor) )

    def mark_tile( self, mark ) :

        if mark :
            self.mark = mark
        else :
            self.mark = mark



class Edge :

    """ Object that represents an edge between two tiles, not the trash Microsoft web browser. """

    # Initialize an edge with the tile it goes to.

    def __init__( self, tile ):
        self.tile = tile
