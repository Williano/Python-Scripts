# Standard Library imports
import secrets
from datetime import datetime
from time import sleep
import random

# Third-party libraries imports
import networkx as nx
import matplotlib.pyplot as plt

cps_graph = nx.DiGraph()
GRAPH_NODES:list = []
no_injections:int


def get_cps_data() -> list:

    print(" ")

    number_of_cps:str = int(input("How many cyber physical systems do you need in the simulation? (eg. 1, 2, ..): "))

    for cps in range(1, number_of_cps + 1):

        print(" ")

        name:str = input(f"Enter the name of cps{cps}: ")

        cps_internal_time = input(f"Enter the interanl timer for {name}(in micro secs): ")

        get_cps_consumers(name, cps_internal_time)







def get_cps_consumers(cps_name, cps_internal_timer):

    number_of_consumers = int(input(f"How many consumer systems does {cps_name} have? (eg. 1, 2, ..): "))

    for cps_consumer in range(1, number_of_consumers +1):
            consumer:str = input(f"Enter the name of {cps_name} consumer {cps_consumer}: ")
            date_rate = input(f"Enter the data rate(kbps): ")

            cps_info = (cps_name, consumer, {"data_rate": date_rate + "kbps",
                        "internal_timer": cps_internal_timer})

            GRAPH_NODES.append(cps_info)



def generate_and_draw_graph(graph_nodes):

    cps_graph.add_edges_from(graph_nodes)

    # cps_graph.remove_node("0")
    # cps_graph.remove_node("")

    plt.figure(figsize=(8,5))

    position = nx.spring_layout(cps_graph)

    nx.draw(cps_graph, position, node_color='lightblue', with_labels=True, node_size=4000)

    rate_label = nx.get_edge_attributes(cps_graph,'data_rate')

    nx.draw_networkx_edge_labels(cps_graph, position, edge_labels=rate_label)

    plt.show()


def write_time_and_data_lost_to_file(interrupt_message,time_message, data_lost_message):

    with open("time_and_data_loss.text", "a") as lost_file:
        lost_file.write(interrupt_message)
        lost_file.write(time_message)
        lost_file.write(data_lost_message)
        lost_file.write("********************* \n")

def injection_fucntion(no_injections):

    open("time_and_data_loss.text", "w").close()

    for n in range(1, no_injections + 1):
        cps_list = []
        time_of_injection = datetime.now().microsecond

        sleep(random.uniform(0.5, 1.5))

        interrupted_cps = secrets.choice(GRAPH_NODES)
        cps1 = interrupted_cps[0]
        cps_list.append(cps1)
        cps2 = interrupted_cps[1]
        cps_list.append(cps2)
        interrupted_cps_name = interrupted_cps[0] # randomly select either one or two
        # get interrupted cps data

        print(cps_graph.out_edges(interrupted_cps_name))
        print(cps_graph.out_edges(interrupted_cps_name))

        interrupted_cps_internal_timer = float(interrupted_cps[2]["internal_timer"])
        interrupted_cps_data_rate = int("".join(list(interrupted_cps[2]["data_rate"])[:-4]))


        cps_time_loss = time_of_injection % interrupted_cps_internal_timer
        cps_data_loss = int(cps_time_loss * interrupted_cps_data_rate) / 1000000

        time_of_interrupt = f"The {n}th injection was on the CPS: {interrupted_cps_name} at the time {time_of_injection}s" + "\n"
        cps_data_lost = f"{interrupted_cps_name} -> DATA LOST: {cps_data_loss}kb" + "\n"
        cps_time_lost = f"{interrupted_cps_name} -> TIME LOST: {cps_time_loss}μs" + "\n"

        write_time_and_data_lost_to_file(time_of_interrupt, cps_data_lost, cps_time_lost)


def main():

     get_cps_data()

     print(" ")

     no_injections:int = int(input(f"Enter the number of fault injections to be done:"))

     injection_fucntion(no_injections)

    #  cps_list = []
    #  time_of_injection = datetime.now().microsecond

    #  interrupted_cps = secrets.choice(GRAPH_NODES)
    #  cps1 = interrupted_cps[0]
    #  cps_list.append(cps1)
    #  cps2 = interrupted_cps[1]
    #  cps_list.append(cps2)
    #  interrupted_cps_name = interrupted_cps[0] # randomly select either one or two
    #  # get interrupted cps data

    #  print(cps_graph.in_edges(interrupted_cps_name))
    #  print(cps_graph.in_edges(interrupted_cps_name))

    #  interrupted_cps_internal_timer = float(interrupted_cps[2]["internal_timer"])
    #  interrupted_cps_data_rate = int("".join(list(interrupted_cps[2]["data_rate"])[:-4]))


    #  cps_time_loss = time_of_injection % interrupted_cps_internal_timer
    #  cps_data_loss = int(cps_time_loss * interrupted_cps_data_rate)/1000000

    #  time_of_interrupt = f"{interrupted_cps_name} was interrupted at time {time_of_injection}s" + "\n"
    #  cps_data_lost = f"{interrupted_cps_name} -> DATA LOST: {cps_data_loss}kb" + "\n"
    #  cps_time_lost = f"{interrupted_cps_name} -> TIME LOST: {cps_time_loss}s" + "\n"


    #  write_time_and_data_lost_to_file(time_of_interrupt, cps_data_lost, cps_time_lost)


     generate_and_draw_graph(GRAPH_NODES)

if __name__ == "__main__":
    main()





# def get_cps_data() -> list:

#     graph_nodes = []

#     print(" ")

#     number_of_cps:str = int(input("How many cyber physical systems do you need in the simulation? (eg. 1, 2, ..): "))

#     for cps in range(1, number_of_cps + 1):

#         print(" ")

#         name:str = input(f"Enter the name of {cps}: ")

#         cps_internal_time = input(f"Enter the interanl timer for {name}(secs): ")

#         graph_nodes = get_cps_consumers(cps_name=name)

#         print(graph_nodes)

#     return graph_nodes


# def get_cps_consumers(cps_name) -> list:

#     graph_nodes = []

#     number_of_consumers = int(input(f"How many consumer systems does {cps_name} have? (eg. 1, 2, ..): "))

#     for cps_consumer in range(1, number_of_consumers +1):
#             consumer:str = input(f"Enter the name of consumer {cps_consumer}: ")
#             date_rate = input(f"Enter the data rate(kbps): ")

#             cps_info = (cps_name, consumer, {"data_rate": date_rate + "kbps"})

#             graph_nodes.append(cps_info)

#     return graph_nodes


# def get_cps_data() -> list:

#     graph_nodes = []

#     print(" ")

#     number_of_cps:str = int(input("How many cyber physical systems do you need in the simulation? (eg. 1, 2, ..): "))

#     for cps in range(1, number_of_cps + 1):

#         print(" ")

#         name:str = input(f"Enter the name of {cps}: ")

#         cps_internal_time = input(f"Enter the interanl timer for {name}: ")

#         number_of_consumers = int(input(f"How many consumer systems does {name} have? (eg. 1, 2, ..): "))

#         for cps_consumer in range(1, number_of_consumers +1):
#             consumer:str = input(f"Enter the name of consumer {cps_consumer}: ")
#             date_rate = input(f"Enter the data rate(kbps): ")

#             cps_info = (name, consumer, {"data_rate": date_rate + "kbps"})

#             graph_nodes.append(cps_info)

#     return graph_nodes
