"""
Implementing a simulation just using coroutines. This simulation will show
how to implement concurrent activities using coroutines instead of threads -
this will help us better understand the asyncio library. Remember that this
concurrent activities will be running in a single-thread program!
"""

from typing import NoReturn, Generator
from random import randint
from enum import Enum
import sys

class TaxiFinishedService(Exception):
    """ Finishing Taxi Service """

class State(Enum):
    LEAVE_GARAGE = 0
    EMPTY = 1
    FULL = 2

class Taxi:
    def __init__(self, id: int, num_travels_to_perform: int) -> None:
        self.id = id
        self.num_travels_to_perform = num_travels_to_perform
        self.state = State.LEAVE_GARAGE

    def simulate(self) -> Generator[State, None, None]:
        #self._log("Leaving garage")
        yield self.state
        while True:
            #self._log("Picking up passanger")
            yield self._pickup_passenger()
            #self._log("Dropping off passanger")
            yield self._drop_passanger()

        return self.num_travels_to_perform != 0

    def _pickup_passenger(self) -> State: 
        self.state = State.FULL
        return self.state

    def _drop_passanger(self) -> State:
        self.state = State.EMPTY
        self.num_travels_to_perform -= 1

        if self.num_travels_to_perform == 0:
            self._finish_service()

        return self.state
    
    def _finish_service(self) -> NoReturn:
        self._log("Finishing service")
        raise TaxiFinishedService()

    def _log(self, msg: str) -> None:
        print(" " * self.id * 3, f"Taxi with id {self.id}: ", msg)
        

class TaxiSimulation:
    def __init__(self, num_taxis: int) -> None:
        self.taxis = []
        print(f"Creating {num_taxis} taxis")
        for i in range(num_taxis):
            taxi = Taxi(i, randint(1, 10))
            self.taxis.append((taxi, taxi.simulate()))

    def run(self) -> None:
        time = 0
        print("Starting simulation")
        while self.taxis:
            try:
                next_taxi_idx = randint(0, len(self.taxis) - 1)
                time = 1 + time + next_taxi_idx
                taxi, taxi_sim = self.taxis[next_taxi_idx]
                taxi_state = next(taxi_sim)
                print(" " * taxi.id * 3, f"taxi: {taxi.id}, Event(time={time}, remaining_pickups={taxi.num_travels_to_perform}, state='{taxi_state}')")
            except TaxiFinishedService as e:
                self.taxis.remove(self.taxis[next_taxi_idx])
                num_taxis_left = len(self.taxis)
                if num_taxis_left > 0:
                    print(f"Still {num_taxis_left} in the simulation")
                else:
                    print("Finishing simulation")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError(f"Expecting only the number of taxis to simulate, received: {sys.argv}")
    sim = TaxiSimulation(int(sys.argv[1]))
    sim.run()
