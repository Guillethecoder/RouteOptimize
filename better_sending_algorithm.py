from partision_algorithm import PartitioningCargo
from dimension import Dimension
from vehicle import Vehicle


def CargoFitsVehicle(cargo, vehicle):
    max_height = 0
    max_width = 0
    total_large = 0
    for element in cargo:
        if element.__cargo_dimension.__hight > max_height:
            max_height = element.__cargo_dimension.__hight
        if element.__cargo_dimension.__width > max_width:
            max_width = element.__cargo_dimension.__width
        total_large += element.__cargo_dimension.__large
    if (max_height <= vehicle.__trunk_dimension.__hight and
    max_width <= vehicle.__trunk_dimension.__width and
    total_large <= vehicle.__trunk_dimension.__large):
        return True
    else:
        return False


def ChooseOrganisationByFuelCost(organisations:list, vehicles:list)->(list,list):
    """
    This Algorithm takes in a list of possible organisation with
    partisions for cargo
    and a list of vehicles possible to use. It returns a list of
    the still possible to use vehicles and a list of list
    with each element correspond to [final cargo partition number n,
    vehicle asigned to that cargo partition].
    """
    ###First step of the algorithm is to del any possible partition that has
    ###an element wich doesnt fit any vehicle.
    for organisation in organisations:
        delete = True
        for partision in organisation:
            for vehicle in vehicles:
                if CargoFitsVehicle(sub_set,vehicle):
                    delete = False
        if delete:
            partitions.remove(organisation)

    ###Now we have only in partitions the possible ones. The goal now is to
    ###know wick ones take less number of vechicles thats easy:

    min_len = len(organisations[0])
    for organisation in organisations
        if len(organisation) < min_len:
            min_len = len(organisation)

    #This way we now know wich is the number of vehicle that's the minimun to
    #use
    defininitive_possible_organisations = []
        for organisation in organisations:
            if len(organisation) = min_len
                defininitive_possible_organisations.append(organisation)


    #Now we have the list with less vehicles needed partitions, we have now to
    #look in wich way we'll use less oil/fuel:

    vehicles.sort(vehicles, key = lambda x: x.__oil_consume)
    #Now the vehicle list is sorted from less fuel consumming vehicles to more.
    for organisation in defininitive_possible_organisations:
        copy = vehicles
        for sub_set in organisation:
            sub_set_truk_list = []
            for vehicle in copy:
                found = False
                if CargoFitsVehicle(sub_set,vehicle):
                    found = True
                    sub_set_truk_list.append(vehicle)
        organisation.append(sub_set_truk_list)
        #Una observacion importante a hacer es que ahora el ultimo elemento de
        #cada organización es una lista con los vehiculos en orden!!!!!

    #Now we choose the cargo organisation that costs less fuel:
    list_fuel_cost = []
    for organisation in defininitive_possible_organisations:
        fuel_cost = 0
        for vehicle in organisation[-1]:
            fuel_cost += vehicle.__oil_consume
        list_fuel_cost.append(fuel_cost)

    #We finally decide wich is better:

    min_fuel = list_fuel_cost[0]
    index = 0
    for organisation_fuel_cost in list_fuel_cost:
        if organisation_fuel_cost <= min_fuel:
            min_fuel = organisation_fuel_cost
            best_index = index #Índice de la mejor organización
        index += 1

    #With best index we now know wich organisation is best within it's
    #respective trucks
    best_organisation = defininitive_possible_organisations[best_index]

    #Now we delete the chosen vehicles from the possibles to use:

    for vehicle in best_organisation[-1]:
        vehicles.remove(vehicle)

    return vehicles, best_organisation



def main():
    list_of_products = []
    list_of_vehicle = []
    list_of_possible_cargos = PartitioningCargo(list_of_products)
    list_of_vehicle, list_of_final_cargo_with_vehicles =
    ChooseOrganisationByFuelCost(
    list_of_possible_cargos,
    list_of_vehicle)
    return

if __name__ == '__main__':
    main()
