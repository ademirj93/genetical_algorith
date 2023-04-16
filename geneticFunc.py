import numpy as np

def initialize_population(n_individuals, bstring_size):
    """Método para inicializar a população.

    Args:
        n_individuals (int): Número de indivíduos da população.
        bstring_size (int): Tamanho do bitstring.

    Returns:
        np.ndarray: A população de invíduos inicializada.
    """

    population = np.zeros((n_individuals, bstring_size))

    for i in range(n_individuals):
        population[i] += np.random.randint(0, 2, bstring_size)

    return population

def hamming_distance(population, goal): 
    """Calcula a distância de Hamming para determinar a aptidão de cada indivíduo.

    Args:
        population (np.ndarray): População
        goal (np.ndarray): Indivíduo que se quer alcançar

    Returns:
        list: Array de aptidões/fitness
    """
    fitness = []

    for i in range(len(population)):
        count = np.sum(population[i] != goal)
        fitness.append(count)

    return fitness

def roulette_wheel_selection(fitness, n_individuals):

    """Método de seleção de indivíduos pela roleta.

    Args:
        fitness (list): Lista contendo os valores de aptidão (fitness).
        n_individuals (int): Quantidade de indivíduos da população.

    Returns:
        np.ndarray: Posição dos indivíduos da população que foram selecionados.
    """

    total_fitness = sum(fitness)

    print(fitness)

    portion = 360 / total_fitness

    qtd_portion = list()

    for i in range(n_individuals):
        qtd_portion.append(fitness[i]*portion)

    bins = np.cumsum(qtd_portion)

    draw_numbers = np.random.uniform(0, 360, n_individuals)

    ind = np.digitize(draw_numbers, bins)
        
    return ind

def crossover_operator(ind, population, n_ind):
    """Método para realizar o crossover entre os cromossomos selecionados.

    Args:
        ind (np.ndarray): Individuos selecionados.
        population (np.ndarray): População.
        n_ind (int): Número de indivíduos.

    Returns:
        np.ndarray: População atualizada após o crossover.
    """

    # NÃO ESTÁ FINALIZADO

    pairs = (int)(len(ind) / 2)

    r = np.random.randint(0, b - 1, pairs)

    print(f'r = {r}')

    return r