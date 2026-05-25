#Testes para a Lista de Compras.

import pytest
from Compras import *
def test_criar_item():
    #Testar a função de criar um novo item
    item = novo_item("Monster", 3, 9.99, 15.99, 2)
    assert item.getName == "Monster"
    assert item.getPriority == "Alta"
    assert item.getMin == 9.99
    assert item.getMax == 15.99
    assert item.getAmount == 2

def test_listar_itens():
    #Testar a função de listar os itens
    novo_item("Detergente", 2, 2.50, 3.99, 3)
    novo_item("Desinfetante", 1, 1.99, 8.99, 1)
    itens = listar_itens()
    assert len(itens) == 2

def test_atualizar_item():
    #Testar a função de atualizar um item
    item = novo_item("RedBull", 3, 7.99, 9.99, 2)
    atualizar_item(item.getID(), nome = "Monster", min = 8.99, max = 15.99)
    assert item.getName() == "Monster"
    assert item.getMin() == 8.99
    assert item.getMax() == 15.99

def test_deletar_item():
    #Testar a função de apagar algum item
    item = novo_item("Palito de Fosfóro", 1, 1.50, 2.99, 1)
    deletar_item(item.getID())
    itens = listar_itens()
    assert len(itens) == 0

