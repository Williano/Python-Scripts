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

def read_input_file():
    with open("input_CPS.txt", "r") as input_file:
        lines = []
        for line in input_file:
            lines.append(line)
            #lines.append(line.strip())

        number_of_cps = len(lines[0].replace(" ", "").strip())

        for i in range(number_of_cps):
                rate = lines[-2].strip().split(" ")[i]
                cps_graph.add_node(i, internal_timer=rate)

        for j in range(number_of_cps):
            for i, value in enumerate(lines[j].strip().split(" ")):
                if value == "1":
                    value1 = lines[j+number_of_cps].strip().split(" ")[i]

                    cps_info = (j, i, {"data_rate": value1})
                    #GRAPH_NODES.append(cps_info)
                    cps_graph.add_edge(j, i, data_rate=value1)

    #print(cps_graph.nodes(data=True))



def get_cps_data() -> list:

    print(" ")

    lines = read_input_file()

    num_of_cps = len(lines[0])

    number_of_cps:int = int(input("How many cyber physical systems do you need in the simulation? (eg. 1, 2, ..): "))

    for cps in range(1, number_of_cps + 1):

        print(" ")

        name:str = input(f"Enter the name of cps{cps}: ")

        cps_internal_time = input(f"Enter the interanl timer for {name}(in micro secs): ")

        cps_graph.add_node(name, internal_timer= cps_internal_time)

        get_cps_consumers(name, cps_internal_time)


def get_cps_consumers(cps_name, cps_internal_timer):

    lines = read_input_file()

    number_of_consumers = int(input(f"How many consumer systems does {cps_name} have? (eg. 1, 2, ..): "))

    for cps_consumer in range(1, number_of_consumers +1):
            consumer:str = input(f"Enter the name of {cps_name} consumer {cps_consumer}: ")
            date_rate = input(f"Enter the data rate(kbps): ")

            cps_info = (cps_name, consumer, {"data_rate": date_rate + "kbps",
                        "internal_timer": cps_internal_timer})

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


def write_time_and_data_lost_to_file(interrupt_message, internal_timer, time_message, data_lost_message):

    with open("time_and_data_loss.text", "a") as lost_file:
        lost_file.write(interrupt_message)
        lost_file.write(internal_timer)
        lost_file.write(time_message)
        lost_file.write(data_lost_message)

def append_stars_to_file():
    with open("time_and_data_loss.text", "a") as lost_file:
        lost_file.write("**********************************************")


def log_consumer_data_and_time_lost_to_file(interrupted_cps_name, time_of_injection, interrupted_cps_data_rate):

        consumers_of_interrupted_cps = list(cps_graph.out_edges(interrupted_cps_name, data=True))

        for consumer in range(0, len(consumers_of_interrupted_cps)):

            consumer_name = consumers_of_interrupted_cps[consumer][1]

            consumer_of_interrupted_cps_internal_timer = float(nx.get_node_attributes(cps_graph, 'internal_timer')[consumer_name])

            print(consumer_of_interrupted_cps_internal_timer)

            consumer_time_loss = time_of_injection % consumer_of_interrupted_cps_internal_timer
            consumer_data_loss = int(consumer_time_loss * interrupted_cps_data_rate) / 1000000


            consumer_internal_timer = f"Consumer {consumer_name} checkpoint delay: {consumer_of_interrupted_cps_internal_timer}us" + "\n"
            consumer_data_lost = f"Consumer {consumer_name} -> DATA LOST: {consumer_data_loss}kb" + "\n"
            consumer_time_lost = f"Consumer {consumer_name} -> TIME LOST: {consumer_time_loss}us" + "\n"
            write_time_and_data_lost_to_file("" ,consumer_internal_timer, consumer_data_lost, consumer_time_lost)

            append_stars_to_file()





def inject_fault(no_injections):

    open("time_and_data_loss.text", "w").close()

    for n in range(1, no_injections + 1):
        cps_list = []
        time_of_injection = datetime.now().microsecond

        sleep(random.uniform(0.5, 1.5))
        interrupted_cps = secrets.choice(list(cps_graph.nodes))
        interrupted_cps = 0
        print(interrupted_cps)
        # cps1 = interrupted_cps[0]
        # cps_list.append(cps1)
        # cps2 = interrupted_cps[1]
        # cps_list.append(cps2)
        interrupted_cps_name = interrupted_cps

        #print(list(cps_graph.out_edges(interrupted_cps))[0][1])
        #interrupted_cps_internal_timer = float(interrupted_cps["internal_timer"])
        data_rate = nx.get_edge_attributes(cps_graph,'data_rate')
        print(data_rate)
        temp:int = 0
        for i in range(len(list(cps_graph.out_edges(interrupted_cps)))):
            print(list(cps_graph.out_edges(interrupted_cps))[i])
            temp += int(data_rate(list(cps_graph.out_edges(interrupted_cps))[i][1]))

        print(temp)
        #interrupted_cps_data_rate = cps_graph.out_edges(interrupted_cps)[0][1]



        cps_time_loss = time_of_injection % interrupted_cps_internal_timer
        cps_data_loss = int(cps_time_loss * interrupted_cps_data_rate) / 1000000

        time_of_interrupt = f"The {n}th injection was on the CPS: {interrupted_cps_name} at the time {time_of_injection}s" + "\n"
        cps_internal_timer = f"CPS {interrupted_cps_name} checkpoint delay: {interrupted_cps_internal_timer}us" + "\n"
        cps_data_lost = f"CPS {interrupted_cps_name} -> DATA LOST: {cps_data_loss}kb" + "\n"
        cps_time_lost = f"CPS {interrupted_cps_name} -> TIME LOST: {cps_time_loss}us" + "\n"

        write_time_and_data_lost_to_file(time_of_interrupt, cps_data_lost, cps_time_lost)

        log_consumer_data_and_time_lost_to_file(interrupted_cps_name, time_of_injection, interrupted_cps_data_rate)


def get_number_of_fault_injections() -> int:

    no_injections:int = int(input(f"Enter the number of fault injections to be done:"))

    print(" ")

    return no_injections


def main():


    read_input_file()

    # get_cps_data()

    #add_edges_to_node()


    no_injections:int = get_number_of_fault_injections()

    inject_fault(no_injections)


    generate_and_draw_graph()



if __name__ == "__main__":
    main()




