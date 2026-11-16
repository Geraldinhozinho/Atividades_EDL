




class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, instancia):
        novo_no = instancia

        novo_no.proximo = self.topo
        self.topo = novo_no

    def desempilhar(self):
        if self.topo is None:
            return None

        removido = self.topo
        self.topo = self.topo.proximo

        return removido.valor

    def ver_topo(self):
        if self.topo is None:
            return None

        return self.topo.valor

    def esta_vazia(self):
        return self.topo is None

    def tamanho(self):
        atual = self.topo
        contador = 0

        while atual is not None:
            contador += 1
            atual = atual.proximo

        return contador

    def listar(self):
        atual = self.topo

        while atual is not None:
            print(atual.valor)
            atual = atual.proximo
