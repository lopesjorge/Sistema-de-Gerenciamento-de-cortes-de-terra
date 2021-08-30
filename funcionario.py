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
         
         
            
            
