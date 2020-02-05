import sys
import os
from classes.profit import Profit

while True:
    print('Lucro da ação\n')
    print("""O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto
espaço de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array
K com os valores das ações nos determinados dias, onde ele poderá escolher onde comprar e vender.\n""")

    try:
        values = list(int(num) for num in input("Informe os valores das ações separados por espaço: ").strip().split())
    except:
        print('Informe os valores das ações separados por espaço')
        sys.exit()

    profit = Profit(values)
    print('\nO maior lucro possível será de: %d\n\n' % profit.calculate_profit())

    message = input('\nDigite (sim) se deseja calcular o lucro com outros valores: ')
    if (message.lower() != 'sim'):
        sys.exit()

    clear = lambda: os.system('clear')
    clear()