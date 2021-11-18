# Classes that graph visitors can use for "to do" lists of vertices waiting to be
# visited. All such classes provide at least the following methods:
#   - reset(), a parameterless method with no return value that makes a list empty.
#   - isEmpty(), a parameterless method that returns True if a list is empty and
#     False otherwise.
#   - insert( v ), a method that inserts a vertex into a list.
#   - removeNext(), a parameterless method that removes the next vertex to visit
#     from a list and returns that vertex. Returns None if the list is empty.

# Created March 2019 by Doug Baldwin as part of a prototype for lectures and exercises
# related to graphs in Math 240.

# Edited March 2019 by Jack Truckenmiller, adding the VisitorList superclass and changing up the Stack class
# to work with this superclass as well as adding the Queue class, as part of Assignment 4 for Math 240.






# A class that represents stacks, i.e., lists in which insertion and removal act in
# a last-in-first-out fashion.

class Stack :


    """ A stack is represented by a list of data items, where items are both inserted and removed from the 
    front of the list. """


    # Initialize a stack to be empty.

    def __init__( self ) : 
        self.reset()


    # Reset a list to be empty.

    def reset( self ) : self.items = []



    # Test whether a list is empty.

    def isEmpty( self ) : return len( self.items ) == 0

    # Insert a vertex into a stack.

    def insert( self, vertex ) : self.items = [vertex] + self.items


    # Remove the next item from a stack and return it.

    def removeNext( self ) :

        # Check that the stack isn't empty (returning None if it is), and if not, take
        # out the first item and return it.
        if self.isEmpty() :
            return None
        else :
            result = self.items[0]
            self.items = self.items[ 1 : ]
            return result