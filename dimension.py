

class Dimension():
    def __init__(self):
        self.__height = 0 #Meters
        self.__weigth = 0 #Kilograms
        self.__width = 0 #Meters
        self.__large = 0 #Meters
        self.__volume = 0 #Cubic Meters

############METHODS######################

    ######VALIDATE


    def __ValidateHeight(dist:float)->bool:
        return True

    def __ValidateWeigth(mass:float)->bool:
        return True

    def __ValidateWidth(dist:float)->bool:
        return True

    def __ValidateLarge(dist:float)->bool:
        return True

    """
    Volume does't need any validations as is based uppon height
    widht and large
    """

    ######SET


    def SetDimension(self, height:float,weight:float,
    width:float,large:float)->bool:
        """
        This method takes in the following attributes in order:
        height;weight;widht;large , and takes it to define a complete dimension
        object with all of it's attrbs described. If the chage could be made it
        returns True, if couldn't it returns False.
        """
        convers = False

        if (Dimension.__ValidateHeight(height) and
        Dimension.__ValidateWeigth(weight) and
        Dimension.__ValidateWidth(width) and
        Dimension.__ValidateWeigth(large)):

            convers = True
            self.__height = height
            self.__weight = weight
            self.__width = width
            self.__large = large
            self.__volume = height*large*width

        return convers


    #When we discrube the dimensions, of a Product, Vehicle's model or it's
    # trunk capacity, we should do it with the function above. this one's are
    #for changing parameters, only for litle exceptions.


    def SetHeight(self, dim:float)->bool:
        """
        This method sets the height of an object,
        change's it's height to the one passed as argument (float) and returns a
        True, if change couldn't be made it returns False
        """
        condition = False
        if Dimension.__ValidateHeight(dim):
            condition= True
            self.__height = dim
        return condition

    def SetWeight(self, mass:float)->bool:
        """
        This method sets the weight of an object,
        change's it's height to the one passed as argument (float) and returns a
        True, if change couldn't be made it returns False
        """
        condition = False
        if Dimension.__ValidateWeigth(mass):
            condition= True
            self.__weight = mass
        return condition

    def SetWidht(self, dist:float)->bool:
        """
        This method sets the widht of an object,
        change's it's height to the one passed as argument (float) and returns a
        True, if change couldn't be made it returns False
        """
        condition = False
        if Dimension.__ValidateWidth(dist):
            condition= True
            self.__width = dist
        return condition

    def SetLarge(self, dist:float)->bool:
        """
        This method sets the large of an object,
        change's it's height to the one passed as argument (float) and returns a
        True, if change couldn't be made it returns False
        """
        condition = False
        if Dimension.__ValidateLarge(dist):
            condition= True
            self.__large = dist
        return condition

    ######GET

    def GetHeight(self)->float:
        """
        This method return the height of the Dimension object whose applied
        """
        return self.__height

    def GetWeight(self)->float:
        """
        This method return the height of the Dimension object whose applied
        """
        return self.__weight

    def GetWidth(self)->float:
        """
        This method return the height of the Dimension object whose applied
        """
        return self.__width

    def GetLarge(self)->float:
        """
        This method return the height of the Dimension object whose applied
        """
        return self.__large

    def GetVolume(self)->float:
        """
        This method return the height of the Dimension object whose applied
        """
        return self.__volume


    def DimensionToString(self)->str:
        string = ''
        string += 'Height: '
        string += str(self.__height)
        string += ' m\nWidth: '
        string += str(self.__width)
        string += ' m\nLarge: '
        string += str(self.__large)
        string += ' m\nWeight: '
        string += str(self.__weight)
        string += ' Kg\nVolume: '
        string += str(self.__volume)
        string += ' m3\n'
        return string

    ########COMPARISION

    """
    All comparisions are made based uppon volume.
    """

    def __gt__(self, dimension)->bool:
        if self.__volume > dimension.__volume:
            return True
        else:
            return False

    def __ge__(self, dimension)->bool:
        if(self.__volume > dimension.__volume or
        self.__volume == dimension.__volume):
            return True
        else:
            return False


    def __eq__(self, dimension)->bool:
        if self.__volume == dimension.__volume:
            return True
        else:
            return False

    def __lt__(self, dimension)->bool:
        if self.__volume < dimension.__volume:
            return True
        else:
            return False

    def __le__(self, dimension)->bool:
        if (self.__volume < dimension.__volume or
        self.__volume == dimension.__volume):
            return True
        else:
            return Falses

def main():
    first = Dimension()
    second = Dimension()
    third = Dimension()
    cond1 = first.SetDimension(4,123,1.3,2.6)
    cond2 = second.SetDimension(1.3,200,1.7,3.4)
    cond3 =third.SetDimension(2.7,222,2.3,5.6)
    if cond1 and cond2 and cond3:
        print('assignation correct\n\n')

    print(first.DimensionToString())
    print(second.DimensionToString())
    print(third.DimensionToString())
    return

if __name__ == '__main__':
    main()
