"""
Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0, 0],
           [1, 1, 0, 1, 1, 0],
           [0, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [1, 1, 0, 0, 0, 0]]
island_counter(islands) # returns 4
"""
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors():
  pass

def dft(row_index, col_index, matrix, visited_verticies):
  neighbors_to_visit = Stack()
  neighbors_to_visit.push((row_index, col_index))

  while neighbors_to_visit.size() > 0:
    current_vertex = neighbors_to_visit.pop()
    if (row_index, col_index) not in visited_verticies:
      visited_verticies.add((row_index, col_index))
      for neighbor in get_neighbors():
        neighbors_to_visit.push(neighbor)

def island_counter(matrix):
    # keep track of visited verticies
    visited_verticies = set()
    island_count = 0
    # go through the matrix of island data
    for row_index in range(matrix):
      for col_index in range(matrix[row_index]):
        # have we seen, whats at matrix[row_index][col_index]
        if (row_index, col_index) not in visited_verticies and matrix[row_index][col_index] == 1:
          dft(row_index, col_index, matrix, visited_verticies)
          island_count += 1
    # if we see a 1, and its not visited
        # do a DFT / BFT
            # keep marking each visited vertex as visited
        # once DFT is done, add 1 to our island count
    
    
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
print(island_counter(islands))