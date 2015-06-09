class Node:
    color = None
    name = None
    colorNames = {None: "NO COLOR", 1: "CPLOR 1", 2: "CPLOR 2", 3: "CPLOR 3", 4: "CPLOR 5"}

    def __init__(self, initName):
        self.name = initName

    def __str__(self):
        return "(name=" + str(self.name) + ", color=" + str(Node.colorNames[self.color]) + ")"

    def __repr__(self):
        return self.__str__()


class Graph:
    edges = set()
    nodes = []
    nodesFromKeys = {}
    graph = {}
    colors = set([1, 2, 3, 4, 5])

    def __init__(self):
        pass

    def addNode(self, node):
        self.nodes.append(node)
        self.nodesFromKeys[node.name] = node
        self.graph[node.name] = set()

    def addUndirectedEdge(self, node1, node2):
        try:
            self.graph[node1.name].add(node2)
        except:
            self.graph[node1.name] = set([node2])
        try:
            self.graph[node2.name].add(node1)
        except:
            self.graph[node2.name] = set([node1])

    def __str__(self):
        return str(self.graph)

    def inputNodes(self):
        print "Please input the number of nodes: "
        number = int(raw_input())

        for i in xrange(0, number):
            print "Please input the name of Node", i
            node = raw_input().strip()
            N = Node(node)
            self.addNode(N)

        while True:
            try:
                print "Please input the relationship of nodes (Stop with EOF): "
                node1, node2 = raw_input().strip().split(" ")
                self.addUndirectedEdge(self.nodesFromKeys[node1], self.nodesFromKeys[node2])
            except EOFError:
                break

    def color(self):
        self.nodes = sorted(self.nodes, key=self.getDegree)
        while len(self.nodes) != 0:
            node = self.nodes.pop()
            color = self.findAvaliableColor(node)
            print "Chosen color for", node, "is", node.colorNames[color]
            node.color = color
        return self.nodesFromKeys.values()

    def findAvaliableColor(self, node):
        color = set(self.colors)
        for node in self.graph[node.name]:
            print "Neighboor node:", node
            print "Colors:", color
            if node.color is not None:
                try:
                    color.remove(node.color)
                except KeyError:
                    pass
        print "Remianing colors are ", color
        if len(color) == 0:
            return None
        return color.pop()

    def getDegree(self, node):
        name = node.name
        print "Calculating the degree of node", name
        print "The degree is", len(self.graph[name])
        return len(self.graph[name])


if __name__ == '__main__':
    G = Graph()
    G.inputNodes()
    print G.color()
