from dimension import Dimension
from product import Product

class Cargo():
    def __init__(self):
        self.__components = [] #of products, empty on construction
        self.__cargo_dimension = Dimension()

    def __ValidateComponents(comp:list)->bool:
        return True

    def __ValidateCargoDimension(dim:Dimension)->bool:
        return True

    def SetCargo(self, comp:list, dim:Dimension)->bool:
        condition = False
        if (Cargo.__ValidateComponents(comp) and
        Cargo.__ValidateCargoDimension(dim)):
            condition = True
            self.__components = comp
            self.__cargo_dimension = dim
        return condition


    def CargoToString(self):

        return
