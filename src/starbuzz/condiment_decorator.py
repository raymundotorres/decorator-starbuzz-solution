from abc import abstractmethod
from .beverage import Beverage
class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage): self.beverage = beverage
    @abstractmethod
    def description(self) -> str: raise NotImplementedError
