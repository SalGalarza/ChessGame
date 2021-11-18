# Class that represents the chess board. In reality this is an directed graph where 
# the tiles are the vertices. The tiles contain most of the information about the
# board/graph, so this class is a mostly a wrapper around a set tiles/vertices and
# provides some convenience features like initializing the set or searching it for 
# a specific tile.

# Created by Jack Truckenmiller in May 2019 for the object-oriented chess game for
# Math 240. Based on code given by Doug Baldwin in Graph.py.


from tile import Tile
from GraphErrors import GraphFormatError, NoSuchVertexError




class Board :




    # Internally, a board consists of a dictionary of tiles, keyed by vertex names.




    # Read a board from a text stream. Each line in the stream should either be empty, be a
    # comment, or be a tile definition. Comment lines begin with "#"; all other non-empty
    # lines are tile definitions. A tile definition is a series of space-separated words,
    # where the first word is the tile name, and the remaining words are the neighbors 
    # representing the different piece movements valid from the tile. If the stream has this
    # format, this method initializes the board accordingly. If the stream doesn't have
    # the right format, or this method detects any other errors while building the board,
    # this method raises exceptions as follows:
    #   - GraphFormatError if the text in the stream doesn't have the expected format.
    #   - NoSuchVertexError if an edge in the graph refers to a vertex that isn't defined.

    def __init__( self, stream ) :


        # This method makes 2 passes over the tile data. The first, done while reading the
        # file, creates a dictionary of empty tiles. The second pass, done over a list of
        # tile lines from the file, adds edges between those tiles.


        # First pass: read the file into a list of lists of words, each list being a tile
        # definition. While breaking tile definitions into their constituent words, create
        # tile objects for each  definition. Also check that every tile definition is unique,
        # reporting the first invalid line found by this test, including its line number.

        self.tiles = {}

        tileDefinitions = []

        line = stream.readline()
        lineNumber = 1

        xstep = 0
        ystep = 0

        while line != "" :

            if line[0] != "#" :

                words = line.split()

                if len(words) > 0 :

                    name = words[0]
                    if name not in self.tiles :
                        self.tiles[name] = Tile( name, xstep + 40, ystep + 40 )
                        if xstep == 630 :
                            xstep = 0
                            ystep += 90
                        else :
                            xstep += 90
                    else :
                        raise GraphFormatError( "Duplicate vertex '" + name + "' on line " + str(lineNumber) )

                    tileDefinitions.append( words )


            line = stream.readline()
            lineNumber += 1


        # Second pass: step through the tile definitions, adding each one's edges to the
        # corresponding tile object.

        for tileDef in tileDefinitions :

            currentTile = self.tiles[ tileDef[0] ]

            for i in range( 1, len(tileDef) ) :

                neighborName = tileDef[i]

                if neighborName in self.tiles:

                    currentTile.addNeighbor( self.tiles[neighborName] )

                else :
                    raise NoSuchVertexError( neighborName )




    # Find and return a tile within a board given its name. If there is no vertex with the
    # requested name, raise a NoSuchVertexError exception.

    def findVertex( self, name ) :

        if name in self.tiles :
            return self.tiles[ name ]
        else :
            raise NoSuchVertexError( name )




    # Clear all data associated with board traversals from the tiles. Clear
    # marks to a client-specified value,.

    def clear( self, clearMark ) :


        # Step through all the tile objects in this board, clearing each.

        for tile in self.tiles.values() :
            tile.mark_tile( clearMark )

    def draw( self, win ) :

        """ Runs the draw method on all of the tiles in the board. """

        for tile in self.tiles.values() :
            tile.draw( win )