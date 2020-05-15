from dimension import Dimension
dim_1 = Dimension()

class Machine():

    def __init__(self):
        self.__dimension = 0

    def SetMachineType(self,type:str)->bool:

            if type == 'M1':
                dim_1 = Dimension()
                dim_1.SetDimension(120,40,90,100)
                self.__dimension = dim_1

            if type == 'M2':
                dim_2 = Dimension()
                dim_2.SetDimension(90,30,80,140)
                self.__dimension = dim_2

            if type == 'M3':
                dim_3 = Dimension()
                dim_3.SetDimension(70,60,110,150)
                self.__dimension = dim_3

def main():
    maquina1 = Machine()
    print(maquina1.__dimension)

    #print(maquina1.__dimension.DimensionToString())
    return

if __name__ == '__main__':
    main()
