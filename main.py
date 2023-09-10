from pymagem import Pymagem


def main():
    ## Testes da classe pymage

    print("\nMATRIZ TT")
    print("Teste str 1")
    tt = Pymagem(2, 3, (110, 122))
    print(tt)

    print("Teste size 1: Mostra a dimenção da matriz")
    size = tt.size()
    print(size)

    print("\nTeste GET: Retorna o valor do elemento linha x coluna")
    get = tt.get(0, 0)
    print(get)

    print("\nMATRIZ T")
    print("\nTeste str 2")
    t = Pymagem(3, 4, -1)
    print(t)

    print("\nTeste GET: Retorna o valor do elemento linha x coluna")
    get = t.get(2, 2)
    print(get)

    print("\nTeste PUT: Atualiza o valor do elemento linha x coluna")
    put = t.put(2, 2, 5)
    print(put)

    print("\nTeste GET: Retorna o valor do elemento linha x coluna")
    get = t.get(2, 2)
    print(get)

    print("\nTeste str 2")
    t = Pymagem(3, 4, -1)
    print(t)

    print("\nTeste size : Mostra a dimenção da matriz")
    size = t.size()
    print(size)

    print("\nTESTES DO EXERCICIO")
    img1 = Pymagem(6, 8, 111)
    print("\nteste atributo data de img1 - uma lista de listas")
    print(img1.data)

    img2 = Pymagem(6, 8, 222)
    print("\nTeste do str img2 -- uma imagem ou matriz")
    print(img2)

    img3 = img1.crop(2, 3, 7, 6)
    print("\nteste crop de img1:")
    print(img3)

    print("\ncrop não altera img1:")
    print(img1)

    img2.paste(img3, -1, 2)
    print("\nteste paste em img2:")
    print(img2)

    img4 = img1 + img2
    print("\nteste __add__:")
    print(img4)

    img5 = img1 * 0.3
    print("\nteste __mul__:")
    print(img5)

    img6 = img5 + img2 * -1.5
    print("\nteste __add__ e __mul__ :")
    print(img6)

if __name__ == "__main__":
    main()