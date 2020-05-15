from dimension import Dimension

class Model():
    def __init__(self):
        self.__name = "Unknown" #Model name, please read doc
        self.__type = "Unknown"
        self.__oil_capacity = 0
        self.__oil_consume = 0
        self.__entire_dimension = Dimension()
        self.__trunk_dimension = Dimension() #In here dim refer to capacity

#################### Model Validations

    def __ValidateName(name):
        return True

    def __ValidateType(type):
        return True

    def __ValidateOilCapacity(oil):
        return True

    def __ValidateOilConsume(oil):
        return True

    def __ValidateEntireDimension(dim):
        return True

    def __ValidateTrunkDimension(dim):
        return True


#################### Model instances creating and edit



    def SetModel(self, name:str, type:str, oil_capacity:float,
    oil_consume:float, entire_dimension:Dimension,
    trunk_dimension:Dimension)->bool:
        """
        This is the intended method to setup an instance of the class rather than
        the only one-long variables ones that are designed for exception handling.
        """

        made = False
        if (Model.__ValidateName(name) and
        Model.__ValidateType(type) and
        Model.__ValidateOilCapacity(oil_capacity) and
        Model.__ValidateOilConsume(oil_consume) and
        Model.__ValidateEntireDimension(entire_dimension) and
        Model.__ValidateTrunkDimension(trunk_dimension)):

            made = True
            self.__name = name
            self.__type = type
            self.__oil_capacity = oil_capacity
            self.__oil_consume = oil_consume
            self.__entire_dimension = entire_dimension
            self.__trunk_dimension = trunk_dimension

        return made


    def SetName(self, name:str)->bool:
        """
        This function is for manually changing only vehicle's name.
        If change couldn't be made won't raise error, will return
        False instead.
        """
        made = False
        if Model.__ValidateName(name):
            made = True
            self.__name = name
        return made


    def SetType(self, type:str)->bool:
        """
        This function is for manually changing only vehicle's type.
        If change couldn't be made won't raise error, will return
        False instead.

        """
        made = False
        if Model.__ValidateType(type):
            made = True
            self.__type = type
        return made


    def SetOilCapacity(self, oil:int)->bool:
        """
        This function is for manually changing only vehicle's oil capacity.
        If change couldn't be made won't raise error, will return
        False instead.
        """
        made = False
        if Model.__ValidateOilCapacity(oil):
            made = True
            self.__oil_capacity = oil
        return made


    def SetOilConsume(self, oil:int)->bool:
        """
        This function is for manually changing only vehicle's oil consume.
        If change couldn't be made won't raise error, will return
        False instead.
        """
        made = False
        if Model.__ValidateOilConsume(oil):
            made = True
            self.__oil_consume = oil
        return made

    def SetEntireDimension(self,dim)->bool: #dim:Dimension()
        """
        This function is for manually changing only vehicle's dimensions.
        This only accept Dimension() object as argument, however it won't
        raise error in other case, it will return False f change couldn't
        be done.
        """
        made = False
        if Model.__ValidateEntireDimension(dim):
            made = True
            self.__dimension = dimension
        return made

    def SetTrunkDimension(self,dim)->bool: #dim:Dimension()
        """
        This function is for manually changing only vehicle's dimensions.
        This only accept Dimension() object as argument, however it won't
        raise error in other case, it will return False f change couldn't
        be done.
        """
        made = False
        if Model.__ValidateTrunkDimension(dim):
            made = True
            self.__dimension = dimension
        return made



###GET###
    def GetName(self)->str:
        return self.__name

    def GetType(self)->str:
        return self.__type

    def GetOilCapacity(self)->float:
        return self.__oil_capacity

    def GetOilConsume(self)->float:
        return self.__oil_consume

    def GetEntireDimension(self)->Dimension:
        return self.__entire_dimension

    def GetTrunkDimension(self)->Dimension:
        return self.__entire_dimension

    def ModelToString(self)->str:
        string = 'Modelo: '
        string += self.__name
        string += '\nVehículo tipo: '
        string += self.__type
        string += '\nTanque con capacidad de: '
        string += str(self.__oil_capacity)
        string += 'L\nConsumo: '
        string += str(self.__oil_consume)
        string += 'L/100km\nDimensiones del vehículo:\n'
        string += self.__entire_dimension.DimensionToString()
        string += '\nDimensiones de carga útil:\n'
        string += self.__trunk_dimension.DimensionToString()

        return string


def main():

    dim_prod1 = Dimension()
    dim_prod2 = Dimension()
    dim_prod3 = Dimension()
    dim_prod1.SetDimension(4,123,1.3,2.6)
    dim_prod2.SetDimension(1.3,200,1.7,3.4)
    dim_prod3.SetDimension(2.7,222,2.3,5.6)

    first = Model()
    second = Model()
    third = Model()
    a = first.SetModel('BMW serie 5','ranchera',48,10, dim_prod1,dim_prod1)
    b = second.SetModel('Mercedes año catapún','deportivo',79,17, dim_prod2,dim_prod2)
    c = third.SetModel('Porche Carrera S','Sdeportivo',120,20, dim_prod3,dim_prod3)
    if a and b and c:
        print('Asignacion Correcta !!!!')

    print(first.ModelToString())
    print(second.ModelToString())
    print(third.ModelToString())


if __name__ == '__main__':
    main()
