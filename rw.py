from __future__ import print_function
from vehiculo import Vehicle
from dimension import Dimension
from model import Model
from product import Product
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


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
    list_large = []
    list_weight = []
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

4
def main():

    # Definición de los vehículos con sus capacidades

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

    data = create_data_model(list_of_vehicles, list_of_products)

    print(data['num_vehicles'])
    print(data['depot'])
    print(data['vehicle_capacities_large'])
    print(data['vehicle_capacities_weight'])
    print(data['demand_large'])
    print(data['demand_weight'])

    return


if __name__ == '__main__':
    main()