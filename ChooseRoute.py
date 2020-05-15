from __future__ import print_function
from vehiculo import Vehicle
from dimension import Dimension
from model import Model
from product import Product
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

dim_prod1 = Dimension()
dim_prod2 = Dimension()
dim_prod3 = Dimension()
dim_prod1.SetDimension(400,400,130,300)
dim_prod2.SetDimension(170,200,160,240)
dim_prod3.SetDimension(300,200,230,560)

model1 = Model()
model2 = Model()
model3 = Model()
model1.SetModel('Camión1','ranchera',48,10, dim_prod1,dim_prod1)
model2.SetModel('Camión2','deportivo',79,17, dim_prod2,dim_prod2)
model3.SetModel('Camión3','Sdeportivo',120,20, dim_prod3,dim_prod3)


first = Vehicle()
second = Vehicle()
third = Vehicle()
first.SetVehicle(model1,170000,'FBB19284','Coche_Camacho',2,'Camacho','Camacho')
second.SetVehicle(model2,999999999,'VC 7878 A','Coche_mortadelo',0.2,'Jose Vicente','Jose Vicente')
third.SetVehicle(model3,10000,'JHV1674','Coche_Guille',19,'Guillermo','Guillermo')

dim_prod1 = Dimension()
dim_prod2 = Dimension()
dim_prod3 = Dimension()
dim_prod1.SetDimension(100,100,40,100)
dim_prod2.SetDimension(120,100,130,100)
dim_prod3.SetDimension(150,200,230,560)

prod1 = Product()
prod2 = Product()
prod3 = Product()
prod4 = Product()
prod5 = Product()

prod1.SetProduct('asdafg',dim_prod1)
prod2.SetProduct('fghsdoiuf',dim_prod1)
prod3.SetProduct('asdregjmerjafg',dim_prod2)
prod4.SetProduct('asfadhrtgdafg',dim_prod3)
prod5.SetProduct('asafhdrgthdafg',dim_prod2)


list_of_vehicles = [first,second,third]
list_of_products = [prod1,prod2,prod3,prod4,prod5]

def create_data_model(list_of_vehicles, list_of_products):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] =[
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
            5.3, 24.7, 17.6, 15.2,0, 34.4
        ],
        [   34, 20, 22.2, 24.6, 34.4, 0

        ],
    ]#map matrix
    #list_of_vheight = []
    #list_of_vwidth = []
    list_of_vlarge = []
    list_of_vweight = []
    for element in list_of_vehicles:
        #list_of_vheight.append(element..__trunk_dimension.__height)
        #list_of_vhwidht.append(element.__model.__trunk_dimension.__width)
        list_of_vlarge.append(element.GetModel().GetTrunkDimension().GetLarge())
        list_of_vweight.append(element.GetModel().GetTrunkDimension().GetWeight())

    #list_height = []
    #list_width = []
    list_large = [0]
    list_weight = [0]
    for element in list_of_products:
        #list_height.append(element.__product_dimension.__height)
        #list_width.append(element.__product_dimension.__width)
        list_large.append(element.GetProductDimension().GetLarge())
        list_weight.append(element.GetProductDimension().GetWeight())


    data['num_vehicles'] = len(list_of_vehicles) #number of vehicles
    data['depot'] = 0
    #data['vehicle_capacities_height'] = list_of_vheight
    #data['vehicle_capacities_width'] = list_of_vwidth
    data['vehicle_capacities_large'] = list_of_vlarge
    data['vehicle_capacities_weight'] = list_of_vweight
    #data['demand_height'] = list_height
    #data['demand_width'] = list_width
    data['demand_large'] = list_large
    data['demand_weight'] = list_weight
    return data


data = create_data_model(list_of_vehicles,list_of_products)
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

routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

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



""" dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name) """
#distance_dimension = routing.GetDimensionOrDie(dimension_name)
#distance_dimension.SetGlobalSpanCostCoefficient(100)

""" 
def demand_callback_height(from_index):
    #Returns the demand of the node by height of the product.
    # Convert from routing variable Index to demands NodeIndex.
    from_node = manager.IndexToNode(from_index)
    return data['demand_height'][from_node]

def demand_callback_width(from_index):
    #Returns the demand of the node by width of the product.
    # Convert from routing variable Index to demands NodeIndex.
    from_node = manager.IndexToNode(from_index)
    return data['demand_width'][from_node] """

def demand_callback_large(from_index):
    """Returns the demand of the node by lenght of the product."""
    # Convert from routing variable Index to demands NodeIndex.
    from_node = manager.IndexToNode(from_index)
    return data['demand_large'][from_node]

def demand_callback_weight(from_index):
    """Returns the demand of the node by height of the product."""
    # Convert from routing variable Index to demands NodeIndex.
    from_node = manager.IndexToNode(from_index)
    return data['demand_weight'][from_node]

""" demand_callback_index_height = routing.RegisterUnaryTransitCallback(
    demand_callback_height)

demand_callback_index_width = routing.RegisterUnaryTransitCallback(
    demand_callback_width)
 """
demand_callback_index_large = routing.RegisterUnaryTransitCallback(
    demand_callback_large)

demand_callback_index_weight = routing.RegisterUnaryTransitCallback(
    demand_callback_weight)

""" routing.AddDimensionWithVehicleCapacity(
    demand_callback_index_height,
    0,  # null capacity slack
    data['vehicle_capacities_height'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Height')

demand_callback_index = routing.RegisterUnaryTransitCallback(
    demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index_width,
    0,  # null capacity slack
    data['vehicle_capacities_width'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Width') """

demand_callback_index_large = routing.RegisterUnaryTransitCallback(
    demand_callback_large)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index_large,
    0,  # null capacity slack
    data['vehicle_capacities_large'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Large')

demand_callback_index_weight = routing.RegisterUnaryTransitCallback(
    demand_callback_weight)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index_weight,
    0,  # null capacity slack
    data['vehicle_capacities_weight'],  # vehicle maximum capacities
    True,  # start cumul to zero
    'Weight')




#AddDimensionWithVehicleCapacity for volume

"""
In more complex CVRPs, each vehicle might carry several different types of cargo,
with a maximum capacity for each type. For example,
a fuel delivery truck might carry several types of fuel,
using multiple tanks with differing capacities. To handle problems like these,
just create a different capacity callback and dimension for each
cargo type (making sure to assign them unique names).
"""
