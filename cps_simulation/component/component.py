# Standard library imports
import random

# Third-party library imports
import simpy


class Broadcaseter(object):
    def __init__(self, name) -> None:
        self.broadcaseter = name
class Component(object):

    def __init__(self, environment, name, consumers,  data_received, braodcaster) -> None:
        self.env = environment
        self.component_name = name
        self.internal_timer = 0
        self.component_consumers = consumers
        self.data_to_send = [2,3,4,5]
        self.data_sender = Broadcaseter(name=name)
        # self.data_received = self.add_data_to_received_data(data_received)
        self.data_received = data_received
        self.send_data_action = self.env.process(self.send_data_to_consumers())
        self.display_data_action = self.env.process(self.display_data_from_consumers())


    def add_data_to_received_data(self, data_recieved):
        self.data_received.append(data_recieved)

    def send_data_to_consumers(self):

        for cousumer in self.component_consumers:
            print(f"{self.env.now} {self.component_name}: Sending data to {cousumer.name}")
            cousumer.data_received = self.data_to_send[1]
            print(f"{self.env.now} {self.component_name}: Sent data to {cousumer.name}")
            yield self.env.timeout(2)



    def display_data_from_consumers(self):
        duration = 5

        print(f"{self.env.now} {self.component_name}: Received {self.data_received} from {self.data_sender.broadcaseter}")

        try:
            yield self.env.process(self.env.timeout(duration))

        except simpy.Interrupt:
            print(f"{self.component_name}: Was interrupted {self.env.now}!!!")

        print(f"{self.component_name}: Continuing data reading at {self.env.now}")
        yield self.env.timeout(2)