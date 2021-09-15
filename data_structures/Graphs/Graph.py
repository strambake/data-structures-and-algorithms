from typing import Generic, List, TypeVar

T = TypeVar('T')
class Graph(Generic[T]):
    def __init__(self) -> None:
        self.__graph = {}


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
        output = []
        visited = set()
        queue = []

        if startNode in self.__graph:
            queue.append(startNode)
            visited.add(startNode)

            while queue:
                currNode = queue.pop(0)
                output.append(currNode)

                for connectedNode in self.__graph[currNode]:
                    if connectedNode not in visited:
                        queue.append(connectedNode)
                        visited.add(connectedNode)

        return output


    def dfs(self, startNode: T):
        visited = set()
        output = []

        self.__dfs(startNode, visited, output)

        return output


    def hasPath(self, start: T, dest: T) -> bool:
        visited = set()
        return self.__hasPath(start, dest, visited)


    def numConnectedComponent(self) -> int:
        return len(self.__getComponents())


    def largetComponent(self) -> int:
        return max(len(component) for component in self.__getComponents())


    def __hasPath(self, currentNode: T, dest: T, visited: set) -> bool:
        visited.add(currentNode)
        if currentNode == dest:
            return True

        for neighbor in self.__graph[currentNode]:
            if neighbor not in visited:
                if self.__hasPath(neighbor, dest, visited):
                    return True
        return False


    def __dfs(self, currNode: T, visited: set, output: List[int]) -> None:
        visited.add(currNode)
        output.append(currNode)

        for neighbor in self.__graph[currNode]:
            if neighbor not in visited:
                self.__dfs(neighbor, visited, output)


    def __getComponents(self) -> List[List[int]]:
        components = []
        visited = set()

        for node in self.__graph.keys():
            output = []
            if node not in visited:
                self.__dfs(node, visited, output)

                components.append(output)
        return components
