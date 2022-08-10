import gym
import random

#Programa Imprime Resultados a Cada 125
#Verificar Se Variaveis São Divisiveis Por 4 para evitar erros

envName = 'MountainCar-v0'
renderMode = 'human'
qGeracoes = 125 #quanto desejar
qIndividuos = 80 #mult4
qMovimentos = 200 #mult4
qAcoes = 3 #API
qObservacoes = 6 #API
iMutacao = 5 #recomenda-se 5 a 0.05
printCada = 125 #recomenda-se 1/4 das geracoes

indices = []
for i in range (0,int (qIndividuos//2)):
    for j in range (0, i):
        indices.append(i) #para realizar escolha n²

#Gerar uma ação (GENE)
def gerarAcao():
    return random.choice(range(0,qAcoes))

#Gera um conjunto de ações (CROMOSSOMO)
def gerarIndividuo():
    lista = []
    for i in range (0, qMovimentos):
        lista.append(gerarAcao())
    return lista

#Gera um conjunto de indivíduos (POPULAÇÃO)
def gerarPopulacao():
    lista = []
    for i in range (0, qIndividuos):
        lista.append(gerarIndividuo())
    return lista

#Gera um valor de avaliação para cada indivíduo (FITNESS)
def fitness(list): 
    fitness = []
    env = gym.make(envName, new_step_api=True)
    for j in range (0,len(list)):
        env.reset()
        for i in range (0, qMovimentos):
            state, reward, done, info, data = env.step((list[j][i]))
            if(i == qMovimentos - 1):
                posFinal = state[0]
        fitness.append(posFinal)
    return fitness

#Ordena os índividuos de acordo melhor fitness (AVALIAÇÃO)
def avaliar(list,g): 
    avalicaoes = fitness(list)
    if(g%printCada==0): #Imprime Dados A Cada
        print(avalicaoes)
    lista = [x for (y,x) in sorted (zip(avalicaoes,list))]
    if(g%printCada==0):
        print("Melhor da geração: ", lista[len(lista)-1])
    return lista

#Seleciona os índividuos de melhor fitness apenas (SELEÇÃO)
def selecionar(list,g): 
    lista = avaliar(list,g)
    return lista[(len(lista)//2):] #segunda metade

#Algoritmo que gere um gene aleatório em novas crianças (MUTAÇÃO)
def mutation(item):       
    probability = random.randint(0, 100)
    if probability <= iMutacao:     #mesmo que entre ele pode ser trocado para o valor que já estava antes 
        mutated_allele = random.randint(0, qMovimentos-1)
        item[mutated_allele] = random.randint(0, qAcoes-1)
    return item

#Algoritmo que junta os genes dos pais (REPRODUÇÃO II)
def criarFilho(parent1, parent2):
    qMov = qMovimentos//2
    return mutation(parent1[:qMov] + parent2[qMov:])

#Algoritmo que seleciona que sorteia 2 entre os mais aptos para procriar (REPRODUÇÃO I)
def crossover(parents):
    kids = []
    cont = 0
    for i in range(0, qIndividuos-len(parents),2):
        pai = random.choice(indices)
        mae = random.choice(indices)
        sun1 = criarFilho(parents[pai],parents[mae])
        sun2 = criarFilho(parents[mae],parents[pai])
        kids.append(sun1)
        kids.append(sun2)
    return kids

#Algoritmo que inicia o processo de criação de próximas gerações
def proxGeracao(list, reproduzir, g):
    filhos = []
    pais = selecionar(list, g)
    if(reproduzir==True):
        filhos = crossover(pais) 
    return filhos + pais

#main
def main():
    populacao = gerarPopulacao()
    for i in range (0, qGeracoes):
        populacao = proxGeracao(populacao, True, i+1)
    populacao = proxGeracao(populacao, False,qGeracoes)
    #populacao = avaliar(populacao,qGeracoes)
    #print(populacao[qIndividuos-1])
    #env = gym.make(envName, new_step_api=True, render_mode='human') #render_mode=renderMode
    #env.reset()
    #for i in range (qMovimentos):
    #    state, reward, done, info, data = env.step(populacao[qIndividuos-1][i])


main()