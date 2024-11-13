def add(*args):
    sec_arg = args[1]
    return sec_arg


def my_function(**kwargs):
    pass

class car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = car(make= "Nissan", model = "GT-R")
print(my_car.make)

the_package_name.a_class()
 import the
