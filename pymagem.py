# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Alex dos Santos Nascimento
    NUSP: 14612990

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

#-------------------------------------------------------------------------- 

class Pymagem:
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # complete os métodos __init__ e __str__ da classe Pymagem 

    def __init__(self, nlins, ncols, valor=0):
        ''' (Pymagem, int, int, obj) 

        Construtor da classe Pymagem, que recebe dois inteiros 
        nlins > 0 e ncols > 0 e um valor. Cria e carrega uma matriz 
        (lista de listas) de dimensão nlins x ncols com valor em 
        cada posição.

        Exemplos:
        >>> t = Pymagem(3,4,-1)
        >>> print(t)
        -1, -1, -1, -1
        -1, -1, -1, -1
        -1, -1, -1, -1
        >>> tt = Pymagem(2, 3, (110, 122))
        >>> tt
        (110, 122), (110, 122), (110, 122)
        (110, 122), (110, 122), (110, 122)
        >>> 
        '''
        # o atributo data é obrigatório
        # carregue a matriz em self.data
        self.data = [[valor for i in range(ncols)] for j in range(nlins)]
        # complete o método com seu código para criar a matriz
        self.nlins = nlins
        self.ncols = ncols
        self.valor = valor
    #--------------------------------------------------------------------------        

    def __str__(self):
        ''' (Pymagem) -> str
        retorna uma string que corresponde ao conteúdo da Pymagem.
        Esse método é chamada pela função `print()` do Python.
        Utilize print() para mostrar o conteúdo de Imagens de
        pequenas dimensões para ajudar você a depurar o seu programa.
        '''

        # substitua a linha abaixo com seu código
        matriz_str = ""
        for linha in self.data:
            linha_str = ", ".join(map(str, linha))
            matriz_str += linha_str + "\n"
        return matriz_str
    #--------------------------------------------------------------------------
    # escreva os demais métodos aqui
    def __add__(self, other):

        soma = []
        for L in range(self.nlins):
            linha_soma = []
            for C in range(self.ncols):
                r = self.data[L][C] + other.data[L][C]
                linha_soma.append(r)
            soma.append(linha_soma)

        return Pymagem(self.nlins, self.ncols, r)


    def __mul__(self, other):

        mul = []
        for L in range(self.nlins):
            linha_mul = []
            for C in range(self.ncols):
                r = self.data[L][C] * other
                linha_mul.append(r)
            mul.append(linha_mul)

        return Pymagem(self.nlins, self.ncols, r)

    def size(self):

        return self.nlins, self.ncols

    def get(self, lin, col):

        return self.data[lin][col]

    def put(self, lin, col, valor):

        self.data[lin][col] = valor

        return "PUT utilizado"

    def crop(self, E=0, S=0, D=None, I=None):

        '''
        Testa se E e S foram especificados ou são menor que 0
        '''
        if D is None or D > self.nlins:
            D = self.nlins + 1 #Precisa do +1 se não é retornado um elemento a menos
        if I is None or I > self.ncols:
            I = self.ncols

        '''
        Testa se E e S foram especificados ou são menor que 0
        '''
        if E < 0:
            E = 0
        if S < 0:
            S = 0

        cropped_data = []
        '''
         Laço que cria uma nova matriz usando a coluna S (Sup. Esquerdo) e I (Inf. Direito) 
         como referência de recorte
        '''
        for i in range(S, I):
            row = self.data[i][E:D]
            cropped_data.append(row)

        return Pymagem(len(cropped_data), len(cropped_data[0]), valor=self.valor)

    # NECESSÁRIO CORREÇÃO
    def paste(self, fonte, X, Y):
        '''
            Método que sobrepõe a matriz criada em crop em outra matriz, levando em consideração o deslocamento.
        '''
        for i in range(fonte.nlins):
            for j in range(fonte.ncols):
                if 0 <= i + X < self.nlins and 0 <= j + Y < self.ncols:
                    self.data[i + X][j + Y] = fonte.data[i][j]
