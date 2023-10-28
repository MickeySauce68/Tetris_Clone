class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

'''
Basically the difference between a function with () and without ()
is that with () the function returns a result to the object called
while without (), the function returns a function reference to the 
callable rather than executing the function and returning a value.

A function reference is exactly what it sounds like, a reference 
to a function
'''