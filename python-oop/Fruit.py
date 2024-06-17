class Fruit():
    def __init__(self,fruit):
        print('Fruit type : ',fruit)
        pass
    
class FruitFlavour(Fruit):
    def __init__(self, fruit):
        super().__init__(fruit)
        