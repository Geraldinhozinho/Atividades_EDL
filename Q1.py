


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, instancia):
        novo_no = instancia

        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no

    def inserir_final(self, instancia):
        novo_no = instancia

        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no

   
    def remover_inicio(self):
        if self.inicio is None:
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        else:
            self.inicio.anterior = None
        return removido.valor

    def remover_final(self):
        if self.fim is None:
            return None
        removido = self.fim
        self.fim = self.fim.anterior
        if self.fim is None:
            self.inicio = None
        else:
            self.fim.proximo = None
        return removido.valor

    def espiar_inicio(self):
        if self.inicio is None:
            return None

        return self.inicio.valor

    def espiar_final(self):
        if self.fim is None:
            return None

        return self.fim.valor

    def esta_vazio(self):
        return self.inicio is None

    def tamanho(self):
        atual = self.inicio
        contador = 0

        while atual is not None:
            contador += 1
            atual = atual.proximo

        return contador

    def listar(self):
        atual = self.inicio

        while atual is not None:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo

        print("None")
