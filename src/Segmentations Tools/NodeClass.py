from typing import Optional, Tuple, List

@dataclass
class Node:
    """Tree node representing an image region and its split"""
    image     : np.ndarray                # original image
    bbox      : Tuple[slice, slice]       # Bounding box in original image coordinates
    split_pos : int = -1                  # position of the spli in the image that produce this node (-1: None)
    direction : Optional[str] = None      # give the direction of the split "horizontal" or "vertical" producing this node
    ratio     : float = 0                 # value of the ratio producing this split
    left      : Optional['Node'] = None   # left child node (or upper child node) if this node is split  (None: no split)
    right     : Optional['Node'] = None   # right child node (or lower child node) if this node is split (None: no split)
    
    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    #@property
    #def is_root(self):
    #    return self.image.shape == self.bbox
