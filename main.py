from abc import ABC, abstractmethod
from typing import List
from enum import Enum
import uuid

class City(Enum):
    City_A = ( "City A", 200, 8, 100)    
    City_B = ( "City B", 300, 6, 150)
    City_C = ( "City C", 250, 9, 120)
    City_D = ( "City D", 350, 7, 200)
    City_E = ( "City E", 400, 5, 250)    
    
class Destination:
    '''Represents a destination with its attributes.''' 
    def __init__(self, name: str, distance: int, scenic_rating: int, cost: int):
        self.id = uuid.uuid4()
        self.name = name 
        self.distance = distance 
        self.scenic_rating = scenic_rating
        self.cost = cost

    def __repr__(self):
        return(f"ID: {self.id}, Name: {self.name}, Distance: {self.distance}, Scenic Rating: {self.scenic_rating}, Cost: {self.cost})")

class PlanningStrategy(ABC):
    '''Abstract base class for planning strategies.'''
    @abstractmethod 
    def plan_itinerary(self, destinations: List[Destination]) -> List[Destination]:
        pass

class ShortestPathStrategy(PlanningStrategy):
    '''A planning strategy that plans the shortest path itinerary.'''
    def plan_itinerary(self, destinations: List[Destination]) -> List[Destination]:
        return sorted(destinations, key= lambda x: x.distance)
    
class MostScenicRouteStrategy(PlanningStrategy):
    '''A planning strategy that plans the most scenic route itinerary.'''
    def plan_itinerary(self, destinations: List[Destination]) -> List[Destination]:
        return sorted(destinations, key= lambda x: x.scenic_rating, reverse=True)

class LeastExpensiveRouteStrategy(PlanningStrategy):
    '''A planning strategy that plans the least expensive route itinerary.'''
    def plan_itinerary(self, destinations: List[Destination]) -> List[Destination]:
        return sorted(destinations, key= lambda x: x.cost)
    
class TravelPlanner:
    '''A travel planner that uses different planning strategies to generate itineraries.'''
    def __init__(self, strategy: PlanningStrategy):
        self.strategy = strategy
        self.destinations = []

    def add_destination(self, destination: Destination):
        '''Adds a destination to the list of destinations.'''
        self.destinations.append(destination)
    
    def set_strategy(self, strategy: PlanningStrategy):
        '''Sets the planning strategy for the travel planner.'''
        self.strategy = strategy

    def generate_itinerary(self):
        '''Generates the itinerary based on the set planning strategy and destinations.'''
        if not self.destinations:
            print("No destinations added")
            return []
        return self.strategy.plan_itinerary(self.destinations)
    
#Usage:
if __name__ == "__main__":
    planner = TravelPlanner(ShortestPathStrategy())
    planner.add_destination(Destination(*City.City_A.value))
    planner.add_destination(Destination(*City.City_B.value))
    planner.add_destination(Destination(*City.City_C.value))
    planner.add_destination(Destination(*City.City_D.value))
    planner.add_destination(Destination(*City.City_E.value))
    print("Shortest Path Itinerary: ")
    for destination in planner.generate_itinerary():
        print(destination)

    planner.set_strategy(MostScenicRouteStrategy())
    print("\nMost Scenic Route Itinerary:")
    for destination in planner.generate_itinerary():
        print(destination)

    planner.set_strategy(LeastExpensiveRouteStrategy())
    print("\nLeast Expensive Route Itinerary:")
    for destination in planner.generate_itinerary():
        print(destination)