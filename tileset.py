from random import randint

class Tile():
    def __init__(self):
        self.L_neighbor = None
        self.R_neighbor = None
        self.state = bool(randint(0,1))

    def invert(self):
        self.state = not self.state

    def __str__(self):
        return str(int(self.state))

    def __repr__(self):
        return str(self)


class TileSet():
    def __init__(self):
        self.init_tiles()
        self.i_list = [0,1,2,7,-1,3,6,5,4]
        

    def init_tiles(self):
        self.tiles = [Tile() for _ in range(8)]
        for i, t in enumerate(self.tiles):
            if i == 0:
                _previous = self.tiles[-1]
            else:
                _previous = self.tiles[i-1]
            
            if i == 7:
                _next = self.tiles[0]
            else:
                _next = self.tiles[i+1]
            
            t.L_neighbor = _previous
            t.R_neighbor = _next

    def flip_tile(self, i):
        t = self.tiles[i]
        t.invert()
        t.L_neighbor.invert()
        t.R_neighbor.invert()

    def print_grid(self):
        grid = f'{self.tiles[0]}    {self.tiles[1]}    {self.tiles[2]}\n' +\
               f'{self.tiles[7]}         {self.tiles[3]}\n' +\
               f'{self.tiles[6]}    {self.tiles[5]}    {self.tiles[4]}'
        print(grid)

    def state_list(self):
        states = []
        for i in self.i_list:
            if i >= 0:
                states.append(self.tiles[i].state)
            else:
                states.append('skip')
        return states