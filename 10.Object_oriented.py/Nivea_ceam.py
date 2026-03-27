class Nivea_cream:
    def __init__(self, consistency, gradient):
        self.consistency = consistency
        self.gradient = gradient 
My_nivea = Nivea_cream( "Slimey", "Rough" )
print(My_nivea.consistency)

class Baby_oil:
    def __init__(self, consistency, gradient):
        self.consistency = consistency
        self.gradient = gradient 
My_oil = Baby_oil("Oily", "slipery")
print(My_oil.gradient)
        