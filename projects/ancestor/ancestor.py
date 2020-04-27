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

def earliest_ancestor(ancestors, starting_node):
    '''
    Write a function that, given the dataset and the ID of an individual 
    in the dataset, returns their earliest known ancestor – 
    the one at the farthest distance from the input individual. 

    If there is more than one ancestor tied for "earliest", 
    return the one with the lowest numeric ID. 

    If the input individual has no parents, the function should return -1.

    The input will not be empty.
    There are no cycles in the input.
    There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
    IDs will always be positive integers.
    A parent may have any number of children.

    '''
    # Using the Depth First method 
    # Create an empty stack
    plan_to_visit = Stack()
    plan_to_visit.push([starting_node])

    # Create a Set for visited ancestors
    visited_nodes = set()

    # while the plan_to_visit stack is not Empty:
    while plan_to_visit.size() > 0:

        # Remove the first node from the stack
        path = plan_to_visit.pop()

        # Get current_vertex
        current_node = path[-1]

        # if its not been visited
        if current_node not in visited_nodes:

            # check if its the target
            if current_vertex == destination_vertex:
                # Return the path
                return path
            
            # mark it as visited, (add it to visited_vertices)   
            visited_vertices.add(current_vertex)

            # add all unvisited neighbors to the stack
            for neighbor in self.get_neighbors(current_vertex):
                # duplicate the path
                new_path = list(path)
                # add the neighbor
                new_path.append(neighbor)
                # add the new path to the queue
                plan_to_visit.push(new_path)