import os
import time


eleitores = []
cpfeleitores = []
branco = [0,0,0]
nulo = [0,0,0]
votostotais = [0]
vencedores = []
eleiçãoam = []
continuar = ""
candidatosprefeitura = []
candidatosgovernador = []
candidatospresidencia = []


def decidir():
    continuar = input("Quer continuar? Sim ou Não ")
    if continuar == "Sim" or continuar == "Não":
        return (continuar)
    else:
        print("Não entendi, tente novamente!")
        decidir()


def apagarterminal():
    os.system('cls')
    time.sleep(0.8)


def cdtcandidatos():
    apagarterminal()
    nome = input("Coloque o nome do candidato: ")
    cargo = input("Coloque o cargo do candidato: ")
    num = input("Coloque o número do candidato: ")
    partido = input("Coloque o partido do candidato: ")
    candidato = [nome, partido, num, cargo,0]
    if cargo == "Presidente":
        candidatospresidencia.append(candidato)
    elif cargo == "Prefeito":
        candidatosprefeitura.append(candidato)
    elif cargo == "Governador":
        candidatosgovernador.append(candidato)
    elif cargo != "Presidente" and cargo != "Governador" and cargo != "Prefeito":
        print("O cargo desse candidato não é aceito! Tente novamente!")
    if decidir() == "Sim":
        cdtcandidatos()
    else:
     menu()
    return


def cdteleitores():
    apagarterminal()
    nome = input("Coloque o nome do eleitor: ")
    cpf = input("Coloque o CPF do eleitor: ")
    y = cpfeleitores.count(cpf)
    if y == 1:
        print("Já existe um cadastro nesse CPF! Tente novamente!!")
        cdteleitores()
    else:
        cpfeleitores.append(cpf)
        eleitores.append(nome)
        if decidir() == "Sim":
            cdteleitores()
        else:
         menu()
    return


    
    
def votaçãopres():
     apagarterminal()
     a = True
     numeropres = input("Coloque o Numero do seu candidato para Presidente: ")
     if numeropres == '-1':
         a = False
         confvoto = input("Deseja eleição branco? ")
         if confvoto == 'Sim':
             print("Seu voto foi Confirmado")
             branco[2] += 1
             votostotais[0] += 1
         if confvoto == 'Não':
             votaçãopres()
     if numeropres == '-2':
         a = False
         confvoto = input("Deseja eleição nulo? ")
         if confvoto == 'Sim':
             print("Seu voto foi Confirmado")
             nulo[2] += 1
             votostotais[0] += 1
         if confvoto == 'Não':
             votaçãopres()
     for i in range(len(candidatospresidencia)):
         if numeropres == candidatospresidencia[i][2]:
             a = False
             confvoto = input(f"Deseja eleição no candidato {candidatospresidencia[i][0]}? ")
             if confvoto == "Sim":
                 candidatospresidencia[i][4] += 1
                 votostotais[0] += 1
                 print("Seu voto foi Confirmado")
             elif confvoto == "Não":
                  votaçãopres()
             elif confvoto != "Sim" and confvoto != "Não":
                 print("tente novamente!")
                 votaçãopres()
     if a:
         print("Esse candidato não existe!")
         time.sleep(0.5)
         votaçãopres()
   
def votaçãogov() :
    apagarterminal()
    a = True
    numerogov = input("Coloque o Numero do seu candidato para Governador: ")
    if numerogov == '-1':
        a = False
        confvoto = input("Deseja eleição branco? ")
        if confvoto == 'Sim':
            print("Seu voto foi Confirmado")
            branco[1] += 1
        if confvoto == 'Não':
            votaçãogov()
    if numerogov == '-2':
        a = False
        confvoto = input("Deseja eleição nulo? ")
        if confvoto == 'Sim':
            print("Seu voto foi Confirmado")
            nulo[1] += 1
        if confvoto == 'Não':
            votaçãogov()
    for i in range(len(candidatosgovernador)):
        if numerogov == candidatosgovernador[i][2]:
            a = False
            confvoto = input(f"Deseja eleição no candidato {candidatosgovernador[i][0]}? ")
            if confvoto == "Sim":
                candidatosgovernador[i][4] += 1
                print("Seu voto foi Confirmado")
            elif confvoto == "Não":
                 votaçãogov()
            elif confvoto != "Sim" and confvoto != "Não":
                print("tente novamente!")
                votaçãogov()
    if a:
        print("Esse candidato não existe!")
        time.sleep(0.5)
        votaçãogov()    
   
    
