from .condiment_decorator import CondimentDecorator
class Mocha(CondimentDecorator):
    def description(self): return self.beverage.description() + ", Mocha"
    def cost(self): return self.beverage.cost() + 0.2
