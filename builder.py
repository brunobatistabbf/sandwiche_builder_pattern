from abc import ABC, abstractmethod
from sandwich import Sandwich

class SandwichBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_bread(self, bread):
        pass

    @abstractmethod
    def add_meat(self, meat):
        pass

    @abstractmethod
    def add_veggies(self, veggies):
        pass

    @abstractmethod
    def add_condiments(self, condiments):
        pass

    @abstractmethod
    def get_sandwich(self):
        pass



class VeggieSandwich(SandwichBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.sandwich = Sandwich()

    def set_bread(self, bread):
        self.sandwich.bread = bread

    def add_meat(self, meat):
        pass

    def add_veggies(self, veggies):
        self.sandwich.veggies.extend(veggies)

    def add_condiments(self, condiments):
        self.sandwich.condiments.extend(condiments)

    def get_sandwich(self):
        return  self.sandwich


class MeatSandwich(SandwichBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.sandwich = Sandwich()

    def set_bread(self, bread):
        self.sandwich.bread = bread

    def add_meat(self, meat):
        self.sandwich.meat = meat

    def add_veggies(self, veggies):
        self.sandwich.veggies.extend(veggies)

    def add_condiments(self, condiments):
        self.sandwich.condiments.extend(condiments)

    def get_sandwich(self):
        return self.sandwich