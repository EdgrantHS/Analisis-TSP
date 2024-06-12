import numpy as np
import random
import time
import itertools


# Generate a random list of nodes
def generate_nodes(n):
    return np.random.rand(n, 2)


# Calculate the distance matrix
def calculate_distance_matrix(nodes):
    n = len(nodes)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = np.linalg.norm(nodes[i] - nodes[j])
    return distance_matrix


def brute_force_tsp(distance_matrix):
    n = len(distance_matrix)
    all_permutations = itertools.permutations(range(n))
    min_cost = float("inf")
    best_path = None
    for perm in all_permutations:
        current_cost = sum(distance_matrix[perm[i]][perm[i + 1]] for i in range(n - 1))
        current_cost += distance_matrix[perm[-1]][perm[0]]
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = perm
    return best_path, min_cost


def dynamic_programming_tsp(distance_matrix):
    n = len(distance_matrix)
    memo = {}

    def visit(node, visited):
        if (node, visited) in memo:
            return memo[(node, visited)]
        if visited == (1 << n) - 1:
            return distance_matrix[node][0]
        min_cost = float("inf")
        for next_node in range(n):
            if not visited & (1 << next_node):
                cost = distance_matrix[node][next_node] + visit(
                    next_node, visited | (1 << next_node)
                )
                if cost < min_cost:
                    min_cost = cost
        memo[(node, visited)] = min_cost
        return min_cost

    min_cost = visit(0, 1)
    return min_cost


def nearest_neighbor_tsp(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_node = min(unvisited, key=lambda x: distance_matrix[last][x])
        tour.append(next_node)
        unvisited.remove(next_node)
    tour.append(0)
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(n))
    return tour, cost


def simulated_annealing_tsp(
    distance_matrix, initial_temp=10000, cooling_rate=0.995, min_temp=1e-3
):
    def calculate_cost(tour):
        return (
            sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            + distance_matrix[tour[-1]][tour[0]]
        )

    def get_neighbor(tour):
        a, b = random.sample(range(len(tour)), 2)
        tour[a], tour[b] = tour[b], tour[a]
        return tour

    n = len(distance_matrix)
    current_tour = list(range(n))
    random.shuffle(current_tour)
    current_cost = calculate_cost(current_tour)
    best_tour = current_tour[:]
    best_cost = current_cost
    temp = initial_temp

    while temp > min_temp:
        new_tour = get_neighbor(current_tour[:])
        new_cost = calculate_cost(new_tour)
        if new_cost < current_cost or random.uniform(0, 1) < np.exp(
            (current_cost - new_cost) / temp
        ):
            current_tour = new_tour
            current_cost = new_cost
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost
        temp *= cooling_rate

    return best_tour, best_cost


def ant_colony_tsp(
    distance_matrix,
    num_ants=10,
    num_iterations=100,
    alpha=1,
    beta=5,
    evaporation_rate=0.5,
    Q=100,
):
    n = len(distance_matrix)
    pheromone = np.ones((n, n)) / n
    all_time_best_cost = float("inf")
    all_time_best_tour = None

    def calculate_cost(tour):
        return (
            sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            + distance_matrix[tour[-1]][tour[0]]
        )

    def select_next_city(pheromone, heuristic, alpha, beta, visited):
        prob = (pheromone**alpha) * (heuristic**beta)
        prob[list(visited)] = 0
        prob = prob / prob.sum()
        return np.random.choice(range(len(prob)), p=prob)

    def update_pheromone(pheromone, all_tours, all_costs):
        pheromone *= 1 - evaporation_rate
        for tour, cost in zip(all_tours, all_costs):
            for i in range(len(tour) - 1):
                pheromone[tour[i]][tour[i + 1]] += Q / cost
            pheromone[tour[-1]][tour[0]] += Q / cost
        return pheromone

    heuristic = 1 / (distance_matrix + np.eye(n) * 1e-10)

    for _ in range(num_iterations):
        all_tours = []
        all_costs = []
        for _ in range(num_ants):
            tour = [0]
            visited = set(tour)
            for _ in range(n - 1):
                next_city = select_next_city(
                    pheromone[tour[-1]], heuristic[tour[-1]], alpha, beta, visited
                )
                tour.append(next_city)
                visited.add(next_city)
            tour.append(0)
            cost = calculate_cost(tour)
            all_tours.append(tour)
            all_costs.append(cost)
            if cost < all_time_best_cost:
                all_time_best_cost = cost
                all_time_best_tour = tour
        pheromone = update_pheromone(pheromone, all_tours, all_costs)

    return all_time_best_tour, all_time_best_cost


