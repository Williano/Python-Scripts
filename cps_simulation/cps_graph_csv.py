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
number_of_cps:int
number_of_consumers:int
negotiating_delay:int


def get_cps_data() -> list:

    print(" ")

    number_of_cps:int = int(input("How many cyber physical systems do you need in the simulation? (eg. 1, 2, ..): "))

    for cps in range(1, number_of_cps + 1):

        print(" ")

        name:str = input(f"Enter the name of cps{cps}: ")

        cps_internal_time = input(f"Enter the interanl timer for {name}(in micro secs): ")

        cps_graph.add_node(name, internal_timer= cps_internal_time)

        get_cps_consumers(name)


def get_cps_consumers(cps_name):

    number_of_consumers = int(input(f"How many consumer systems does {cps_name} have? (eg. 1, 2, ..): "))

    for cps_consumer in range(1, number_of_consumers +1):
            consumer:str = input(f"Enter the name of {cps_name} consumer {cps_consumer}: ")
            date_rate = input(f"Enter the data rate(kbps): ")

            cps_info = (cps_name, consumer, {"data_rate": date_rate + "kbps"})

            GRAPH_NODES.append(cps_info)


def add_edges_to_node():
    cps_graph.add_edges_from(GRAPH_NODES)


def generate_and_draw_graph():

    plt.figure(figsize=(8,5))

    position = nx.spring_layout(cps_graph)

    nx.draw(cps_graph, position, node_color='lightblue', with_labels=True, node_size=4000)

    rate_label = nx.get_edge_attributes(cps_graph,'data_rate')

    nx.draw_networkx_edge_labels(cps_graph, position, edge_labels=rate_label)

    plt.show()


def write_time_and_data_lost_to_file(cps_name, injection_time, internal_timer, data_lost, time_lost, number_of_cps_consumers):


    with open("time_and_data_loss.csv", "a") as lost_file:
        lost_file.write(cps_name)
        lost_file.write(injection_time)
        lost_file.write(internal_timer)
        lost_file.write(data_lost)
        lost_file.write(time_lost)
        lost_file.write(number_of_cps_consumers)

def append_new_line_to_file():
    with open("time_and_data_loss.csv", "a") as lost_file:
        lost_file.write("\n")



def log_consumer_data_and_time_lost_to_file(negotiating_delay, interrupted_cps_name, time_of_injection, interrupted_cps_data_rate):


        consumers_of_interrupted_cps = list(cps_graph.out_edges(interrupted_cps_name, data=True))

        decendants_of_interrupted_cps: list = []

        for consumer in range(len(consumers_of_interrupted_cps)):

            consumer_name = consumers_of_interrupted_cps[consumer][1]
            decendants_of_interrupted_cps.append({"consumer_name": consumer_name, "negotiating_delay": 0})

            descendants = list(nx.descendants(cps_graph, consumer_name))

            cps_decendants = [{"consumer_name": descendant, "negotiating_delay": negotiating_delay} for index, descendant in enumerate(descendants)]

            decendants_of_interrupted_cps.extend(cps_decendants)


        for index, consumer in enumerate(decendants_of_interrupted_cps):

            consumer_name = consumer["consumer_name"]

            consumer_of_interrupted_cps_internal_timer = float(nx.get_node_attributes(cps_graph, 'internal_timer')[consumer_name])

            total_data_rate = sum([int("".join(list(edge[2]["data_rate"])[:-4])) for index, edge in enumerate(list(cps_graph.out_edges(consumer_name, data=True)))])

            consumer_time_loss = (time_of_injection % consumer_of_interrupted_cps_internal_timer) + (negotiating_delay + consumer["negotiating_delay"])
            consumer_data_loss = int(consumer_time_loss * total_data_rate) / 1000000


            cps_consumer_name = f"{consumer_name},"
            cps_consumer_internal_timer = f"{consumer_of_interrupted_cps_internal_timer},"
            cps_consumer_data_lost = f"{consumer_data_loss},"
            cps_consumer_time_lost = f"{consumer_time_loss},"


            write_time_and_data_lost_to_file(cps_consumer_name, "", cps_consumer_internal_timer, cps_consumer_data_lost, cps_consumer_time_lost, "")

        append_new_line_to_file()


def inject_fault(no_injections, negotiating_delay):

    open("time_and_data_loss.csv", "w").close()

    for n in range(1, no_injections + 1):

        time_of_injection = datetime.now().microsecond

        sleep(random.uniform(0.5, 1.5))

        interrupted_cps = secrets.choice(GRAPH_NODES)
        interrupted_cps_name = interrupted_cps[0]

        total_data_rate = sum([int("".join(list(edge[2]["data_rate"])[:-4])) for index, edge in enumerate(list(cps_graph.out_edges(interrupted_cps_name, data=True)))])


        interrupted_cps_internal_timer = float(nx.get_node_attributes(cps_graph, 'internal_timer')[interrupted_cps_name])
        interrupted_cps_data_rate = total_data_rate


        cps_time_loss = time_of_injection % interrupted_cps_internal_timer
        cps_data_loss = int(cps_time_loss * interrupted_cps_data_rate) / 1000000

        cps_name = f"{interrupted_cps_name},"
        injection_time = f"{time_of_injection},"
        cps_internal_timer = f"{interrupted_cps_internal_timer},"
        cps_data_lost = f"{cps_data_loss},"
        cps_time_lost = f"{cps_time_loss},"
        number_of_cps_consumers = f"{len(list(cps_graph.out_edges(interrupted_cps_name, data=True)))},"


        write_time_and_data_lost_to_file(cps_name, injection_time, cps_internal_timer, cps_data_lost, cps_time_lost, number_of_cps_consumers)


        log_consumer_data_and_time_lost_to_file(negotiating_delay, interrupted_cps_name, time_of_injection, interrupted_cps_data_rate)


def get_number_of_fault_injections() -> int:

    no_injections:int = int(input(f"Enter the number of fault injections to be done: "))

    print(" ")

    return no_injections

def get_negotiating_delay() -> int:

    negotiating_delay:int = int(input(f"Enter the negotiating delay: "))

    return negotiating_delay



def main():

     get_cps_data()

     add_edges_to_node()

     print(" ")

     no_injections:int = get_number_of_fault_injections()

     print(" ")

     negotiating_delay:int = get_negotiating_delay()

     inject_fault(no_injections, negotiating_delay)


     generate_and_draw_graph()



if __name__ == "__main__":
    main()




