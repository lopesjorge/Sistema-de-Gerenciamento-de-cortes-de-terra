from math import sqrt

#classe Agricultor
class Agricultor:
    def __init__(self,nome,data_nascimento,cpf, Propriedade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.Propriedade = Propriedade
        
        def setNome (self,nome):
            self.nome = nome
            
        def setDataNascimento (self, data_nascimento):
            self.data_nascimento = data_nascimento
        
        def setCpf (self,cpf):
            self.cpf = cpf
            
        def setNomeRua (self,nome_rua):
            self.nome_rua = nome_rua
            
        def setBairro (self,bairro):
            self.bairro = bairro
            
        def setNumero (self,numero):
            self.numero = numero
            
        def setCep (self, cep):
            self.cep = cep

#classe Propriedade
class Propriedade:
    def __init__(self,nome_propriedade, nome_rua, bairro, numero, cep):
        self.nome_propriedade = nome_propriedade
        self.nome_rua = nome_rua
        self.bairro = bairro
        self.numero = numero
        self.cep = cep
        
        def setNomeRua (self,nome_rua):
            self.nome_rua = nome_rua
            
        def setBairro (self,bairro):
            self.bairro = bairro
            
        def setNumero (self,numero):
            self.numero = numero
            
        def setCep (self, cep):
            self.cep = cep    
                    
#Classe Funcionário
class Funcionario:
    def __init__(self,nome,idade,matricula,CPF):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.cpf = CPF
        
        def setNome (self,nome):
            self.nome = nome
            
        def setIdade (self, idade):
            self.idade = idade
            
        def setMatricula (self,matricula):
            self.matricula = matricula
            
        def setCpf (self, CPF):
            self.cpf = CPF
            
        def getNome (self):
            return self.nome
        
        def getIdade (self):
            return self.idade
        
        def getMatricula (self):
            return self.matricula
        
        def getCpf (self):
            return self.cpf

#classe Motorista
class Motorista:
    def __init__(self,Funcionario,cnh,Veiculo):
        self.funcionario = Funcionario
        self.cnh = cnh
        self.veiculo = Veiculo
        
        def setCnh (self, cnh):
            self.cnh = cnh
            
        def getCnh (self):
            return self.chn
                   
#Classe Veiculo
class Veiculo:
    def __init__(self,placa,modelo):
        self.placa = placa
        self.modelo = modelo
        
    def setPlaca (self, placa):
        self.placa = placa
        
    def setModelo (self, modelo):
        self.modelo = modelo
        
    def getPlaca (self):
        return self.placa
    
    def getModelo (self):
        return self.modelo

lista_funcionario = []
lista_motorista = []
lista_veiculo = []
lista_produtor = []
lista_propriedade = []
lista_servico = []

print ("\n\tBem-Vindo ao SGCT:")

x = 1

while x > 0:
    opcao = int (input("1-Cadastrar Funcionário\n2-Cadastrar Produtor Rural\n3-Cadastrar Veículo\n4-Listar Motoristas\n5-Listar Funcionário\n6-Listar Veículos\n7-Listar Produtores Rurais\n8-Listar Propriedades\n9-Envio de Tratores\n0-Sair\n"))

    
    if opcao == 1:
        arquivo_funcionario = open("funcionario", "a")
        arquivo_motorista = open("motorista","a")  
        arquivo_veiculo = open("veiculo", "a")
       

        nome = input("\nDigite o nome:")
        idade = input("Digite a idade:")
        matricula = input("Digite a matrícula:")
        cpf = input("Digite o CPF:")
        funcionario = Funcionario(nome,idade,matricula,cpf)
        lista_funcionario.append(funcionario)
        resposta = int (input("O funcionário é motorista? 1 -Sim  2 -Não\n"))
        
        if resposta == 1:
            cnh = input("Digite o CNH:\n")
            placa = input("Digite o nome da placa:")
            modelo = input("Digite o nome do modelo:\n")
            veic = Veiculo(placa,modelo)
            lista_veiculo.append(veic)

            motorista = Motorista(funcionario,cnh,veic)
            lista_motorista.append(motorista)
            arquivo_motorista.write("Nome: %s %s Idade: Matrícula: %s CNH: %s Dirige veículo:[Placa: %s Modelo:%s]\n" % (motorista.funcionario.nome,motorista.funcionario.idade,motorista.funcionario.matricula,cnh,motorista.veiculo.placa,motorista.veiculo.modelo))
            arquivo_funcionario.write("Nome: %s Idade: %s Matrícula: %s CPF: %s Cargo: Motorista" % (funcionario.nome,funcionario.idade,funcionario.matricula,funcionario.cpf))
            arquivo_veiculo.write("Placa: %s Modelo: %s\n" % (veic.placa, veic.modelo))

            arquivo_motorista.close()
            arquivo_veiculo.close()
            arquivo_funcionario.close()
            
        else:
            arquivo_funcionario = open("funcionario", "a")
            arquivo_funcionario.write("Nome: %s Idade: %s Matrícula: %s CPF: %s\n" % (funcionario.nome,funcionario.idade,funcionario.matricula,funcionario.cpf))
            arquivo_funcionario.close()

    if opcao == 2:
        arquivo_produtor = open("produtor", "a")
        arquivo_servico = open("servico", "a")
        arquivo_propriedade = open("propriedade","a")

        nome = input("\nDigite o nome:")
        idade = input("Digite a data de nascimento:")
        cpf = input("Digite o CPF:")
        print("Digite o endereço da propriedade onde trabalha:\n")
        nome_propriedade = input("Digite o nome da propriedade:")
        rua = input("Digite o endereço:")
        bairro = input("Digite o nome do Bairro:")
        numero = input("Digite o número da casa:")
        cep = input("Digite o Cep:")
        
        propriedade = Propriedade(nome_propriedade,rua,bairro,numero,cep)
        produtor = Agricultor(nome,idade,cpf,propriedade)
        
        lista_produtor.append(produtor)
        lista_propriedade.append(propriedade)
        
        arquivo_produtor.write("Nome: %s, Data de nascimento: %s, CPF: %s, Trabalha em: %s, Endreço: %s, Bairro: %s, Número: %s, CEP: %s\n" % (produtor.nome,produtor.data_nascimento,produtor.cpf,produtor.Propriedade.nome_propriedade,produtor.Propriedade.nome_rua,produtor.Propriedade.bairro,produtor.Propriedade.numero,produtor.Propriedade.cep))
        arquivo_servico.write("Nome da propriedade:%s, Endereço: %s, Bairro: %s, Número: %s, CEP: %s \n" % (propriedade.nome_propriedade,propriedade.nome_rua,propriedade.bairro,propriedade.numero,propriedade.cep))
        arquivo_propriedade.write("Nome da propriedade: %s, Administrada por: %s, Endreço: %s, Bairro: %s, Número: %s, CEP: %s\n" % (propriedade.nome_propriedade,produtor.nome,propriedade.nome_rua,propriedade.bairro,propriedade.numero,propriedade.cep))

        arquivo_produtor.close()
        arquivo_servico.close()
        arquivo_propriedade.close()
        
       
        
    if opcao == 3:
        arquivo_veiculo = open("veiculo", "a")

        placa = input("\nDigite o nome da placa:")
        modelo = input("Digite o nome do modelo:")
        veic = Veiculo(placa,modelo)
        lista_veiculo.append(veic)
        arquivo_veiculo.write("Placa: %s Modelo: %s\n" % (veic.placa, veic.modelo))
        arquivo_veiculo.close()        
        
        
    if opcao == 4:
        arquivo_motorista = open("motorista", "r")

        for i in arquivo_motorista.readlines():
            lista_motorista.append(i)
        
        print(lista_motorista)
        arquivo_motorista.close()
        
    if opcao == 5:
        
        arquivo_funcionario = open("funcionario", "r")

        for i in arquivo_funcionario.readlines():
            lista_funcionario.append(i)
        
        print(lista_funcionario)
        arquivo_funcionario.close()

    if opcao == 6:
        arquivo_veiculo = open("veiculo", "r")

        for i in arquivo_veiculo.readlines():
            lista_veiculo.append(i)
        
        print(lista_veiculo)
        arquivo_veiculo.close()
        
    if opcao == 7:
        arquivo_produtor = open("produtor", "r")

        for i in arquivo_produtor.readlines():
            lista_produtor.append(i)
        
        print(lista_produtor)
        arquivo_produtor.close()
    
    if opcao == 8:
        arquivo_propriedade = open("propriedade", "r")

        for i in arquivo_propriedade.readlines():
            lista_propriedade.append(i)
        
        print(lista_propriedade)
        arquivo_propriedade.close()
        
    
    if opcao == 9:
        arquivo_servico = open("servico", "r")
        cont = 0
        for i in arquivo_servico.readlines():
            lista_servico.append(i)
        
        print(lista_servico)
        arquivo_servico.close()

    if opcao == 0:
        print("Até logo.......")
        exit()