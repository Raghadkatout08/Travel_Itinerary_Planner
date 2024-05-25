from main import TravelPlanner, ShortestPathStrategy, MostScenicRouteStrategy, LeastExpensiveRouteStrategy, Destination, City

def test_shortest_path_strategy():
    '''Test For The Shortest Path Strategy.'''
    planner = TravelPlanner(ShortestPathStrategy())
    planner.add_destination(Destination(*City.City_A.value))
    planner.add_destination(Destination(*City.City_B.value))
    planner.add_destination(Destination(*City.City_C.value))
    planner.add_destination(Destination(*City.City_D.value))
    planner.add_destination(Destination(*City.City_E.value))
    
    itinerary = planner.generate_itinerary()
    expected = ['City A', 'City C', 'City B', 'City D', 'City E']
    actual = [destination.name for destination in itinerary]
    assert expected == actual

def test_most_scenic_route_strategy():
    '''Test For The Most Scenic Route Strategy.'''
    planner = TravelPlanner(MostScenicRouteStrategy())
    planner.add_destination(Destination(*City.City_A.value))
    planner.add_destination(Destination(*City.City_B.value))
    planner.add_destination(Destination(*City.City_C.value))
    planner.add_destination(Destination(*City.City_D.value))
    planner.add_destination(Destination(*City.City_E.value))

    itinerary = planner.generate_itinerary()
    expected = ['City C', 'City A', 'City D', 'City B', 'City E']
    actual = [destination.name for destination in itinerary]
    assert expected == actual


def test_least_expensive_route_strategy():
    '''Test For The Least Expensive Route Strategy.'''
    planner = TravelPlanner(LeastExpensiveRouteStrategy())
    planner.add_destination(Destination(*City.City_A.value))
    planner.add_destination(Destination(*City.City_B.value))
    planner.add_destination(Destination(*City.City_C.value))
    planner.add_destination(Destination(*City.City_D.value))
    planner.add_destination(Destination(*City.City_E.value))

    itinerary = planner.generate_itinerary()
    expected = ['City A', 'City C', 'City B', 'City D', 'City E']
    actual = [destination.name for destination in itinerary]
    assert expected == actual