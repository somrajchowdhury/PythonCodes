class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def print_details(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

c = Car('Audi','Z4',2016)
print(c.print_details())
