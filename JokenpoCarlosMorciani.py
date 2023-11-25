from random import randint
import time

partida = True
jogadas = ('Pedra' , 'Papel', 'Tesoura')
resultados = ('Empate', 'Vitória', 'Derrota')
modalidades = (' 0: Humano x Computador',' 1: Humano x Humano' , ' 2: Computador x Computador')
vitoria = 0
derrota = 0
empate = 0

##Tela Inicial

print('Jokenpô')
print('Opções de jogo:\n0:Humano x Computador\n1:Humano x Humano\n2:Computador x Computador')
escolha = int(input('Digite a opção desejada:'))
print('Você escolheu => {}'.format(modalidades[escolha]))

while partida:
    ##Humano x Computador

    if escolha == 0:
        #Jogador
        print('0:Pedra   1:Papel   2:Tesoura')
        jogador = int(input('Qual a sua jogada?'))
        print('Você jogou:{}'.format(jogadas[jogador]))
        time.sleep(0.9)

        #Computador
        computador = randint(0,2)
        print('Computador jogou:{}'.format(jogadas[computador]))
        time.sleep(0.9)

        #Vitória/Derrota/Empate
        resul_joga = (jogador - computador) % 3
        if resul_joga == 0:
            empate = empate + 1
            print('Deu empate!!')
            print('Jogador:', vitoria, '--Computador:', derrota, '--Empate:', empate)

            #Reinicio da partida
            reinicio = input('Você deseja continuar jogando (continuar/sair):')
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Jogador:', vitoria, '--Computador:', derrota, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False

        elif resul_joga == 2:
            derrota = derrota + 1
            print('O computador ganhou!!')
            print('Jogador:', vitoria, 'Computador:', derrota, 'Empate:', empate)
            reinicio = input('Você deseja continuar jogando (continuar/sair):')

            # Reinicio da partida
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Jogador:', vitoria, '--Computador:', derrota, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False
        else:
            vitoria = vitoria + 1
            print('Você ganhou!!')
            print('Jogador:', vitoria, 'Computador:', derrota, 'Empate:', empate)
            reinicio = input('Você deseja continuar jogando (continuar/sair):')

            # Reinicio da partida
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Jogador:', vitoria, '--Computador:', derrota, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False
        time.sleep(0.9)


    ##Humano x Humano

    if escolha == 1:
        #Jogador
        print('0:Pedra   1:Papel   2:Tesoura')
        jogador = int(input('Qual a sua jogada?'))
        print('Jogador Um:{}'.format(jogadas[jogador]))
        time.sleep(0.9)

        # Jogador2
        jogador2 = int(input('Qual a sua jogada?'))
        print('Jogador Dois:{}'.format(jogadas[jogador2]))
        time.sleep(0.9)

        # Vitória/Derrota/Empate
        resul_joga = (jogador - jogador2) % 3
        if resul_joga == 0:
            empate = empate + 1
            print('Deu empate!!')
            print('Jogador Um:', vitoria, '--Jogador Dois:', derrota, '--Empate:', empate)

            # Reinicio da partida
            reinicio = input('Você deseja continuar jogando (continuar/sair):')
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Jogador Um:', vitoria, '--Jogador Dois:', derrota, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False

        elif resul_joga == 2:
            derrota = derrota + 1
            print('O Jogador Dois ganhou!!')
            print('Jogador Um:', vitoria, '--Jogador Dois:', derrota, '--Empate:', empate)

            # Reinicio da partida
            reinicio = input('Você deseja continuar jogando (continuar/sair):')
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Jogador Um:', vitoria, '--Jogador Dois:', derrota, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False
        else:
            vitoria = vitoria + 1
            print('Jogador Um ganhou!!')
            print('Jogador Um:', vitoria, '--Jogador Dois:', derrota, '--Empate:', empate)

            # Reinicio da partida
            reinicio = input('Você deseja continuar jogando (continuar/sair):')
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Jogador Um:', vitoria, '--Jogador Dois:', derrota, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False
        time.sleep(0.9)

        ##Computador x Computador

    if escolha == 2:

        # Computador
        computador = randint(0, 2)
        print('Computador Um:{}'.format(jogadas[computador]))
        time.sleep(0.9)

        # Computador2
        computador2 = randint(0, 2)
        print('Computador Dois:{}'.format(jogadas[computador2]))
        time.sleep(0.9)

        # Vitória/Derrota/Empate
        resul_joga = (computador2 - computador) % 3
        if resul_joga == 0:
            empate = empate + 1
            print('Deu empate!!')
            print('Computador Um:', derrota, '--Computador Dois:', vitoria, '--Empate:', empate)

            # Reinicio da partida
            reinicio = input('Você deseja continuar jogando (continuar/sair):')
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Computador Um:', derrota, '--Computador Dois:', vitoria, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False

        elif resul_joga == 2:
            derrota = derrota + 1
            print('O computador Um ganhou!!')
            print('Computador Um:', derrota, 'Computador Dois:', vitoria, 'Empate:', empate)

            # Reinicio da partida
            reinicio = input('Você deseja continuar jogando (continuar/sair):')
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Computador Um:', derrota, '--Computador Dois:', vitoria, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False
        else:
            vitoria = vitoria + 1
            print('Computador Dois ganhou!!')
            print('Computador Um:', derrota, 'Computador Dois:', vitoria, 'Empate:', empate)

            # Reinicio da partida
            reinicio = input('Você deseja continuar jogando (continuar/sair):')
            if reinicio == 'continuar':
                print('Você escolheu jogar novamente'.format(partida))
            elif reinicio == 'sair':
                print('PLACAR FINAL:', 'Computador Um:', derrota, '--Computador Dois:', vitoria, '--Empate:', empate)
                print('Muito obrigado por jogar.\nCriado por: Carlos E.N.Morciani')
                partida = False
            else:
                reinicio != 'continuar' or 'sair'
                print('Texto Inválido')
                partida = False
        time.sleep(0.9)

