# Import Graph Class
from graph import Graph
from util import Stack, Queue

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
    ancestorsGraph = Graph()
    # ancestorsList = []

    # Add ancestors data to Graph
    for dataset in ancestors:

        # For each set check both values
        for data in dataset:

            # Check if vertex exists
            if not data in ancestorsGraph.vertices.keys():

                # Add vertex if does not exist
                ancestorsGraph.add_vertex(data)

    # Add ancestors connections to Graph
    for dataset in ancestors:
        ancestorsGraph.add_edge(dataset[0], dataset[1])
                
    # print(ancestorsGraph.vertices)

    ''' Get The Earliest Ancestor '''
    parents = []

    # Create a plan_to_visit Stack
    plan_to_visit = Stack()
    plan_to_visit.push(starting_node)

    # create a Set for visited_vertices
    visited_vertices = set()
    
    # while the plan_to_visit stack is not Empty:
    while plan_to_visit.size() > 0:

        # pop the first vertex from the stack
        current_vertex = plan_to_visit.pop()

        # if its not been visited
        if current_vertex not in visited_vertices:

            # mark it as visited, (add it to visited_vertices)   
            visited_vertices.add(current_vertex)

            # Check vertices for parent/child
            for parent, child in ancestorsGraph.vertices.items():
                
                # Check if node is a child
                if current_vertex in child:

                    # Check if already in list
                    if parent not in visited_vertices:

                        # Add to list
                        plan_to_visit.push(parent)
                        parents.append(parent)

    print (parents)

    # If no parents found, return with -1
    if len(parents) == 0:
        return -1

    # if only 1 parents found, return with the parent
    if len(parents) == 1:
        return parents[0]

    # More than 1 parent found, return the one with the lowest numeric ID
    return min(parents)


# Test Function
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def testFunction(testThis, shouldResult):
    print (f"Test: {testThis}")
    print (f"Test result: {earliest_ancestor(test_ancestors, testThis)}")
    print (f"Should result: {shouldResult}")

testThis = 1
shouldResult = 10
testFunction(testThis, shouldResult)

testThis = 2
shouldResult = -1
testFunction(testThis, shouldResult)

# testThis = earliest_ancestor(test_ancestors, 3)
# testResult = 10
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 4)
# testResult = -1
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 5)
# testResult = 4
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 6)
# testResult = 10
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 7)
# testResult = 4
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 8)
# testResult = 4
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 9)
# testResult = 4
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 10)
# testResult = -1
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")

# testThis = earliest_ancestor(test_ancestors, 11)
# testResult = -1
# print (f"Test result: {testThis}")
# print (f"Should result: {testResult}")