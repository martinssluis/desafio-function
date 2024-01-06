rendimento = input("Qual é o rendimento da lata?")
altura = input("Qual a altura da parede?")
largura = input("Qaul a largura da parede?")

def calculo_tinta():
    area = altura * largura
    total = area/rendimento
    print("Você precisa de {toal} latas de tinta")

calculo_tinta()