def votaçãopref():
    apagarterminal()
    a = True
    numeropref = input("Coloque o Numero do seu candidato para Prefeito: ")
    if numeropref == '-1':
        a = False
        prefvt = input("Deseja eleição branco? ")
        if prefvt == 'Sim':
            print("Seu voto foi Confirmado")
            branco[0] += 1
        if prefvt == 'Não':
            votaçãopref()
    if numeropref == '-2':
        a = False
        prefvt = input("Deseja eleição nulo? ")
        if prefvt == 'Sim':
            print("Seu voto foi Confirmado")
            nulo[0] += 1
        if prefvt == 'Não':
            votaçãopref()
    for i in range(len(candidatosprefeitura)):
        if numeropref == candidatosprefeitura[i][2]:
            a = False
            prefvt = input(f"Deseja eleição no candidato {candidatosprefeitura[i][0]}? ")
            if prefvt == "Sim":
                candidatosprefeitura[i][4] += 1
                print("Seu voto foi Confirmado")
            elif prefvt == "Não":
                 votaçãopref()
            elif prefvt != "Sim" and prefvt != "Não":
                print("tente novamente!")
                votaçãopref()
    if a:
        print("Esse candidato não existe!")
        time.sleep(0.5)
        votaçãopref()
        
def validareleitor():
    apagarterminal()
    entradacpf = input("Coloque o CPF do Eleitor / Digite 0 para voltar ao menu: ")
    x = cpfeleitores.count(entradacpf)
    print(x)
    if x == 1:
        votaçãopref()
    elif entradacpf == "0":
        menu()
    elif x < 1:
        print("Esse eleitor não existe! Tente novamente ")
        time.sleep(2)
        validareleitor()
    return
            

        
def apuraração():
    print()
    lista1 = []
    for i in candidatosprefeitura:
        lista1.append(i[4])
    ordenar(lista1)
    lista1 = lista1[::-1]
    lista2 = []
    for i in range(len(candidatosprefeitura)):
        for j in (lista1):
            if candidatosprefeitura[i][4] == j:
                lista2.append(candidatosprefeitura[i])
    votosval = votostotais[0] - (branco[0] + nulo[0])
    vencedores.append(lista2[0])
    print('RANKING DO RESULTADO PARA PREFEITO')
    print('CANDIDATO / PARTIDO /  VOTOS / % VOTOS VÁLIDOS')
    h = 0
    for i in lista2:
        h += 1
        k = (i[4]*100)//votosval
        print(f'{h}.{i[0]} / {i[1]} / {i[4]} / {k}')
    print()
    print(f'Total de votos = {votostotais[0]}')
    y = votosval*100//(votostotais[0])
    print(f'Total de votos válidos e % = {votosval} {y}%')
    w = branco[0]*100//(votostotais[0])
    print(f'Total de brancos e % = {branco[0]} {w}%')
    z = branco[0]*100//(votostotais[0])
    print(f'Total de nulos e % = {nulo[0]} {z}%')
    print()
    lista3 = []
    for i in candidatosgovernador:
        lista3.append(i[4])
    ordenar(lista3)
    lista3 = lista3[::-1]
    lista4 = []
    for i in range(len(candidatosgovernador)):
        for j in (lista3):
            if candidatosgovernador[i][4] == j:
                lista4.append(candidatosgovernador[i])
    votosval = votostotais[0] - (branco[1] + nulo[1])
    vencedores.append(lista4[0])
    print('RANKING DO RESULTADO PARA GOVERNADOR')
    print('CANDIDATO / PARTIDO / VOTOS / % VOTOS VÁLIDOS')
    h = 0
    for i in lista4:
        h += 1
        k = (i[4]*100)//votosval
        print(f'{h}.{i[0]} / {i[1]} / {i[4]} / {k}')
    print()
    print(f'Total de votos = {votostotais[0]}')
    y = votosval*100//(votostotais[0])
    print(f'Total de votos válidos e % = {votosval} {y}%')
    w = branco[1]*100//(votostotais[0])
    print(f'Total de brancos e % = {branco[1]} {w}%')
    z = branco[1]*100//(votostotais[0])
    print(f'Total de nulos e % = {nulo[1]} {z}%')
    print()
    lista5 = []
    for i in candidatospresidencia:
        lista5.append(i[4])
    ordenar(lista5)
    lista5 = lista5[::-1]
    lista6 = []
    for i in range(len(candidatospresidencia)):
        for j in (lista5):
            if candidatospresidencia[i][4] == j:
                lista6.append(candidatospresidencia[i])
    votosval = votostotais[0] - (branco[2] + nulo[2])
    vencedores.append(lista2[0])
    print('RANKING DO RESULTADO PARA GOVERNADOR')
    print('CANDIDATO / PARTIDO /  VOTOS / % VOTOS VÁLIDOS')
    h = 0
    for i in lista6:
        h += 1
        k = i[4]*100//(votosval)
        print(f'{h}.{i[0]} / {i[1]} / {i[4]} / {k}')
    print()
    print(f'Total de votos = {votostotais[0]}')
    y = votosval*100//(votostotais[0])
    print(f'Total de votos válidos e % = {votosval} {y}%')
    w = branco[2]*100//(votostotais[0])
    print(f'Total de brancos e % = {branco[2]} {w}%')
    z = branco[2]*100//(votostotais[0])
    print(f'Total de nulos e % = {nulo[2]} {z}%')
    print()
    menu()


