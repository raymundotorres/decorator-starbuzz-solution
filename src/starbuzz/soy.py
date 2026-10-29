from .condiment_decorator import CondimentDecorator
class Soy(CondimentDecorator):
    def description(self): return self.beverage.description() + ", Soy"
    def cost(self): return self.beverage.cost() + 0.15
