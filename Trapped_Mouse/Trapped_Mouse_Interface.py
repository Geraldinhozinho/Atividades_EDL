




import pygame

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
                        
arquivo = 'Trapped_Mouse/Mapa.txt'
with open(arquivo, 'r') as mapa:
    linhas_mapa = mapa.readlines()
    
    linhas_limpas = []
    for linha in linhas_mapa:
        linhas_limpas.append(list(linha.strip())) 
        
    linhas_mapa = linhas_limpas
    
    altura = len(linhas_mapa) + 2
    largura = len(linhas_mapa[0]) + 2

parede = ['1'] * (largura)
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

tamanho_celula = 25
acrescimo_altura = altura * 5
acrescimo_largura = largura * 5

altura_tela = (altura  * tamanho_celula) + acrescimo_altura
largura_tela = (largura * tamanho_celula) + acrescimo_largura 

x = 0
y = 0
cont = 0

imagem_rato = pygame.image.load('Trapped_Mouse/rato.png')
imagem_rato = pygame.transform.scale(imagem_rato, (tamanho_celula, tamanho_celula))

pygame.init()
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura_tela, altura_tela))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False  
            
    for linha in range(len(maze) -1, -1, -1):
        for coluna in range(len(maze[linha])):
            if maze[linha][coluna] == '1':
                pygame.draw.rect(tela, (104, 34, 139), (x, y, tamanho_celula, tamanho_celula))
                x = x + 30
            elif maze[linha][coluna] == 'E':
                pygame.draw.rect(tela, (255, 255, 0), (x, y, tamanho_celula, tamanho_celula))
                x = x + 30    
            elif visitados[linha][coluna] == True:
                pygame.draw.rect(tela, (49, 79, 79), (coluna * 30, (len(maze) - 1 - linha) * 30, tamanho_celula, tamanho_celula))
                x = x + 30
            elif maze[linha][coluna] == '0':
                pygame.draw.rect(tela, (224, 255, 255), (x, y, tamanho_celula, tamanho_celula))
                x = x + 30
            elif maze[linha][coluna] == 'M':
                pygame.draw.rect(tela, (224, 255, 255), (x, y, tamanho_celula, tamanho_celula))
                x = x + 30
        x = 0
        y = y + 30    
             
    pygame.draw.rect(tela, (0, 255, 0), (coluna_atual * 30, (len(maze) - 1 - linha_atual) * 30, tamanho_celula, tamanho_celula))
    tela.blit(imagem_rato, (coluna_atual * 30, (len(maze) - 1 - linha_atual) * 30))
    pygame.display.update() 
    
    if maze[linha_atual][coluna_atual] == 'E':
        relogio.tick(0.5)
        break
        
    pilha_disponiveis = Verificar_Caminhos(linha_atual, coluna_atual)
    if pilha_disponiveis.topo_pilha is not None:
        posicao = pilha_disponiveis.Remover()

        linha_atual = posicao.valor[0]
        coluna_atual = posicao.valor[1]
        
        visitados[linha_atual][coluna_atual] = True

        pilha_caminho.Inserir(Node((linha_atual, coluna_atual)))
    else:
        posicao = pilha_caminho.Remover()

        if pilha_caminho.topo_pilha is not None:
            linha_atual = pilha_caminho.topo_pilha.valor[0]
            coluna_atual = pilha_caminho.topo_pilha.valor[1]
        else:
            break      
    if cont == 0:
        relogio.tick(0.8)
        cont = 1
    else:
        relogio.tick(10)
pygame.quit()

print("Caminho encontrado:")
pilha_caminho.Mostrar_pilha() 