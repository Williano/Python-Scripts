# Standard library imports
import random

# Third-party library imports
import simpy

RANDOM_SEED = 42

class FaultInjector(object):

    def __init__(self, environment, components:list) -> None:
       self.env =  environment
       self.components = components
       self.action = environment.process(self.inject_fault_randomly_into_compoents())


    def inject_fault_randomly_into_compoents(self):
        random.seed(RANDOM_SEED)
        component_1 = self.components(random.randint(1, 4))
        yield self.env.timeout(3)
        component_1.action.interrupt()
        print(f"{self.env.now}: INTERRUPTED {component_1}")
        component_2 = self.components(random.randint(1, 4))
        component_2.action.interrupt()
        print(f"{self.env.now}: INTERRUPTED {component_2}")