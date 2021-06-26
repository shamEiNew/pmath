import numpy as np

class Group:
    

    def __init__(self, order):

        if isinstance(order, int):
             self._order = order
        else:
            raise TypeError(f"The order of the group must be an integer not {type(order)}")
        
    @property
    def order(self):
        return self._order
        

class CyclicGroup(Group):
    """
    This class generates an instance of cyclic group of order n.
    """
    
    def __init__(self, order):
        super().__init__(order)

def isAbelian(_cls):

    if not isinstance(_cls, Group):
        raise TypeError(f"Expected group object as argument, given {_cls} {type(_cls)}")
    
    if isinstance(_cls, CyclicGroup):
        return True


