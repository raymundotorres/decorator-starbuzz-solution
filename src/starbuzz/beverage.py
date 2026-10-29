from abc import ABC, abstractmethod
class Beverage(ABC):
    @abstractmethod
    def description(self) -> str: raise NotImplementedError
    @abstractmethod
    def cost(self) -> float: raise NotImplementedError
