



class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio_fila = None
        self.fim_fila = None

    def enfileirar(self, instancia):
        novo_no = instancia

        if self.inicio_fila is None:
            self.inicio_fila = novo_no
            self.fim_fila = novo_no
        else:
            self.fim_fila.proximo = novo_no
            self.fim_fila = novo_no

    def desenfileirar(self):
        if self.inicio_fila is None:
            return None

        removido = self.inicio_fila
        self.inicio_fila = self.inicio_fila.proximo

        if self.inicio_fila is None:
            self.fim_fila = None

        return removido.valor

    def espiar(self):
        if self.inicio_fila is None:
            return None

        return self.inicio_fila.valor

    def esta_vazia(self):
        return self.inicio_fila is None

    def tamanho(self):
        atual = self.inicio_fila
        contador = 0
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador

    def listar(self):
        atual = self.inicio_fila

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo
