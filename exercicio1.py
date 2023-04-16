import numpy as np
import geneticFunc as gf

# Número de indivíduos = tamanho da população
n_individuals = 10

# Tamanho do bitstring
bstring_size = 12

# Bitstring representando o número 0
goal = np.array([1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1])

# Inicializa a população
population = gf.initialize_population(n_individuals, bstring_size)

# Avalia a população por meio da distância de Hamming => Cálculo da aptidão.
fitness = gf.hamming_distance(population, goal)

# Seleciona os indíviduos para aplicar os operadores crossover e mutação.
# A seleção é feita pelo método da roleta.
selected_ind = gf.roulette_wheel_selection(fitness, n_individuals)

#population = crossover_operator(selected_ind, population, n_individuals)

print(selected_ind)

