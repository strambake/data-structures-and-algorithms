from typing import Generic, List, TypeVar


T = TypeVar('T')
class Graph(Generic[T]):
    def __init__(self) -> None:
        self.__graph = dict()


    def addNode(self, node: T) -> None:
        if node not in self.__graph:
            self.__graph[node] = []


    def addDirectedEdge(self, src: T, dest: T) -> None:
        if src not in self.__graph:
            self.__graph[src] = []

        if dest not in self.__graph:
            self.__graph[dest] = []

        self.__graph[src].append(dest)


    def addUndirectedEdge(self, src: T, dest: T) -> None:
        if src not in self.__graph:
            self.__graph[src] = []

        if dest not in self.__graph:
            self.__graph[dest] = []

        self.__graph[src].append(dest)
        self.__graph[dest].append(src)



    def bfs(self, startNode: T) -> str:
        output = ''
        visited = []
        queue = []

        if startNode in self.__graph:
            queue.append(startNode)
            visited.append(startNode)

            while len(queue):
                currNode = queue.pop(0)
                output +=  '{} '.format(currNode)

                for connectedNode in self.__graph[currNode]:
                    if connectedNode not in visited:
                        queue.append(connectedNode)
                        visited.append(connectedNode)

        return output


    def dfs(self, startNode: T):
        global visited, output

        visited = set()
        output = ''

        self.__dfs(startNode)

        return output


    def hasPath(self, start: T, dest: T) -> bool:
        global visited
        visited = set()
        return self.__hasPath(start, dest)


    def numConnectedComponent(self) -> int:
        return len(self.__getComponents())


    def largetComponent(self) -> int:
        return max(len(component) for component in self.__getComponents())


    def __hasPath(self, currentNode: T, dest: T) -> bool:
        global visited

        visited.add(currentNode)
        if currentNode == dest:
            return True
        else:
            for neighbor in self.__graph[currentNode]:
                if neighbor not in visited:
                    if self.__hasPath(neighbor, dest):
                        return True
            return False


    def __dfs(self, currNode: T) -> None:
        global visited, output

        visited.add(currNode)
        output.append(currNode)

        for neighbor in self.__graph[currNode]:
            if neighbor not in visited:
                self.__dfs(neighbor)


    def __getComponents(self) -> List[List[int]]:
        components = []
        global visited, output
        visited = set()

        for node in self.__graph.keys():
            output = []
            if node not in visited:
                self.__dfs(node)

                components.append(output)
        return components



if __name__ == "__main__":
    g = Graph[int]()
    g.addUndirectedEdge(1, 2)
    g.addNode(3)
    g.addUndirectedEdge(4, 6)
    g.addUndirectedEdge(5, 6)
    g.addUndirectedEdge(8, 6)
    g.addUndirectedEdge(7, 6)

    print('There is {} connected components'.format(g.numConnectedComponent()))
    print('Largest component {}'.format(g.largetComponent()))
