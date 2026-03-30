import os
from forex_python.converter import CurrencyRates
c = CurrencyRates()
from pint import UnitRegistry
u = UnitRegistry()

ne = '\033[1m' #negrito
f = '\033[m' #f de final
az = '\033[1;34m' #azul
op = '\033[1;36m' #azul claro
ve = '\033[1;32m' #verde

print(f"{ne}=-={f}" * 20)
print(f"\n {az}Opções de Conversão:{f}\n {op}[ 1 ] {f}Moedas \n {op}[ 2 ] {f}Comprimento \n {op}[ 3 ] {f}Peso \n {op}[ 4 ] {f}Temperatura \n {op}[ 5 ] {f}Volume \n {op}[ 6 ] {f}Dados(GB, MB, KB) \n {op}[ 7 ] {f}Velocidade \n")
print(f"{ne}=-={f}" * 20)
print(" ")

opcao_medida = input("Digite a opção desejada: ").strip()

if opcao_medida.isdigit() and int(opcao_medida) in range(1, 8):
    opcao_medida = int(opcao_medida)
else:
    print("Digite uma das opções!(De 1 a 7)")
    quit()
os.system('cls')

def opcao_moedas():
    print("Opções de Moedas: \n[ 1 ] Real(BRL/R$) \n[ 2 ] Dólar Americano(USD/$) \n[ 3 ] Euro(EUR/€) \n[ 4 ] Libra Esterlina(GBP/£) \n[ 5 ] Iene Japonês(JPY/¥) \n[ 6 ] Dólar Canadense(CAD/C$) \n \n")
    moedas = [['', ''], ['BRL', 'R$'], ['USD', '$'], ['EUR', '€'], ['GBP', '£'], ['JPY', '¥'], ['CAD', 'C$']]
    while True:
        moeda1 = input("Qual moeda você quer converter? ").strip()
        if moeda1.isdigit(): 
            moeda1 = int(moeda1)
            if moeda1 in range(1, 7):
                break
        print("Digite um valor válido!")

    while True:
        num = input(f"Converter quanto(a)(s) {ve}{moedas[moeda1][1]}{f}? ").strip()
        try:
            num = float(num)
            break
        except:
            print("Digite um número!")
 
    while True:
        moeda2 = input(f"Você quer converter {ve}{moedas[moeda1][1]}{num}{f} para: ").strip()
        if moeda2.isdigit(): 
            moeda2 = int(moeda2)
            if moeda2 in range(1, 7) and moeda2 != moeda1:
                break
        print("Digite um valor válido!")

    resultado = round((c.convert(moedas[moeda1], moedas[moeda2], num)), 2)

    print(f"{ve}{moedas[moeda1][1]}{num}{f} = {az}{moedas[moeda2][1]}{resultado:.2f}{f}")

def opcao_comp():
    print("Opções de Comprimento: \n[ 1 ] Quilômetros(km) \n[ 2 ] Metros(m) \n[ 3 ] Centímetros(cm) \n[ 4 ] Milímetros(mm) \n[ 5 ] Polegada(in) \n[ 6 ] Pé(ft) \n[ 7 ] Jarda(yd) \n[ 8 ] Milha(mi) \n \n")
    comps = [['', ''], ['Quilômetros', 'km'], ['Metros', 'm'], ['Centímetros', 'cm'], ['Milímetros', 'mm'], ['Polegadas', 'in'], ['Pés', 'ft'], ['Jardas', 'yd'], ['Milhas', 'mi']]
    while True:
        comp1 = input("Qual a medida de comprimento que deseja converter?: ").strip()
        if comp1.isdigit():
            comp1 = int(comp1)
            if comp1 in range(1, 9):
                break
        print("Digite um valor válido!")

    while True:
        num = input(f"Converter quanto(a)(s) {ve}{comps[comp1][0]}{f}? ").strip()
        if num.isdigit():
            num = float(num)
            if num > 0:
                break
        print("Digite um número!(MAIOR QUE 0)")
    
    while True:
        comp2 = input(f"Converter {ve}{num} {comps[comp1][1]}{f} para: ").strip()
        if comp2.isdigit():
            comp2 = int(comp2)
            if comp2 in range(1, 9) and comp2 != comp1:
                break
        print("Digite um valor válido!")
    
    valor = num * u(comps[comp1][1])
    resultado = valor.to(u(comps[comp2][1]))

    print(f"{ve}{num} {comps[comp1][1]}{f} = {az}{resultado.magnitude:.2f} {comps[comp2][1]}{f}")

