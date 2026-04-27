from numbers import Number


class Automobile:
    __Num_gear = 6
    def __init__(self):
        self.__name = None   # __ is used to make data private  ,  _ is used to make data protected   , without(- or __) the data is public
        self.__color = None
        self.__speed = None

    def set_name(self,name):
        self.__name = name
    def set_color(self,color):
        self.__color = color
    def set_speed(self,speed):
        self.__speed = speed

    def get_name(self):
        return self.__name
    def get_color(self):
        return self.__color
    def get_speed(self):
        return self.__speed


    def change_gear(self,gear):
        if gear > Automobile.__Num_gear:
            print("No more gears....")
        elif gear == 1:
            print("Gear sifted to 1 ")
            self.__speed = 20
            print("The speed of the car is :",self.__speed)
        else :
            print("Gear applied..")


    def brake(self):
        print("Applying Accelerator !!!!!!")
        if self.__speed == 0:
            print("The car is already stoped...")
        else :
            print("The speed of the car at current time is :",self.__speed)
            self.__speed -= 20
            print("The speed of the car after applying the break is :", self.__speed)


    def accelerator(self):
        if self.__speed >180:
            print("Your speed is high please slow down the car !!!!")
        else:
            print("Applying Accelerator !!!!!!")
            print("The speed of the car at current time is :", self.__speed)
            self.__speed += 20
            print("The speed of the car after applying the accelerator is :", self.__speed)

auto =Automobile()
auto.set_name("BMW")
auto.set_color("White")
auto.set_speed(150)

print("The name of the car is :",auto.get_name())
print("The color of the car is :",auto.get_color())
print("The speed of the car is :",auto.get_speed())

auto.change_gear(6)
auto.change_gear(7)

auto.accelerator()

auto.brake()

# print(Automobile.__Num_gear)    ## (__Num_gear) it is not accesible as it is private