"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex_id in self.vertices:
            return("Warning that vertex_id already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
      # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create an empty queue
        # Add the starting vertex_id to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
        # Dequeue, the first vertex
        # Check if it's been visited
        # If it has not been visited...
        # Mark it as visited
        # Then add all neighbors to the back of the queue
        # Create an empty queue
        queue = Queue()
        # get starting point
        queue.enqueue(starting_vertex)
        # create set to track visited
        visited = set()
        # run algo while items are present in queue
        while queue.size() > 0:
            vertex = queue.dequeue()
            # If not visited
            if vertex not in visited:
                # print the vertex and add it to visited
                print(vertex)
                visited.add(vertex)
                # get the edges/neighbors
                for neighbor in self.get_neighbors(vertex):
                    # add the edge to the queue
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # same a bft except use stack instead of queue
        # TODO
        # create stack
        stack = Stack()
        # get starting point
        stack.push(starting_vertex)
        # create set to keep track of visited
        visited = set()
        # run algo while items are present in stack
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
       # create queue
        queue = Queue()
        # Create starting point
        queue.enqueue([starting_vertex])
        # create visited set
        visited = set()
        # while items in set run algo
        while queue.size() > 0:
            # Pop 1st item
            path = queue.dequeue()
            vertex = path[-1]
            # if not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # for each edge add the item
                for next_vert in self.get_neighbors(vertex):
                    # copy path to avoid pass by reference bug
                    # mak a copy of path rather then the reference
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None

    def earliest(self, starting_vertex):
        stack = Stack()
        # Put the starting point in that
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # Track the path
        longest_path = [starting_vertex]
        # While there is stuff in the queue/stack
        while stack.size() > 0:

            #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                visited.add(vertex)
        # For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy the path
                    new_path = list(path)
                    new_path.append(next_vert)
                    # Add that edge to the queue/stack
                    stack.push(new_path)
                    # compare the path lengths and update
                    if len(new_path) > len(longest_path):
                        longest_path = new_path
                    # path may be same size size but path has changed so check last element for change
                    if len(new_path) == len(longest_path) and new_path[-1] != longest_path[-1]:
                        longest_path = new_path
        return longest_path
