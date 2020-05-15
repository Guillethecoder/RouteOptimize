from model import Model

from dimension import Dimension

##############################################################################
##############################VEHICLE CLASS###################################
##############################################################################
class Vehicle():
    """
    This class is for more accurate description of a concrete vehicle.
    It has all the information that vehicles of the same model share
    as well as information that's unique for the vehicle tha belongs to.
    """

    #We call Model initation:
    def __init__(self):
        self.__model = Model()
        self.__km = 0 #The Km the vehicle has done so far
        self.__registration = "Unknown" #matrícula
        self.__company_registration = "Unknown" #Company
        #registration for vehicle
        self.__oil_actual = 0 #Oil that the
        #vehicle has charged right now
        #self.__cargo_actual = None #Cargo the
        #vehicle has right now
        self.__driver = "Unknown" #Driver asigned
        #to the vehicle drive
        self.__responsable = "Unknown" #Person who must
        #take care of the vehicle


############# VALIDACIONES ATRIBUTOS:

    def __ValidateKm(km:str)->bool:
        return True

    def __ValidateRegistration(regis:str)->bool:
        return True

    def __ValidateCompanyRegistration(cr:str)->bool:
        return True

    def __ValidateOilActual(oil:int)->bool:
        return True

    #def __ValidateCargo_Actual(cargo:None())->bool:
    #    return True

    def __ValidateDriver(driver:str)->bool:
        return True

    def __ValidateResponsable(resp:str)->bool:
        return True


############# MÉTODOS VEHÍCULO:

####SET####

    def SetVehicle(self, model:Model, km:float, regis:str,
    cr:str, oil_actual:float, driver:str, resp:str)->bool:

        cond = False
        if(Vehicle.__ValidateKm(km) and
        Vehicle.__ValidateRegistration(regis) and
        Vehicle.__ValidateCompanyRegistration(cr) and
        Vehicle.__ValidateOilActual(oil_actual) and
        Vehicle.__ValidateDriver(driver) and
        Vehicle.__ValidateResponsable(resp)):

            cond = True
            self.__model = model
            self.__km = km
            self.__registration = regis
            self.__company_registration = cr
            self.__oil_actual = oil_actual
            self.__driver = driver
            self.__responsable = resp
        return cond


    def SetKm(self,km:int)->bool:
        conver = False
        if Vehicle.__ValidateKm(km):
            convers = True
            self.__km = km
        return convers

    def SetRegistration(self, regis:str)->bool:
        convers = False
        if Vehicle.__ValidateRegistration(regis):
            convers = True
            self.__registration = regis
        return convers

    def SetCR(self, cr:str)->bool:
        convers = False
        if Vehicle.__ValidateCompanyRegistration(CR):
            convers =True
            self.__company_registration
        return convers

    def SetOilActual(self, oil:int)->bool:
        convers = False
        if Vehicle.__ValidateOilActual(oil):
            convers = True
            self.__oil_actual = oil
        return convers

    #def SetCargoActual(self, cargo:Cargo)->bool:
    #    return

    def SetDriver(self,driver:str)->bool:
        convers = False
        if Vehicle.__ValidarDriver(driver):
            convers = True
            self.__driver = driver
        return convers

    def SetResponsable(self, resp:str)->bool:
        convers = False
        if Vehicle.__ValidateResponsable(resp):
            convers = True
            self.__responsable = resp
        return convers

###GET###

    def GetModel(self)->Model:
        return self.__model

    def GetKm(self)->float:
        return self.__km

    def GetRegistration(self)->str:
        return self.__registration

    def GetCR(self)->str:
        return self.__company_registration

    def GetOilActual(self)->float:
        return self.__oil_actual

    #def GetCargo


    def GetDriver(self)->str:
        return self.__driver

    def GetResonsable(self)->str:
        return self.__responsable

    def VehicleToString(self):
        string = 'Modelo y sus características:\n'
        string += self.GetModel().ModelToString()
        string += '\n Km del vehículo: '
        string += str(self.GetKm())
        string += '\nMatrícula: '
        string += self.GetRegistration()
        string += '\nCodigo de registro: '
        string += self.GetCR()
        string += '\nDepósito: '
        string += str(self.GetOilActual())
        string += 'L\nConductor: '
        string += self.GetDriver()
        string += '\nResponsable del vehículo: '
        string += self.GetResonsable()
        return string


def main():
    """
    self, name:str, type:str, oil_capacity:float,
    oil_consume:float, entire_dimension:Dimension,
    trunk_dimension:Dimension, km:float, registration:str,
    cr:str, oil_actual:float, driver:str, resp:str
    """

    dim_prod1 = Dimension()
    dim_prod2 = Dimension()
    dim_prod3 = Dimension()
    dim_prod1.SetDimension(4,123,1.3,2.6)
    dim_prod2.SetDimension(1.3,200,1.7,3.4)
    dim_prod3.SetDimension(2.7,222,2.3,5.6)

    model1 = Model()
    model2 = Model()
    model3 = Model()
    model1.SetModel('BMW serie 5','ranchera',48,10, dim_prod1,dim_prod1)
    model2.SetModel('Mercedes año catapún','deportivo',79,17, dim_prod2,dim_prod2)
    model3.SetModel('Porche Carrera S','Sdeportivo',120,20, dim_prod3,dim_prod3)


    first = Vehicle()
    second = Vehicle()
    third = Vehicle()
    first.SetVehicle(model1,170000,'FBB19284','Coche_Camacho',2,'Camacho','Camacho')
    second.SetVehicle(model2,999999999,'VC 7878 A','Coche_mortadelo',0.2,'Jose Vicente','Jose Vicente')
    third.SetVehicle(model3,10000,'JHV1674','Coche_Guille',19,'Guillermo','Guillermo')

    print(first.VehicleToString())
    print(second.VehicleToString())
    print(third.VehicleToString())

    return

if __name__ == '__main__':
    main()
