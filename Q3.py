


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista_encadeada_circular:
    def __init__(self):
        self.inicio_lista = None

    def inserir(self, instancia):
        novo_no = instancia
        if self.inicio_lista is None:
            self.inicio_lista = novo_no
            novo_no.proximo = novo_no
        else:
            atual = self.inicio_lista
            while atual.proximo != self.inicio_lista:
                atual = atual.proximo
            novo_no.proximo = self.inicio_lista
            atual.proximo = novo_no
            self.inicio_lista = novo_no
    
    def remover(self, valor):
        if self.inicio_lista is None:
            return False

        atual = self.inicio_lista
        anterior = None
        while True:
            if atual.valor == valor:
                if atual.proximo == atual:
                    self.inicio_lista = None
                elif atual == self.inicio_lista:
                    ultimo = self.inicio_lista
                    while ultimo.proximo != self.inicio_lista:
                        ultimo = ultimo.proximo
                    self.inicio_lista = atual.proximo
                    ultimo.proximo = self.inicio_lista
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
            if atual == self.inicio_lista:
                break
        return False

    def buscar(self, valor):
        if self.inicio_lista is None:
            return False

        atual = self.inicio_lista
        while True:
            if atual.valor == valor:
                return True
            atual = atual.proximo
            if atual == self.inicio_lista:
                break
        return False
       
    def listar(self):
        if self.inicio_lista is None:
            return False
        atual = self.inicio_lista
        while True:
            print(atual.valor, end=' - ')
            atual = atual.proximo
            if atual == self.inicio_lista:
                break

A1 = Node(10)
A2 = Node(20)
A3 = Node(30)
A4 = Node(40)

B1 = Lista_encadeada_circular()
B1.inserir(A1)
B1.inserir(A2)
B1.inserir(A3)

B1.remover(30)

print(B1.buscar(30))

B1.listar()

# def inserir_inicio(self, instancia):
#     novo_no = instancia

#     if self.inicio_lista is None:
#         self.inicio_lista = novo_no
#         novo_no.proximo = novo_no
#     else:
#         atual = self.inicio_lista

#         # Encontrar o último nó
#         while atual.proximo != self.inicio_lista:
#             atual = atual.proximo

#         novo_no.proximo = self.inicio_lista
#         atual.proximo = novo_no
#         self.inicio_lista = novo_no


# def inserir_final(self, instancia):
#     novo_no = instancia

#     if self.inicio_lista is None:
#         self.inicio_lista = novo_no
#         novo_no.proximo = novo_no
#     else:
#         atual = self.inicio_lista

#         # Encontrar o último nó
#         while atual.proximo != self.inicio_lista:
#             atual = atual.proximo

#         novo_no.proximo = self.inicio_lista
#         atual.proximo = novo_no