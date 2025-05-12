class Engine:
    def start(self):
        return "Engine Started."


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        return self.engine.start()
    
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())