def menu():
    print("")
    print("====================================")
    print("== Sistema de cafe, cha e lasanha ==")
    print("====================================")
    print("== 1. Criar um café               ==")
    print("== 2. Listar cafés                ==")
    print("== 3. qual o maior preço do café  ==")
    print("== 4. Sair                        ==")
    print("====================================")
    print("")
    print("Escolha uma opção:")
    print("")

class Cafe:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Café: {self.nome} - R$: {self.preco:.2f}"

cafes = []

while True:
    menu()
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
       nome = input("Digite o nome do café: ")
       preco = float(input("Digite o preço do café: "))
       
       novo_cafe = Cafe(nome, preco)
       cafes.append(novo_cafe)  
    
       if len(cafes) == 0:
           print("Nenhum café cadastrado.")
       else:
           print("\n ---Lista de Cafés ---")
           for cafe in cafes:
               print(cafe)
    
    elif opcao == 3:
        mais_caro = cafes[0]
        for cafe in cafes:
            if cafe.preco > mais_caro.preco:
                mais_caro = cafe
        print(f"\n\n O café mais caro é: {mais_caro.nome} - R$: {mais_caro.preco:.2f}")
       
    elif opcao == 2:
        if len(cafes) == 0:
            print("Nenhum café cadastrado.")
        else:
            print("\n ---Lista de Cafés ---\n")
            for cafe in cafes:
                print(cafe)
