import networkx as nx
import matplotlib.pyplot as plt


def get_cps_data() -> list:

    graph_nodes = []

    print(" ")

    number_of_cps = int(input("How many cyber physical systems do you need in the simulation? (eg. 1, 2, ..): "))

    for cps in range(1, number_of_cps + 1):

        print(" ")

        name:str = input(f"Enter the name of {cps}: ")
        consumer:str = input(f"Enter the name of consumer: ")
        date_rate = input(f"Enter the data rate(kbps): ")

        cps_info = (name, consumer, {"data_rate": date_rate + "kbps"})

        graph_nodes.append(cps_info)


    return graph_nodes

def generate_and_draw_graph(graph_nodes):

    cps_graph = nx.DiGraph()

    cps_graph.add_edges_from(graph_nodes)

    cps_graph.remove_node("0")

    plt.figure(figsize=(8,5))

    position = nx.spring_layout(cps_graph)

    nx.draw(cps_graph, position, node_color='lightblue', with_labels=True, node_size=4000)

    rate_label = nx.get_edge_attributes(cps_graph,'data_rate')

    nx.draw_networkx_edge_labels(cps_graph, position, edge_labels=rate_label)

    plt.show()


def main():

     graph_nodes = get_cps_data()

     generate_and_draw_graph(graph_nodes)

if __name__ == "__main__":
    main()