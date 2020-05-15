"""Capacited Vehicles Routing Problem (CVRP)."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

vehicles = {}
vehicle_capacities_mass = [300, 240, 560]
vehicle_capacities_vol = [10,10,10]
num_vehicles_jj = 3

demands = {}
demands_mass = [0, 100,100,100,560,100]
demands_vol = [0, 1, 1, 2, 4, 2]
distance_matrix = [
    [
        0, 18.5, 12.5, 10.5, 5.3, 34
    ],
    [
        18.5, 0, 8.4, 10.9, 24.7, 20
    ],
    [
        12.5, 8.4, 0, 4.5, 17.6, 22.2
    ],
    [
        10.5, 10.9, 4.5, 0, 15.2, 24.6
    ],
    [
        5.3, 24.7, 17.6, 15.2, 0, 34.4
    ],
    [   34, 20, 22.2, 24.6, 34.4, 0

    ],
]



def create_data_model(vehicle_capacities_mass,vehicle_capacities_vol,
        num_vehicles_jj, demands_mass, demands_vol, distance_matrix):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = distance_matrix

    data['demands_m'] = demands_mass
    data['demands_l'] = demands_vol
    data['vehicle_capacities_m'] = vehicle_capacities_mass
    data['vehicle_capacities_l'] = vehicle_capacities_vol
    data['num_vehicles'] = num_vehicles_jj
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    total_load_m = 0
    total_load_l = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load_l = 0
        route_load_m = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load_l += data['demands_l'][node_index]
            route_load_m += data['demands_m'][node_index]
            plan_output += ' {0} Load({1}) -> '.format(node_index, route_load_m)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
                                                 route_load_m)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Load of the route: {}\n'.format(route_load_m)
        print(plan_output)
        total_distance += route_distance
        total_load_m += route_load_m
    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load_m))


def main(demands_mass, demands_vol, distance_matrix):
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model(vehicle_capacities_mass,vehicle_capacities_vol,
            num_vehicles_jj, demands_mass, demands_vol, distance_matrix)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Capacity constraint.
    def demand_callback_m(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands_m'][from_node]

    def demand_callback_l(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands_l'][from_node]

    demand_callback_index_m = routing.RegisterUnaryTransitCallback(
        demand_callback_m)


    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index_m,
        0,  # null capacity slack
        data['vehicle_capacities_m'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    demand_callback_index_l = routing.RegisterUnaryTransitCallback(
        demand_callback_l)

    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index_l,
        0,  # null capacity slack
        data['vehicle_capacities_l'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)

    else:
        demands_mass1 = demands_mass[:-1]
        demands_vol1 = demands_vol[:-1]
        distance_matrix1 = distance_matrix[:-1]
        demands_mass2 = demands_mass[-1]
        demands_vol2 = demands_vol[-1]
        distance_matrix2 = distance_matrix [-1]
        main(demands_mass1, demands_vol1, distance_matrix1)
        main(demands_mass2, demands_vol2, distance_matrix2)


if __name__ == '__main__':
    main(demands_mass, demands_vol, distance_matrix)