def opcao_peso():
    print("Opções de Peso/Massa: \n[ 1 ] Quilograma(kg) \n[ 2 ] Grama(g) \n[ 3 ] Míligrama(mg) \n[ 4 ] Tonelada(t) \n[ 5 ] Libra/Pound(lb) \n[ 6 ] Onça(oz) \n \n")
    pesos = [['', ''], ['Quilograma(s)', 'kg'], ['Grama(s)', 'g'], ['Míligrama(s)', 'mg'], ['Tonelada(s)', 't'], ['Libra(s)', 'lb'], ['Onça(s)', 'oz']]
    while True:
        peso1 = input("Qual medida de peso deseja converter? ").strip()
        if peso1.isdigit():
            peso1 = int(peso1)
            if peso1 in range(1, 7):
                break
        print("Digite um valor válido!(De 1 a 6)")

    while True:
        num = input(f"Converter quanto(a)(s) {ve}{pesos[peso1][0]}{f}? ").strip()
        if num.isdigit():
            num = float(num)
            if num > 0:
                break
        print("Digite um número!")

    while True:
        peso2 = input(f"Converter {ve}{num} {pesos[peso1][1]}{f} para: ").strip()
        if peso2.isdigit():
            peso2 = int(peso2)
            if peso2 in range(1, 7) and peso2 != peso1:
                break
        print("Digite um valor válido!(De 1 a 6)")

    valor = num * u(pesos[peso1][1])
    resultado = valor.to(u(pesos[peso2][1]))
    print(f"{ve}{num} {pesos[peso1][1]}{f} = {az}{resultado.magnitude:.2f} {pesos[peso2][1]}{f}")

def opcao_temp():
    print("Opções de Temperatura: \n[ 1 ] Celsius(°C) \n[ 2 ] Fahrenheit(°F) \n[ 3 ] Kelvin(K) \n \n")
    temps = [['', '',], ['°C', 'degC'], ['°F', 'degF'], ['K', 'kelvin']]
    while True:
        temp1 = input("Qual opção de Temperatura você quer converter? ").strip().strip()
        if temp1.isdigit():
            temp1 = int(temp1)
            if temp1 in range(1, 4):
                break
        print("Digite um valor válido!(De 1 a 3)")

    while True:
        num = input(f"Quanto(s) {ve}{temps[temp1][0]}{f} você deseja converter? ").strip()
        try:
            num = int(num)
            break
        except:
            print("Digite um número!")

    while True:
        temp2 = input(f"Converter {ve}{num}{temps[temp1][0]}{f} para: ").strip()
        if temp2.isdigit():
            temp2 = int(temp2)
            if temp2 in range(1, 4) and temp2 != temp1:
                break
        print("Digite um valor válido!(De 1 a 3, diferente da 1ª opção)")
    
    valor = u.Quantity(num, temps[temp1][1])
    resultado = valor.to(temps[temp2][1])
    print(f"{ve}{num} {temps[temp1][0]}{f} = {az}{resultado.magnitude:.2f} {temps[temp2][0]}{f}")

