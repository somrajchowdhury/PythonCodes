class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        print('A Car object is Created!')

    def print_details(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

c = Car('Audi','Z4',2016)
print(c.print_details())

'''
---------Output---------

A Car object is Created!
2016 Audi Z4

------------------------
'''
