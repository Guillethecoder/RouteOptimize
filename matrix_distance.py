from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] =[]
    data['num_vehicles'] = 1
    data['depot'] = 0
    data['demands'] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    data['vehicle_capacities'] = [15, 15, 15, 15]
    return data

manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                       data['num_vehicles'], data['depot'])
routing = pywrapcp.RoutingModel(manager)


def distance_callback(from_index, to_index):
    """Returns the distance between the two nodes."""
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data['distance_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)


"""
The arc cost evaluator tells the solver how to calculate the cost of travel
between any two locations—in other words, the cost of the edge (or arc) joining
them in the graph for the problem. The following code sets the arc cost evaluator.
"""

routing.SetArcCostEvaluatorOfAllVehicles(oil_consume*transit_callback_index)

"""
This means that the cost of travel between any two locations is just the
distance between them. However, in general the costs can involve other
factors as well.
"""

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

"""
The code sets the first solution strategy to PATH_CHEAPEST_ARC,
which creates an initial route for the solver by repeatedly adding edges
with the least weight that don't lead to a previously
visited node (other than the depot). For other options,
see First solution strategy.
"""


def print_solution(manager, routing, solution):
  """Prints solution on console."""
  print('Objective: {} miles'.format(solution.ObjectiveValue()))
  index = routing.Start(0)
  plan_output = 'Route for vehicle 0:\n'
  route_distance = 0
  while not routing.IsEnd(index):
    plan_output += ' {} ->'.format(manager.IndexToNode(index))
    previous_index = index
    index = solution.Value(routing.NextVar(index))
    route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
  plan_output += ' {}\n'.format(manager.IndexToNode(index))
  print(plan_output)
  plan_output += 'Route distance: {}miles\n'.format(route_distance)

#The function displays the optimal route and its distance, which is given by ObjectiveValue().


solution = routing.SolveWithParameters(search_parameters)
    if solution:
      print_solution(manager, routing, solution)


def get_routes(solution, routing, manager):
  """Get vehicle routes from a solution and store them in an array."""
  # Get vehicle routes and store them in a two dimensional array whose
  # i,j entry is the jth location visited by vehicle i along its route.
  routes = []
  for route_nbr in range(routing.vehicles()):
    index = routing.Start(route_nbr)
    route = [manager.IndexToNode(index)]
    while not routing.IsEnd(index):
      index = solution.Value(routing.NextVar(index))
      route.append(manager.IndexToNode(index))
    routes.append(route)
  return routes



dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)


def demand_callback(from_index):
    """Returns the demand of the node."""
    # Convert from routing variable Index to demands NodeIndex.
    from_node = manager.IndexToNode(from_index)
    return data['demands'][from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(
    demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    data['vehicle_capacities'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity')

#AddDimensionWithVehicleCapacity for volume

"""
In more complex CVRPs, each vehicle might carry several different types of cargo,
with a maximum capacity for each type. For example,
a fuel delivery truck might carry several types of fuel,
using multiple tanks with differing capacities. To handle problems like these,
just create a different capacity callback and dimension for each
cargo type (making sure to assign them unique names).
"""