def opcao_vol():
    print("Opções de Volume: \n[ 1 ] Litro(L) \n[ 2 ] Mililítro(mL) \n[ 3 ] Métros Cúbico(m³) \n[ 4 ] Galão(gal) \n[ 5 ] Pinta(pt) \n[ 6 ] Onça Líquida(fl oz) \n \n")
    volumes = [['', ''], ['L', 'L'], ['mL', 'mL'], ['m³', 'm^3'], ['gal', 'gal'], ['pt', 'pt'], ['fl oz', 'fl_oz']]
    while True:
        vol1 = input("Qual medida de volume deseja converter? ").strip()
        if vol1.isdigit():
            vol1 = int(vol1)
            if vol1 in range(1, 7):
                break
        print("Digite um valor válido!(de 1 a 6)")

    while True:
        num = input(f"Quanto(s) {ve}{volumes[vol1][0]}{f} deseja converter? ").strip()
        if num.isdigit():
            num = float(num)
            if num > 0:
                break
        print("Digite um número maior que 0!")

    while True:
        vol2 = input(f"Converter {ve}{num} {volumes[vol1][0]}{f} para: ").strip()
        if vol2.isdigit():
            vol2 = int(vol2)
            if vol2 in range(1, 7) and vol2 != vol1:
                break
        print("Digite um valor válido!(de 1 a 6, diferente da 1° opção)")

    valor = num * u(volumes[vol1][1])
    resultado = valor.to(u(volumes[vol2][1]))
    print(f"{ve}{num} {volumes[vol1][0]}{f} = {az}{resultado.magnitude:.2f} {volumes[vol2][0]}{f}")

def opcao_dados():
    print("Opções de Temperatura: \n[ 1 ] Bit \n[ 2 ] Byte \n[ 3 ] Kilobyte(kB) \n[ 4 ] Megabyte(MB) \n[ 5 ] Gigabyte(GB) \n[ 6 ] Terabyte(TB) \n \n")
    dados = ['', 'bit', 'byte', 'kB', 'MB', 'GB', 'TB']
    while True:
        dado1 = input("Qual opção de Dados você quer converter? ").strip()
        if dado1.isdigit():
            dado1 = int(dado1)
            if dado1 in range(1, 7):
                break
        print("Digite um valor válido(de 1 a 6)")

    while True:
        num = input(f"Quantos {ve}{dados[dado1]}{f} você deseja converter? ").strip()
        if num.isdigit():
            num = float(num)
            if num > 0:
                break
        print("Digite um número maior que 0!")

    while True:
        dado2 = input(f"Converter {ve}{num} {dados[dado1]}{f} para: ").strip()
        if dado2.isdigit():
            dado2 = int(dado2)
            if dado2 in range(1, 7) and dado2 != dado1:
                break
        print("Digite um valor válido!(de 1 a 6, diferente da 1° opção)")
    
    valor = num * u(dados[dado1])
    resultado = valor.to(u(dados[dado2]))
    print(f"{ve}{num}{dados[dado1]}{f} = {az}{resultado.magnitude:.2f} {dados[dado2]}{f}")

def opcao_vel():
    print("Opções de Velocidade: \n[ 1 ] Quilômetro por hora(km/h) \n[ 2 ] Metros por segundo(m/s) \n[ 3 ] Milhas por hora(mph) \n[ 4 ] Nós(knot) \n[ 5 ] Pés por segundo(ft/s) \n[ 6 ] Centímetros por segundo(cm/s) \n \n")
    vels = ['', 'km/h', 'm/s', 'mph', 'knot', 'ft/s', 'cm/s']
    while True:
        vel1 = input("Qual opção de Dados você quer converter? ").strip()
        if vel1.isdigit():
            vel1 = int(vel1)
            if vel1 in range(1, 7):
                break
        print("Digite um valor válido(de 1 a 6)")

    while True:
        num = input(f"Quantos {ve}{vels[vel1]}{f} você deseja converter? ").strip()
        if num.isdigit():
            num = float(num)
            if num > 0:
                break
        print("Digite um número maior que 0!")

    while True:
        vel2 = input(f"Converter {ve}{num} {vels[vel1]}{f} para: ").strip()
        if vel2.isdigit():
            vel2 = int(vel2)
            if vel2 in range(1, 7) and vel2 != vel1:
                break
        print("Digite um valor válido!(de 1 a 6, diferente da 1° opção)")
    
    valor = num * u(vels[vel1])
    resultado = valor.to(u(vels[vel2]))
    print(f"{ve}{num}{vels[vel1]}{f} = {az}{resultado.magnitude:.2f} {vels[vel2]}{f}")

match opcao_medida:
    case 1: 
        opcao_moedas()
    case 2:
        opcao_comp()
    case 3:
        opcao_peso()
    case 4:
        opcao_temp()
    case 5:
        opcao_vol()
    case 6:
        opcao_dados()
    case 7:
        opcao_vel()

