from abc import ABC

class MyInterface(ABC):
    # Defining abstract method ::
    @abc.abstractmethod
    def absmethod(self):
        pass
