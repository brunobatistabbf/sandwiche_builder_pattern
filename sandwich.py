#Produto Final
class Sandwich:
    def __init__(self):
        self.bread = None
        self.meat = None
        self.veggies = []
        self.condiments = []

    def __str__(self):
        return (f"Pão: {self.bread}, Carne: {self.meat}, "
                f"Vegetais: {', '.join(self.veggies)}, "
                f"Condimentos: {', '.join(self.condiments)}")