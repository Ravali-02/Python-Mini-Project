#  classess arelike blue print when we want to craete omething and
# we are going to create objects with classess are blue prnts to objects

class Motor:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        # self.happy = happy

    def moves(self):
        print("Moves along....")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


# my_vehicle is a object that create from the class Motor
my_vehicle = Motor("BMW", "Model 23.4")
my_vehicle.get_make_model()
print(my_vehicle.make)
print(my_vehicle.model)
my_vehicle.moves()  # a class have propteries

My_car = Motor("Merede", "Tesla")
My_car.get_make_model()
My_car.moves()


class Parent(Motor):
    # def __init__(self, make, model, happy):
    #     super().__init__(make, model, happy)
    #     self.happy = happy

    def moves(self):
        print("I am Dad....")


class child(Motor):
    def moves(self):
        print("I am your child...")


class grandchild(Motor):
    def moves(self):
        print("I am your Grandchild...")


class child_1(Motor):
    pass


Vishwanath = Parent("grandfather", "sukanaya")
Kumarswamr = child("Father", "Dad")
Chetan = child_1("kumarswamy", "chetan")
Ravali = grandchild("Ravali's", "Happies")

Vishwanath.get_make_model()
Vishwanath.moves()
# Vishwanath.happy()
Kumarswamr.get_make_model()
Kumarswamr.moves()
Chetan.get_make_model()
Chetan.moves()
Ravali.get_make_model()
Ravali.moves()

# print(Vishwanath)
# print(Kumarswamr)
# print(Chetan)
# polymorphisim

print('\n\n')

for v in (my_vehicle, My_car, Vishwanath, Kumarswamr, Chetan, Ravali):
    v.get_make_model()
    v.moves()
