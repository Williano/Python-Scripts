from itertools import combinations, groupby
import random
import networkx as nx
import matplotlib.pyplot as plt


def gnp_random_connected_graph(nodes, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(1, nodes), 2)

    graph = nx.Graph()

    graph.add_nodes_from(range(1, nodes))

    if p <= 0:
        return graph
    if p >= 1:
        return nx.complete_graph(nodes, create_using=graph)

    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        graph.add_edge(*random_edge)


        for e in node_edges:
            if random.random() < p:
                graph.add_edge(*e)


    return graph


def main():

    print(" ")

    number_of_cps = int(input("How many cyber physical systems do you need in the simulation? (eg. 1, 2, ..): "))

    seed = random.randint(1,10)
    probability = 0.1
    G = gnp_random_connected_graph(number_of_cps ,probability)

    plt.figure(figsize=(8,5))
    nx.draw(G, node_color='lightblue', with_labels=True, node_size=500)
    plt.show()


if __name__ == "__main__":
    main()