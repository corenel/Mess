import networkx as nx
INF = float('inf')


def inputNodes():
    print "Please input the number of nodes: "
    number = int(raw_input())
    for i in xrange(0, number):
        print "Please input the name of Node ", i
        node, inputDemand = raw_input().strip().split(" ")
        G.add_node(node, demand=int(inputDemand))

    while True:
        try:
            print "Please input the cost of nodes (Stop with EOF): "
            node1, node2, cost = raw_input().strip().split(" ")
            G.add_edge(node2, node1, weight=float(cost), capacity=INF)
        except EOFError:
            break
    return G

G = nx.DiGraph()
G = inputNodes()
flowCost, flowDict = nx.capacity_scaling(G)
print flowCost
print flowDict
