from abc import ABC

class Node(ABC):
    def __init__(self):
        self.ancestor = None
        