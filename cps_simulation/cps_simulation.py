# Standard Library imports
import sys
import random
import statistics

# Third-party library imports
import simpy

# Local app imports
from broadcast_pipe import BroadcastPipe


RANDOM_SEED = 42
SIM_TIME = 200

time_lost: list = []
data_lost: list = []


def message_generator(name, env, out_pipe):
    """A process which randomly generates messages."""
    while True:
        # wait for next transmission
        yield env.timeout(random.randint(6, 10))

        # messages are time stamped to later check if the consumer was
        # late getting them.  Note, using event.triggered to do this may
        # result in failure due to FIFO nature of simulation yields.
        # (i.e. if at the same env.now, message_generator puts a message
        # in the pipe first and then message_consumer gets from pipe,
        # the event.triggered will be True in the other order it will be
        # False
        msg = (env.now, '%s says hello at %d' % (name, env.now))
        out_pipe.put(msg)


def message_consumer(name, env, in_pipe):
    """A process which consumes messages."""
    while True:
        # Get event for message pipe
        msg = yield in_pipe.get()

        if msg[0] < env.now:
            # if message was already put into pipe, then
            # message_consumer was late getting to it. Depending on what
            # is being modeled this, may, or may not have some
            # significance
            print('LATE Getting Message: at time %d: %s received message: %s' %
                  (env.now, name, msg[1]))

            time_lost.append(env.now - msg[0])
            data_lost.append(sys.getsizeof(msg[1]))

        else:
            # message_consumer is synchronized with message_generator
            print('at time %d: %s received message: %s.' %
                  (env.now, name, msg[1]))

        # Process does some other work, which may result in missing messages
        yield env.timeout(random.randint(4, 8))


def calculate_time_lost(time_lost):
    average_time_lost = statistics.mean(time_lost)

    # Pretty print the results
    minutes, frac_minutes = divmod(average_time_lost, 1)
    seconds = frac_minutes * 60

    return round(minutes), round(seconds)


def calculate_data_lost(data_lost):
    average_data_lost = statistics.mean(data_lost)

    return average_data_lost


def main():
    # Setup and start the simulation
    print('Process communication')
    random.seed(RANDOM_SEED)
    env = simpy.Environment()

    # # For one-to-one or many-to-one type pipes, use Store
    # pipe = simpy.Store(env)
    # env.process(message_generator('Generator A', env, pipe))
    # env.process(message_consumer('Consumer A', env, pipe))

    # print('\nOne-to-one pipe communication\n')
    # env.run(until=SIM_TIME)

    # For one-to many use BroadcastPipe
    # (Note: could also be used for one-to-one,many-to-one or many-to-many)
    env = simpy.Environment()
    bc_pipe = BroadcastPipe(env)

    env.process(message_generator('Generator A', env, bc_pipe))
    env.process(message_consumer('Consumer A', env, bc_pipe.get_output_conn()))
    env.process(message_consumer('Consumer B', env, bc_pipe.get_output_conn()))

    print('\nOne-to-many pipe communication\n')

    env.run(until=SIM_TIME)

    # View results
    mins, secs = calculate_time_lost(time_lost=time_lost)
    size_of_data_loss = calculate_data_lost(data_lost=data_lost)

    print(f"Total time lost is {secs} secs")

    print(f"Total size of data lost is {size_of_data_loss} bytes")

if __name__ == "__main__":
    main()