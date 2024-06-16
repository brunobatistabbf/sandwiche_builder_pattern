from builder import SandwichBuilder

class Director:
    def __init__(self, builder: SandwichBuilder):
        self._builder = builder

    def build_veggie_sandwich(self):
        self._builder.reset()
        self._builder.set_bread("7 Grãos")
        self._builder.add_veggies(["Alface, Tomate, Picles"])
        self._builder.add_condiments(["Maionese", "Mustarda"])

    def build_meat_sandwich(self):
        self._builder.reset()
        self._builder.set_bread("7 Grãos")
        self._builder.add_meat("Bovina")
        self._builder.add_veggies(["Alface, Tomate, Picles"])
        self._builder.add_condiments(["Maionese", "Mustarda", "BBQ"])