def statuseleição():
    ordenar(eleiçãoam)
    print('Eleitores Votantes:')
    for i in eleiçãoam:
        print(i)
    a = len(eleitores)
    print(f'dos {a} eleitores, {votostotais[0]} eleiçãoam')
    
    x = vencedores[0][1]
    y = vencedores[1][1]
    z = vencedores[2][1]
    if x == y and x == z:
        print(f'o partido {x} foi o que elegeu mais candidatos')
        a = 1
    elif x == y or x == z:
        print(f'o partido {x} foi o que elegeu mais candidatos')        
        a = 2
    elif y == x and y == x:
        print(f'o partido {y} foi o que elegeu mais candidatos')  
        a = 1
    elif y == x or y == x:
        print(f'o partido {y} foi o que elegeu mais candidatos')
        a = 2
    elif z == y and z == x:
        print(f'o partido {z} foi o que elegeu mais candidatos')
        a = 1
    elif z == y or z == x:
        print(f'o partido {z} foi o que elegeu mais candidatos')
        a = 2
    elif x != y and x != z and y != z:
        print(f'os partidos {x}, {y} e {z} elegeram apenas 1 candidato')
        a = 3
    print()
    k = []
    l = []
    for i in candidatosgovernador:
        if i[1] in k:
            continue
        else:
            k.append(i[1])
    for i in candidatosprefeitura:
        if i[1] in k:
            continue
        else:
            k.append(i[1])
    for i in candidatospresidencia:
        if i[1] in k:
            continue
        else:
            k.append(i[1])
    if a == 1 or a ==3:
        for i in k:
            if i == x or i == y or i == z:
                continue
            else:
                l.append(i)
        print('os partidos', end = ' ')
        for i in l:
            print(i,end =', ')
        print('não elegeram nenhum candidato')
    else:
        if x == y:
            print(f'O partido {z} foi o que elegeu menos candidatos')
        if y == z:
            print(f'O partido {x} foi o que elegeu menos candidatos')
        if z == x:
            print(f'O partido {y} foi o que elegeu menos candidatos')
            print()
    menu()
    
    
    
def eleição():
    print()
    a = True
    x = input('Coloque o seu nome: ')
    for i in eleitores:
        if x == i:
            a = False
            eleiçãoam.append(i)
    if a:
        x = input('Nome não registrado, deseja tentar novamente? Sim / Não ')
        if x == 'Sim':
            eleição()
        else:
            menu()
            
    votaçãopref()
    print()
    votaçãogov()
    print()
    votaçãopres()
    print()
    menu()
    
    
def menu():
    print("Menu de Votação")
    print("1 - Cadastrar Candidatos: ")
    print("2 - Cadastrar Eleitores: ")
    print("3 - Votação: ")
    print("4 - apurarvotos dos Resultados: ")
    print("5 - Relatório e Estatísticas: ")
    print("6 - Encerrar: ")

    decidirmenu = int(input("Qual opcão você deseja selecionar? : "))
    if decidirmenu  == 1:
        cdtcandidatos()
    if decidirmenu  == 2:
        cdteleitores()
    if decidirmenu  == 3:
        eleição()
    if decidirmenu  == 4:
        apuraração()
    if decidirmenu  == 5:
        statuseleição()
    if decidirmenu  == 6:
        return(None)
    
    
def organizar(v, e, d):
    x = v[d-1]
    i = e-1
    for j in range(e,d):
        if v[j] <=x:
            i += 1
            v[i],v[j] = v[j], v[i]
    return(i)        
def ordenar(v): 
    n = len(v)
    e = 0
    d = n
    ordem1 = []
    ordem1.append((e, d))
    while ordem1 != []:
        e, d = ordem1.pop()
        if e < d-1:
            m = organizar(v, e, d)
            ordem1.append((e, m))
            ordem1.append((m+1, d))
menu()