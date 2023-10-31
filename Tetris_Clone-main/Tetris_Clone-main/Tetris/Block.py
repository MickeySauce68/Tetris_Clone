class Block:
    def __init__(self, id):
        self.id = id    
        self.cells = {}                                               
        self.cells_size = 30
        self.rotation_state = 0

