x = 0
y = 0
angulo = 0

flag = 1
controle = True

while flag == 1:
    #Abro o arquivo no começo do laço para caso queira fazer um novo teste ele vai reabrir o arquivo para pegar os novos comandos
    arquivo = open('entrada.txt', 'r')
    texto = arquivo.read()
    arquivo.close

    #Vejo se o tamanho da sala vai ser menor ou igual a 0, caso seja, inserir um valor válido
    while controle:
        largura = int(input('Largura da sala: '))
        comprimento = int(input('Comprimento: '))
        if largura <= 0 or comprimento <= 0:
            print("Dimensão inválida")
            break

        for palavras in texto:
            if palavras == 'F':
                if angulo == 0:
                    if y < comprimento:
                        y = y + 1
                elif angulo == 90:
                    if x < largura:
                        x = x + 1
                elif angulo == 180:
                    y = y - 1
                    if y < 0:
                        y = 0
                elif angulo == 270:
                    x = x - 1
                    if x < 0:
                        x = 0

            elif palavras == 'D':
                if angulo == 270:
                    angulo = 0
                else:
                    angulo = angulo + 90

            elif palavras == 'T':
                if angulo == 0:
                    y = y - 1
                    if y < 0:
                        y = 0
                elif angulo == 90:
                    x = x - 1
                    if x < 0:
                        x = 0
                elif angulo == 180:
                    if y < comprimento:
                        y = y + 1

                elif angulo == 270:
                    if x < largura:
                        x = x + 1
                    
            elif palavras == 'E':
                if angulo == 0:
                    angulo = 270
                else:
                    angulo = angulo - 90
            
        if angulo == 0:
                print("N", x, y)

        elif angulo == 90:
                print("L", x, y)

        elif angulo == 180:
                print("S", x, y)

        elif angulo == 270:
                print("O", x, y)

        x = 0
        y = 0
        angulo = 0
    
    
        print('Novo teste?  1.Sim  2.Nao')
        flag = int(input())
        if flag != 1:
            controle = False
