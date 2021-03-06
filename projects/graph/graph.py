"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return set() #return empty set, vertex_id isn't in graph

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        # use a deque like a queue, append to end (enqueue), 
        # pop from front (dequeue)
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            curr_vertex = queue.popleft() # dequeue from front
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                print(curr_vertex)
                for neighbor in self.get_neighbors(curr_vertex):
                    queue.append(neighbor) # enqueue to end

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        #use a deque like a stack, append to end (push), pop from end (pop)
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            curr_vertex = stack.pop() # pop from end
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                print(curr_vertex)
                for neighbor in self.get_neighbors(curr_vertex):
                    stack.append(neighbor) # push to end

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        self.dft_recursive_helper(starting_vertex, visited)

    def dft_recursive_helper(self, starting_vertex, visited):
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    self.dft_recursive_helper(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = deque()
        queue.append([starting_vertex])
        while len(queue) > 0:
            curr_path = queue.popleft()
            curr_vertex = curr_path[-1]
            if curr_vertex == destination_vertex:
                return curr_path
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                for neighbor in self.get_neighbors(curr_vertex):
                    newPath = list(curr_path)
                    newPath.append(neighbor)
                    queue.append(newPath)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = deque()
        stack.append([starting_vertex])
        while len(stack) > 0:
            curr_path = stack.pop()
            curr_vertex = curr_path[-1]
            if curr_vertex == destination_vertex:
                return curr_path
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                for neighbor in self.get_neighbors(curr_vertex):
                    newPath = list(curr_path)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, visited)

    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        curr_vertex = curr_path[-1]
        if curr_vertex == destination_vertex:
            return curr_path
        visited.add(curr_vertex)
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                new_path = list(curr_path)
                new_path.append(neighbor)
                res = self.dfs_recursive_helper(new_path, destination_vertex, visited)
                if len(res) > 0:
                    return res
        return []



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
