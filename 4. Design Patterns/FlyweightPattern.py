class ComplexCars(object):
    """Separate class for Complex Cars"""

    def __init__(self):
        pass

    def cars(self, car_name):
        return "ComplexPattern[% s]" % (car_name)


class CarFamilies(object):
    """dictionary to store ids of the car"""

    car_family = {}

    def __new__(cls, name, car_family_id):
        try:
            id = cls.car_family[car_family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.car_family[car_family_id] = id
        return id

    def set_car_info(self, car_info):

        """set the car information"""

        cg = ComplexCars()
        self.car_info = cg.cars(car_info)

    def get_car_info(self):

        """return the car information"""

        return (self.car_info)
# if __name__ == '__main__':
#     car_data = (('a', 1, 'Audi'), ('a', 2, 'Ferrari'), ('b', 1, 'Audi'), ('m', 3, 'Mecedes'))
#     car_family_objects = []
#     for i in car_data:
#         obj = CarFamilies(i[0], i[1])
#         obj.set_car_info(i[2])
#         car_family_objects.append(obj)
#
#     """similar id's says that they are same objects """
#
#
#     for i, ins in CarFamilies.car_family.items():
#         print(str(i),  str(id(ins)), ins.get_car_info())
#
#     for i in car_family_objects:
#         print("id = " + str(id(i)))
#         print(i.get_car_info())
##########################################################################
# Another EXAMPLE
##########################################################################




import abc


class FlyweightFactory:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=abc.ABCMeta):
    """
    Declare an interface through which flyweights can receive and act on
    extrinsic state.
    """

    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    """
    Implement the Flyweight interface and add storage for intrinsic
    state, if any. A ConcreteFlyweight object must be sharable. Any
    state it stores must be intrinsic; that is, it must be independent
    of the ConcreteFlyweight object's context.
    """

    def operation(self, extrinsic_state):
        pass
def main():
    flyweight_factory = FlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight("key")
    concrete_flyweight.operation(None)


if __name__ == "__main__":
    main()