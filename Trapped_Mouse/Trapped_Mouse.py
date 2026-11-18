






import time
import os

class Node:
    def __init__(self, valor, ):
        self.valor = valor
        self.proximo_no = None
        
class Pilha:
    def __init__(self):
        self.topo_pilha = None
    
    def Inserir(self, instancia):
        if self.topo_pilha == None:
            self.topo_pilha = instancia
        else:
            novo_no = instancia
            novo_no.proximo_no = self.topo_pilha
            self.topo_pilha = novo_no
    
    def Remover(self):
        if self.topo_pilha is None:
            print("Pilha vazia")
        else:
            item_removido = self.topo_pilha
            self.topo_pilha = self.topo_pilha.proximo_no
            return item_removido
        
    def Mostrar_pilha(self):
            atual = self.topo_pilha
            if atual:   
                while atual is not None:
                    print(atual.valor)
                    atual = atual.proximo_no
            else:
                print("Sem itens na Pilha para listar")   
    
def Verificar_Caminhos(linha, coluna):
    pilha_disponiveis = Pilha()
    # BAIXO
    if (maze[linha + 1][coluna] == '0' or maze[linha + 1][coluna] == 'E') and visitados[linha + 1][coluna] == False:
        pilha_disponiveis.Inserir(Node((linha + 1, coluna)))
    # CIMA
    if (maze[linha - 1][coluna] == '0' or maze[linha - 1][coluna] == 'E') and visitados[linha - 1][coluna] == False:
        pilha_disponiveis.Inserir(Node((linha - 1, coluna)))
    # ESQUERDA
    if (maze[linha][coluna - 1] == '0' or maze[linha][coluna - 1] == 'E') and visitados[linha][coluna - 1] == False:
        pilha_disponiveis.Inserir(Node((linha, coluna - 1)))
    # DIREITA
    if (maze[linha][coluna + 1] == '0' or maze[linha][coluna + 1] == 'E') and visitados[linha][coluna + 1] == False:
        pilha_disponiveis.Inserir(Node((linha, coluna + 1)))
    return pilha_disponiveis    

def Encontrar_Rato():
    for linha in range(len(maze)):
        for coluna in range(len(maze[linha])):
            if maze[linha][coluna] == 'M':
                return linha, coluna
    return None

def Mostrar_Maze(linha_rato, coluna_rato):
    for linha in range(len(maze) - 1, -1, -1):
        texto = ""
        for coluna in range(len(maze[linha])):
            if linha == linha_rato and coluna == coluna_rato:
                texto = texto + "\033[1;32;42m M \033[0m"
            elif maze[linha][coluna] == "1":
                texto = texto + "\033[1;37;47m 1 \033[0m"
            elif maze[linha][coluna] == "E":
                texto = texto + "\033[1;33;43m E \033[0m"
            elif visitados[linha][coluna] == True:
                texto = texto + "\033[1;32;46m . \033[0m"           
            elif maze[linha][coluna] == "0":
                texto = texto + "\033[1;30;40m 0 \033[0m"           
            elif maze[linha][coluna] == "M":
                texto = texto + "\033[1;30;40m 0 \033[0m"        
        print(texto)   
                        
arquivo = 'Trapped_Mouse/Mapa.txt'
with open(arquivo, 'r') as mapa:
    linhas_mapa = mapa.readlines()
    
    linhas_limpas = []
    for linha in linhas_mapa:
        linhas_limpas.append(list(linha.strip())) 
        
    linhas_mapa = linhas_limpas
    
    altura = len(linhas_mapa)
    largura = len(linhas_mapa[0])
    
parede = ['1'] * (largura + 2)
matriz = linhas_mapa

pilha = Pilha()
for linha in matriz:
    linha.insert(0, '1')
    linha.append('1')
    pilha.Inserir(Node(linha))
    
maze = []    
maze.append(parede)
while pilha.topo_pilha is not None:
    linha = pilha.Remover()
    maze.append(linha.valor)
maze.append(parede)

visitados = []
for linha in maze:
    visitados.append([False] * len(linha))

posicao_rato = Encontrar_Rato()
if posicao_rato is None:
    print("\033[1;31mNão tem Rato no mapa\033[m")
    exit()
linha_atual, coluna_atual = posicao_rato

pilha_caminho = Pilha()
pilha_caminho.Inserir(Node((linha_atual, coluna_atual)))
visitados[linha_atual][coluna_atual] = True
cont = 0
while True:
    if maze[linha_atual][coluna_atual] == 'E':
        break
    
    pilha_disponiveis = Verificar_Caminhos(linha_atual, coluna_atual)
    
    if cont == 0:
        Mostrar_Maze(linha_atual, coluna_atual)
        time.sleep(1)
        cont = 1
    if pilha_disponiveis.topo_pilha is not None:
        
        posicao = pilha_disponiveis.Remover()

        linha_atual = posicao.valor[0]
        coluna_atual = posicao.valor[1]

        os.system('cls')
        Mostrar_Maze(linha_atual, coluna_atual)
        time.sleep(0.2)
        
        visitados[linha_atual][coluna_atual] = True

        pilha_caminho.Inserir(Node((linha_atual, coluna_atual)))
    else:
        posicao = pilha_caminho.Remover()

        if pilha_caminho.topo_pilha is not None:
            linha_atual = pilha_caminho.topo_pilha.valor[0]
            coluna_atual = pilha_caminho.topo_pilha.valor[1]

            os.system('cls')
            Mostrar_Maze(linha_atual, coluna_atual)
            time.sleep(0.2)
        else:
            break
print("Caminho encontrado:")
pilha_caminho.Mostrar_pilha()