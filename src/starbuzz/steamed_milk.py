from .condiment_decorator import CondimentDecorator
class SteamedMilk(CondimentDecorator):
    def description(self): return self.beverage.description() + ", Steamed Milk"
    def cost(self): return self.beverage.cost() + 0.1