def genetic_algorithm_tsp(
    distance_matrix,
    population_size=100,
    generations=500,
    mutation_rate=0.01,
    elite_size=20,
):
    def calculate_cost(tour):
        return (
            sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            + distance_matrix[tour[-1]][tour[0]]
        )

    def initial_population():
        return [
            random.sample(range(len(distance_matrix)), len(distance_matrix))
            for _ in range(population_size)
        ]

    def selection(population):
        costs = np.array([calculate_cost(individual) for individual in population])
        probabilities = np.exp(-costs / costs.std())
        probabilities /= probabilities.sum()
        selected = np.random.choice(
            range(len(population)), size=population_size - elite_size, p=probabilities
        )
        return [population[i] for i in selected]

    def crossover(parent1, parent2):
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [-1] * len(parent1)
        child[start:end] = parent1[start:end]
        pointer = end
        for gene in parent2:
            if gene not in child:
                while pointer < len(child) and child[pointer] != -1:
                    pointer += 1
                if pointer >= len(child):
                    pointer = 0
                while child[pointer] != -1:
                    pointer += 1
                child[pointer] = gene
        return child

    def mutate(tour):
        if random.random() < mutation_rate:
            a, b = random.sample(range(len(tour)), 2)
            tour[a], tour[b] = tour[b], tour[a]
        return tour

    population = initial_population()
    for _ in range(generations):
        population = sorted(population, key=calculate_cost)
        new_population = population[:elite_size]
        for _ in range(population_size - elite_size):
            parent1, parent2 = random.sample(population[: population_size // 2], 2)
            child = mutate(crossover(parent1, parent2))
            new_population.append(child)
        population = new_population

    best_tour = min(population, key=calculate_cost)
    best_cost = calculate_cost(best_tour)
    return best_tour, best_cost


def run_brute_force(f):
    start_time = time.time()
    best_path, min_cost = brute_force_tsp(distance_matrix)
    end_time = time.time()
    print(
        f"Brute Force: Best Path: {best_path}, \nCost: {min_cost}, \nTime: {end_time - start_time} seconds"
    )
    f.write(f"Brute Force: Best Path: {best_path}, \nCost: {min_cost}, \nTime: {end_time - start_time} seconds")

def run_dynamic_programming(f):
    start_time = time.time()
    min_cost = dynamic_programming_tsp(distance_matrix)
    end_time = time.time()
    print(
        f"Dynamic Programming: \nCost: {min_cost}, \nTime: {end_time - start_time} seconds"
    )
    f.write(f"Dynamic Programming: \nCost: {min_cost}, \nTime: {end_time - start_time} seconds")

def run_nearest_neighbor(f):
    start_time = time.time()
    tour, cost = nearest_neighbor_tsp(distance_matrix)
    end_time = time.time()
    print(
        f"Nearest Neighbor: Best Path: {tour}, \nCost: {cost}, \nTime: {end_time - start_time} seconds"
    )
    f.write(f"\nNearest Neighbor: Best Path: {tour}, \nCost: {cost}, \nTime: {end_time - start_time} seconds")

def run_simulated_annealing(f):
    start_time = time.time()
    best_tour, best_cost = simulated_annealing_tsp(distance_matrix)
    end_time = time.time()
    print(
        f"Simulated Annealing: Best Path: {best_tour}, \nCost: {best_cost}, \nTime: {end_time - start_time} seconds"
    )
    f.write(f"\nSimulated Annealing: Best Path: {best_tour}, \nCost: {best_cost}, \nTime: {end_time - start_time} seconds")

def run_ant_colony(f):
    start_time = time.time()
    best_tour, best_cost = ant_colony_tsp(distance_matrix)
    end_time = time.time()
    print(
        f"Ant Colony: Best Path: {best_tour}, \nCost: {best_cost}, \nTime: {end_time - start_time} seconds"
    )
    f.write(f"Ant Colony: Best Path: {best_tour}, \nCost: {best_cost}, \nTime: {end_time - start_time} seconds")

def run_genetic_algorithm(f):
    start_time = time.time()
    best_tour, best_cost = genetic_algorithm_tsp(distance_matrix)
    end_time = time.time()
    print(
        f"Genetic Algorithm: Best Path: {best_tour}, \nCost: {best_cost}, \nTime: {end_time - start_time} seconds"
    )
    f.write(f"Genetic Algorithm: Best Path: {best_tour}, \nCost: {best_cost}, \nTime: {end_time - start_time} seconds")


# save to file
with open("output.txt", "w") as f:

    for j in range(1, 10, 1):
        print(f"Run {j+1}")
        for i in range(10):
            nodes = generate_nodes(j + 1)
            distance_matrix = calculate_distance_matrix(nodes)
            run_brute_force(f)
            run_dynamic_programming(f)
            run_simulated_annealing(f)
            run_ant_colony(f)
            run_genetic_algorithm(f)
            run_nearest_neighbor(f)

    for j in range(10, 20, 2):
        print(f"Run {j+1}")
        for i in range(10):
            nodes = generate_nodes(j + 1)
            distance_matrix = calculate_distance_matrix(nodes)
            # run_brute_force(f)
            run_dynamic_programming(f)
            run_simulated_annealing(f)
            run_ant_colony(f)
            run_genetic_algorithm(f)
            run_nearest_neighbor(f)

    for j in range(20, 100, 10):
        print(f"Run {j+1}")
        for i in range(10):
            nodes = generate_nodes(j + 1)
            distance_matrix = calculate_distance_matrix(nodes)
            # run_brute_force(f)
            # run_dynamic_programming(f)
            run_simulated_annealing(f)
            run_ant_colony(f)
            run_genetic_algorithm(f)
            run_nearest_neighbor(f)
