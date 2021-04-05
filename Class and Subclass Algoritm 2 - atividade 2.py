
'''''1)Construa um algoritmo para implementar a 
classe Aluno que contém os atributos código, 
nome e matrícula. 

2) A classe Aluno possui duas subclasses, 
sendo a classe AlunoEnsinoMedio, que tem 
o atributo ano como seu atributo próprio

3)e a classe AlunoGraduacao que tem o atributo semestre como atributo próprio. 
As duas subclasses herdam todos atributos da classe Aluno. 
As três classes possuem o método construtor e também o método imprimir, 
que imprime na tela os valores de todos os atributos da sua respectiva classe.'''


class Aluno:
    def _init_(self, codigo, nome, matricula):
        self.nome = nome
        self.codigo = codigo
        self.matricula = matricula

    def imprimir(self):
        print ("nome:", self.nome)
        print ("codigo:", self.codigo)
        print ("matricula:", self.matricula)
        
class AlunoEnsinoMedio:
    def _init_(self, codigo, nome, matricula ,ano):
        Aluno._init_(self, codigo, nome, matricula)
        self.ano = ano
    
    def imprimir(self):
        print ("nome:", self.nome)
        print ("codigo:", self.codigo)
        print ("matricula:", self.matricula)
        print ("ano:", self.ano)

class AlunoGraduacao
    def _init_(self, codigo, nome, matricula, semestre):
        Aluno._init_(self, codigo, nome, matricula)
        self.semestre = semestre
        
    def imprimir(self):
        print ("nome:", self.nome)
        print ("codigo:", self.codigo)
        print ("matricula:", self.matricula)
        print ("semestre:", self.semestre)
        
        
        
        
        
        