import os
from forex_python.converter import CurrencyRates
c = CurrencyRates()
from pint import UnitRegistry
u = UnitRegistry()

print("Opções de Conversão: \n 1 -> Moedas \n 2 -> Comprimento \n 3 -> Peso \n 4 -> Temperatura \n 5 -> Volume \n 6 -> Dados(GB, MB, KB) \n 7 -> Velocidade \n \n")
opcao_medida = input("Digite a opção desejada: ")

if opcao_medida.isdigit() and int(opcao_medida) in range(1, 8):
    opcao_medida = int(opcao_medida)
else:
    print("Digite uma das opções!")
    quit()
os.system('cls')

def opcao_moedas():
    print("Opções de Moedas: \n 1 -> Real(BRL) \n 2 -> Dólar Americano(USD) \n 3 -> Euro(EUR) \n 4 -> Libra Esterlina(GBP) \n 5 -> Iene Japonês(JPY) \n 6 -> Dólar Canadense(CAD) \n \n")
    moedas = [' ', 'BRL', 'USD', 'EUR', 'GBP', 'JPY', 'CAD']
    moeda_symb = [' ', 'R$', '$', '€', '£', '¥', 'C$']
    moedas_nomes = [' ', 'Real/Reais', 'Dólar(es) Americano(s)', 'Euro(s)', 'Libra(s)', 'Iene(s)', 'Dólar(es) Canadense(s)']
    while True:
        moeda1 = input("Qual moeda você quer converter? ")
        if moeda1.isdigit(): 
            moeda1 = int(moeda1)
            if moeda1 in range(1, 7):
                break
        print("Digite um valor válido!")

    while True:
        num = input(f"Converter quanto(a)(s) {moedas_nomes[moeda1]}?(digite um '.' caso houver decimal) ")
        try:
            num = float(num)
            break
        except:
            print("Digite um número!")
 
    while True:
        moeda2 = input(f"Você quer converter {num:.2f} {moedas_nomes[moeda1]} para: ")
        if moeda2.isdigit(): 
            moeda2 = int(moeda2)
            if moeda2 in range(1, 7) and moeda2 != moeda1:
                break
        print("Digite um valor válido!")

    resultado = round((c.convert(moedas[moeda1], moedas[moeda2], num)), 2)

    print(f"\nA conversão de {num:.2f} {moedas_nomes[moeda1]} para {moedas_nomes[moeda2]} é: {moeda_symb[moeda2]} {resultado}\n")  

def opcao_comp():
    print("Opções de Comprimento: \n 1 -> Quilômetros(km) \n 2 -> Metros(m) \n 3 -> Centímetros(cm) \n 4 -> Milímetros(mm) \n 5 -> Polegada(in) \n 6 -> Pé(ft) \n 7 -> Jarda(yd) \n 8 -> Milha(mi) \n \n")
    comps_nomes = ['', 'Quilômetros', 'Metros', 'Centímetros', 'Milímetros', 'Polegadas', 'Pés', 'Jardas', 'Milhas']
    comps = ['', 'km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi']
    while True:
        comp1 = input("Qual a medida de comprimento que deseja converter?: ")
        if comp1.isdigit():
            comp1 = int(comp1)
            if comp1 in range(1, 9):
                break
        print("Digite um valor válido!")

    while True:
        num = input(f"Converter quanto(a)(s) {comps_nomes[comp1]}?(digite um '.' caso houver decimal) ")
        try:
            num = float(num)
            break
        except:
            print("Digite um número!")
    
    while True:
        comp2 = input(f"Converter {num} {comps_nomes[comp1]} para: ")
        if comp2.isdigit():
            comp2 = int(comp2)
            if comp2 in range(1, 9) and comp2 != comp1:
                break
        print("Digite um valor válido!")
    
    valor = num * u(comps[comp1])
    resultado = valor.to(u(comps[comp2]))

    print(f"O resultado da conversão de {num} {comps_nomes[comp1]} para {comps_nomes[comp2]} é: {resultado.magnitude:.2f} {comps[comp2]}")

def opcao_peso():
    print("Opções de Peso/Massa: \n 1 -> Quilograma(kg) \n 2 -> Grama(g) \n 3 -> Míligrama(mg) \n 4 -> Tonelada(t) \n 5 -> Libra/Pound(lb) \n 6 -> Onça(oz) \n \n")
    pesos = [['', ''], ['Quilograma(s)', 'kg'], ['Grama(s)', 'g'], ['Míligrama(s)', 'mg'], ['Tonelada(s)', 't'], ['Libra(s)', 'lb'], ['Onça(s)', 'oz']]
    while True:
        peso1 = input("Qual medida de peso deseja converter? ")
        if peso1.isdigit():
            peso1 = int(peso1)
            if peso1 in range(1, 7):
                break
        print("Digite um valor válido!")

    while True:
        num = input(f"Converter quanto(a)(s) {pesos[peso1][0]}?(digite um '.' caso houver decimal) ")
        try:
            num = float(num)
            break
        except:
            print("Digite um número!")

    while True:
        peso2 = input("Qual medida de peso deseja converter? ")
        if peso2.isdigit():
            peso2 = int(peso2)
            if peso2 in range(1, 7) and peso2 != peso1:
                break
        print("Digite um valor válido!")

    valor = num * u(pesos[peso1][1])
    resultado = valor.to(u(pesos[peso2][1]))
    print(f"A conversão de {num} {pesos[peso1][0]} para {pesos[peso2][0]} é: {resultado.magnitude:.2f} {pesos[peso2][1]}")

match opcao_medida:
    case 1: 
        opcao_moedas()
    case 2:
        opcao_comp()
    case 3:
        opcao_peso()

