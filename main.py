from builder import VeggieSandwich, MeatSandwich
from director import Director


def lanchonete(a):
    if a == 1:
        veggie_builder = VeggieSandwich()
        director = Director(veggie_builder)
        director.build_veggie_sandwich()
        veggie_sandwich = veggie_builder.get_sandwich()
        print("Sanduiche Vegano")
        print(veggie_sandwich)
        print()
    elif a == 2:
        meat_builder = MeatSandwich()
        director = Director(MeatSandwich)
        director.build_meat_sandwich()
        meat_sandwich = meat_builder.get_sandwich()
        print("Sanduiche com Carne")
        print(meat_sandwich)
        print()
    elif a == 3:

        print("Bem-vindo(a) ao Pedido Personalizado")
        print()
        print("Preencha seu pedido:")
        add_bread = input("Qual o tipo de pão deseja?")
        add_meat = input("Qual a carne de escolha?")
        add_veggies = input("Qual o vegetal?")
        add_condiments = input("Qual o molho?")
        print()

        custom_builder = MeatSandwich()
        custom_builder.reset()
        custom_builder.set_bread(add_bread)
        custom_builder.add_meat(add_meat)
        custom_builder.add_veggies([add_veggies])
        custom_builder.add_condiments([add_condiments])
        custom_sandwich = custom_builder.get_sandwich()
        print("Sanduiche Personalizado")
        print(custom_sandwich)
        print()
    else:
        print("Insira um numero Válido")


if __name__ == '__main__':
    print("------------------ Lanchonete Inc. --------------------")
    print()
    print("Faça o pedido do seu Sanduíche, escolha uma opção:")
    print("1 - Sanduíche Vegano")
    print("2 - Sanduíche Com Carne")
    print("3 - Sanduíche Personalizado")
    print()
    a = int(input("Insira o numero do Pedido:"))

    lanchonete(a)
