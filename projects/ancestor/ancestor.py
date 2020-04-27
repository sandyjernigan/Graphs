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

    # Create a plan_to_visit Stack
    plan_to_visit = Stack()
    plan_to_visit.push(starting_node)

    # create a Set for visited_vertices
    visited_vertices = set()

    # If the input individual has no parents, the function should return -1.
    parent_node = -1
    
    # while the plan_to_visit stack is not Empty:
    while plan_to_visit.size() > 0:
        parents = []

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
            
            # Return parent with the lowest numeric ID
            if len(parents) > 0:
                parent_node = min(parents)
                
    return parent_node


# Test Function
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def testFunction(testThis, shouldResult):
    results = earliest_ancestor(test_ancestors, testThis)

    if results == shouldResult:
        print (f"Test: {testThis} -- Passed")
    else:
        print(f"Test: {testThis} -- Failed")
        print (f"Test Result: {results}")
        print (f"Should Result: {shouldResult}")

testThis = 1
shouldResult = 10
testFunction(testThis, shouldResult)

testThis = 2
shouldResult = -1
testFunction(testThis, shouldResult)

testThis = 3
shouldResult = 10
testFunction(testThis, shouldResult)

testThis = 4
shouldResult = -1
testFunction(testThis, shouldResult)

testThis = 5
shouldResult = 4
testFunction(testThis, shouldResult)

testThis = 6
shouldResult = 10
testFunction(testThis, shouldResult)

testThis = 7
shouldResult = 4
testFunction(testThis, shouldResult)

testThis = 8
shouldResult = 4
testFunction(testThis, shouldResult)

testThis = 9
shouldResult = 4
testFunction(testThis, shouldResult)

testThis = 10
shouldResult = -1
testFunction(testThis, shouldResult)

testThis = 11
shouldResult = -1
testFunction(testThis, shouldResult)