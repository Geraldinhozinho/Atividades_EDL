


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista_encadeada_simples:
    def __init__(self):
        self.inicio_lista = None

    def inserir_inicio(self, instancia):
        novo_no = instancia
        if self.inicio_lista == None:
            self.inicio_lista = novo_no
        else:
            novo_no.proximo = self.inicio_lista
            self.inicio_lista = novo_no

    def inserir_final(self, instancia):
        novo_no = instancia
        if self.inicio_lista == None:
            self.inicio_lista = novo_no
        else:
            atual = self.inicio_lista
            while atual.proximo is not None:
                atual = atual.proximo
        atual.proximo = novo_no

    def buscar(self, valor):
        atual = self.inicio_lista

        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def remover(self, valor):
        atual = self.inicio_lista
        anterior = None
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.inicio_lista = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar(self):
        atual = self.inicio_lista
        while atual is not None:
            print(atual.valor, end=" - ")
            atual = atual.proximo




A1 = Node(10)
A2 = Node(20)
A3 = Node(30)
A4 = Node(40)

B1 = Lista_encadeada_simples()
B1.inserir_inicio(A1)
B1.inserir_inicio(A2)
B1.inserir_inicio(A3)

B1.inserir_final(A4)

B1.remover(40)

print(B1.buscar(30))

B1.listar()

