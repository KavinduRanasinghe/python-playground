from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def hello(self):
        print()
        pass
    pass
        
    



class B(A):
    
    def hello(self):
        print("Hello b")
    pass


b= B()

b.hello()