"""
Sistema para uma lista de compras
os itens possuem:
1. Id (Gerado automaticamente)
2. Nome (Atribuido)
3. Prioridade (Nível de prioridade de compra)
4. Preço mínimo (Preço mínimo que se espera do produto)
5. Preço máximo (Preço máximo que se espera do produto)
6. Quantidade (Quantidade do produto a ser comprado)
7. Peso (Peso do produto a ser comprado)
"""

class Item:
    #ID pra classe item
    ID = 0
    #Função para iniciar o item
    def __init__(self, name: str, priority: int, min: float, max: float, amount = 1, weight = 0):
        #Atribuir ID e acrescer pros próximos
        self.__id = Item.ID
        Item.ID += 1
        #Manejar a informação atráves de verificações e atribuições
        self.__name = name
        self.__priority = "Alta" if priority >= 3 else "Baixa" if priority <= 1 else "Média"
        if(min < max): self.__min = min
        else: self.__min = max
        if(max > min): self.__max = max
        else: self.__max = min
        self.__amount = amount
        self.__weight = weight
    #Função para modificar algum valor
    def setter(self, name = None, priority = None, min = None, max = None, amount = None, weight = None):
        #Verificar se os valores foram repassados e quais foram, se forem repassados, modifica-los no item.
        if(name): self.name = name
        if(priority): self.__priority = "Alta" if priority >= 3 else "Baixa" if priority <= 1 else "Média"
        if(min and min > 0 and min < self.__max and min <= max): self.__min = min
        if(max and max > 0 and max > self.__min and max >= min): self.__max = max
        if(amount): self.__amount = amount
        if(weight): self.__weight = weight

    #Funções para retornar as informações do item
    def getID(self) -> int:
        return self.__id
    
    def getName(self) -> str:
        return self.__name
    
    def getPriority(self) -> str:
        return self.__priority
    
    def getMin(self) -> float:
        return self.__min
    
    def getMax(self) -> float:
        return self.__max
    
    def getAmount(self) -> int:
        return self.__amount
    
    def getWeight(self) -> int:
        return self.__weight
    
    #Função para representar o produto como uma String
    def __str__(self):
        return f'{self.__id} - {self.__amount * self.__weight 
                              if self.__amount > 0 and self.__weight > 0 
                              else self.__amount if self.__amount > 0 
                              else self.__weight if self.__weight > 0 
                              else 1}{self.name}({self.__priority}) {self.__min}-{self.__max}'

lista = []
#Criar novo item, recebe as informações necessárias e retornará o nova instância do produto criado
def novo_item(nome, priority, min, max, amount = 1, weight = 0) -> Item:
    #Cria uma nova instância de Item com as informações repassadas
    novo = Item(nome, priority, min, max, amount, weight)
    #Adiciona na lista de compras
    lista.append(novo)
    #Retorna o novo produto
    return novo
#Mostrar a lista de itens
def listar_itens() -> list:
    #Mostrar cada item da lista
    for item in lista:
        print(item)
    #Retorna a lista de produtos
    return lista
#Modificar algum item da lista
def atualizar_item(id, nome = None, priority = None, min = None, max = None, amount = None, weight = None):
    for item in lista:
        #Verifica se o id é correspondente
        if item.getID() == id:
            #Chama o setter para modificar com base nas informações recebidas
            item.setter(nome, priority, min, max, amount, weight)
            #Retorna o item modificado
            return item
    #Se não achar o item na lista, não retorna nada
    return None
#Apagar item da lista
def deletar_item(id):
    #Reescreve a lista sem o item
    lista = [item for item in lista if item.getID() != id]