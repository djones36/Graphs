from graph import Graph


def earliest_ancestor(ancestors, starting_vertex):
    # Initialize the graph

    ag = Graph()

    # Loop through ancestor adn add each set as vertices

    for each_group in ancestors:
        ag.add_vertex(each_group[0])
        ag.add_vertex(each_group[1])

    # Add edges

    for each_group in ancestors:
        ag.add_edge(each_group[1], each_group[0])

    ancestor = ag.earliest(starting_vertex)

    if ancestor[-1] == starting_vertex:
        return -1
    else:
        return ancestor[-1]

    list_of_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7)
                         (4, 5), (4, 8), (8, 9), (11, 9), (10, 1)]

    earliest_ancestor(list_of_ancestors, 3)
