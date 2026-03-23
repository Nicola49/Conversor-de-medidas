import os
from forex_python.converter import CurrencyRates

c = CurrencyRates()

opcao_medida = input("Opções de Conversão: \n 1 -> Moedas \n 2 -> Comprimento \n 3 -> Peso \n 4 -> Temperatura \n 5 -> Volume \n 6 -> Dados(GB, MB, KB) \n 7 -> Velocidade \n \n")
print(" ")

if opcao_medida.isdigit() and int(opcao_medida) in range(1, 8):
    opcao_medida = int(opcao_medida)
else:
    print("Digite uma das opções!")
    quit()
os.system('cls')

def opcao_moedas():
    print("Opções de Moedas: \n 1 -> Real(BRL) \n 2 -> Dólar Americano(USD) \n 3 -> Euro(EUR) \n 4 -> Libra Esterlina(GBP) \n 5 -> Iene Japonês(JPY) \n 6 -> Dólar Canadense(CAD) \n \n")
    while True:
        moeda1 = input("Qual moeda você quer converter? ")
        if moeda1.isdigit(): 
            moeda1 = int(moeda1)
            if moeda1 in range(1, 7):
                break
        print("Digite um valor válido!")

    match moeda1:
        case 1:
            moeda1nome = "Real/Reais" 
        case 2:
            moeda1nome = "Dólar(es) Americano(s)"
        case 3:
            moeda1nome = "Euro(s)"
        case 4:
            moeda1nome = "Libra(s)" 
        case 5:
            moeda1nome = "Iene(s)"
        case 6:
            moeda1nome = "Dólar(es) Canadense(s)"

    while True:
        num = input(f"Converter quanto(a)(s) {moeda1nome}?(digite um '.' caso houver decimal) ")

        try:
            num = float(num)
            break
        except:
            print("Digite um valor válido!")
 
    while True:
        moeda2 = input(f"Você quer converter {num:.2f} {moeda1nome} para: ")
        if moeda2.isdigit(): 
            moeda2 = int(moeda2)
            if moeda2 in range(1, 7) and moeda2 != moeda1:
                break
        print("Digite um valor válido!")

    match moeda2:
        case 1:
            moeda2nome = "Real/Reais" 
        case 2:
            moeda2nome = "Dólar(es) Americano(s)"
        case 3:
            moeda2nome = "Euro(s)"
        case 4:
            moeda2nome = "Libra(s)" 
        case 5:
            moeda2nome = "Iene(s)"
        case 6:
            moeda2nome = "Dólar(es) Canadense(s)"
    if moeda1 == 1:
        match moeda2:
            case 2: resultado = round((c.convert('BRL', 'USD', num)), 2)
            case 3: resultado = round((c.convert('BRL', 'EUR', num)), 2)
            case 4: resultado = round((c.convert('BRL', 'GBP', num)), 2)
            case 5: resultado = round((c.convert('BRL', 'JPY', num)))
            case 6: resultado = round((c.convert('BRL', 'CAD', num)), 2)
    if moeda1 == 2:
        match moeda2:
            case 1: resultado = round((c.convert('USD', 'BRL', num)), 2)
            case 3: resultado = round((c.convert('USD', 'EUR', num)), 2)
            case 4: resultado = round((c.convert('USD', 'GBP', num)), 2)
            case 5: resultado = round(c.convert('USD', 'JPY', num))
            case 6: resultado = round((c.convert('USD', 'CAD', num)), 2)
    if moeda1 == 3:
        match moeda2:
            case 1: resultado = round((c.convert('EUR', 'BRL', num)), 2)
            case 2: resultado = round((c.convert('EUR', 'USD', num)), 2)
            case 4: resultado = round((c.convert('EUR', 'GBP', num)), 2)
            case 5: resultado = round(c.convert('EUR', 'JPY', num))
            case 6: resultado = round((c.convert('EUR', 'CAD', num)), 2)
    if moeda1 == 4:
        match moeda2:
            case 1: resultado = round((c.convert('GBP', 'BRL', num)), 2)
            case 2: resultado = round((c.convert('GBP', 'USD', num)), 2)
            case 3: resultado = round((c.convert('GBP', 'EUR', num)), 2)
            case 5: resultado = round(c.convert('GBP', 'JPY', num))
            case 6: resultado = round((c.convert('GBP', 'CAD', num)), 2)
    if moeda1 == 5:
        match moeda2:
            case 1: resultado = round((c.convert('JPY', 'BRL', num)), 2)
            case 2: resultado = round((c.convert('JPY', 'USD', num)), 2)
            case 3: resultado = round((c.convert('JPY', 'EUR', num)), 2)
            case 4: resultado = round((c.convert('JPY', 'GBP', num)), 2)
            case 6: resultado = round((c.convert('JPY', 'CAD', num)), 2)
    if moeda1 == 6:
        match moeda2:
            case 1: resultado = round((c.convert('CAD', 'BRL', num)), 2)
            case 2: resultado = round((c.convert('CAD', 'USD', num)), 2)
            case 3: resultado = round((c.convert('CAD', 'EUR', num)), 2)
            case 4: resultado = round(c.convert('CAD', 'GBP', num))
            case 5: resultado = round((c.convert('CAD', 'JPY', num)), 2)
    finalmoeda = (f"A conversão de {num:.2f} {moeda1nome} para {moeda2nome} é: {resultado}")
    return finalmoeda   

if opcao_medida == 1: 
    print(opcao_moedas())