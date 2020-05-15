from dimension import Dimension

class Product():


    def __init__(self):
        self.__code = "Unknown"
        self.__product_dimension = Dimension()

    def __ValidateCode(code:str)->bool:
        return True

    def __ValidateProductDimension(dim:Dimension)->bool:
        return True

    def SetProduct(self,code:str,dim:Dimension)->bool:
        condition = False
        if(Product.__ValidateCode(code) and
        Product.__ValidateProductDimension(dim)):
            condition = True
            self.__code = code
            self.__product_dimension = dim
        return condition

    def SetCode(self, code:str)->bool:
        condition = False
        if Product.__ValidateCode(code):
            condition = True
            self.__code = code
        return condition

    def SetProductDimension(self, dim:Dimension)->bool:
        condition = False
        if Product.__ValidateProductDimension(dim):
            condition = True
            self.__code = dim
        return condition


    def GetCode(self)->bool:
        return self.__code

    def GetProductDimension(self)->bool:
        return self.__product_dimension

    def ProductToString(self)->str:
        string = ''
        string += 'Product Code: '
        string += self.__code
        string += '\nDimensions:\n'
        string += self.__product_dimension.DimensionToString()
        return string


def main():

    dim_prod1 = Dimension()
    dim_prod2 = Dimension()
    dim_prod3 = Dimension()
    dim_prod1.SetDimension(4,123,1.3,2.6)
    dim_prod2.SetDimension(1.3,200,1.7,3.4)
    dim_prod3.SetDimension(2.7,222,2.3,5.6)

    first = Product()
    second = Product()
    third = Product()
    a = first.SetProduct('hola', dim_prod1)
    b = second.SetProduct('aloh', dim_prod2)
    c = third.SetProduct('asios', dim_prod3)

    if a and b and c:
        print('asignacion correcta')

    print(first.ProductToString())
    print(second.ProductToString())
    print(third.ProductToString())


    return


if __name__ == '__main__':
    main()
