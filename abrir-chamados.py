nome = input("Digite seu nome: ")

setor = input("Digite seu setor: ")

descricao = input("Descreva seu problema: ")

print("Nível de Urgencia:\n 1.Urgente\n 2.Alto\n 3.Médio\, 4.Baixa\n 0.Sair")

urgencia = int(input("De 1 a 4, qual o nível de urgência de seu pedido?"))

urgentes = []
alto = []
medio = []
baixo = []

if urgencia == 1:
    urgentes.append(descricao)
    print("Urgente!!!",nome, setor, urgentes)

elif urgencia == 2:
    alto.append(descricao)
    print("Alta urgencia::", nome, setor, alto)
elif urgencia == 3:
    medio.append(descricao)
    print("Media urgencia: ", nome, setor, medio)
elif urgencia == 4:
    baixo.append(descricao)
    print('Baixa urgencia: ', nome, setor, baixo)
else:
    print ('Opção inválida')

# Objetivo é fazer as informações vão para uma planilha do Google, que atualize toda vez que alguém abra o chamado.