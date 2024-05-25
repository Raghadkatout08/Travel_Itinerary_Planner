# Travel_Itinerary_Planner

## Overview 
    This system generates travel itineraries based on different planning strategies, such as finding the shortest path, the most scenic route, or the least expensive route.

## Components
- **PlanningStrategy Interface:** Defines an interface for different planning strategies.

- **Concrete Planning Strategies:** Implement different planning methods such as Shortest Path, Most Scenic Route, and Least Expensive Route.

- **TravelItineraryPlanner Class:** Generates travel itineraries based on the selected planning strategy.

## Installation
To use this project, you need Python 3 installed on your system. It's recommended to use a virtual environment to manage dependencies. Here's how you can set up the project:

1. `git clone git@github.com:Raghadkatout08/Travel_Itinerary_Planner.git`.

2. Navigate to the project directory: `cd Travel_Itinerary_Planner`.

3. Create a virtual environment (optional but recommended): `python3 -m venv .venv`.

4. Activate the virtual environment:
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```
5. Install the project dependencies: `pip install -r requirements.txt`

## Usage 
1. After setting up the project, you can run the main script to see sample itineraries: `python3 main.py`

## Testing
This project includes unit tests to ensure the correctness of the implemented strategies. To run the tests, you need to install pytest. Here's how you can do it:
1. Install pytest: `pip install pytest`

2. Run the tests: `pytest` OR `python -m pytest`