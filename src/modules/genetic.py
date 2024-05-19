import random
from modules.chromosome import Chromosome


class Genetic:
    @staticmethod
    def population_generate(
        population_size: int,
        binary_length: int = 4,
    ) -> list[Chromosome]:
        population: list[Chromosome] = []
        for _ in range(population_size):
            random_value = "".join(random.choices(["0", "1"], k=binary_length))
            population.append(Chromosome(random_value))

        return population

    @staticmethod
    def get_fitnes_ratio(population: list[Chromosome]) -> tuple[list[float], float]:
        fitness_array: list[int] = []
        fitness_ratio: list[float] = []
        sum_fitness = 0

        # Calculo do fitness de cada cromossomo
        for chromosome in population:
            fitness_array.append(Genetic.fitness(chromosome.get_number()))

        # Soma total dos fitness
        for fitness in fitness_array:
            sum_fitness += fitness

        # Calculo do ratio de fitness de cada cromossomo [fitness do cromossomo / soma total dos fitness]
        for i in range(len(fitness_array)):
            fitness_ratio.append(fitness_array[i] / sum_fitness)

        # Media de fitness
        fitness_average = sum(fitness_array) / len(fitness_array)
        return fitness_ratio, fitness_average


    #Retorna os dois melhores indices da população
    @staticmethod
    def roulette_selection(
        population: list[Chromosome],
        fines_ratio: list[float],
    ) -> tuple[Chromosome, Chromosome]:
        x = Chromosome("0000")
        y = Chromosome("0000")
        
        for fitnes in fines_ratio:
            if random.random() <= fitnes:
                if x == Chromosome("0000"):
                    x = population[fines_ratio.index(fitnes)]
                    break

                else:
                    y = population[fines_ratio.index(fitnes)]
                    break

        return x, y

    @staticmethod
    def mutation(chromosome: Chromosome, percent_mutation: float) -> Chromosome:        
        if random.random() <= percent_mutation:
            #Escolhe aleatoriamente um bit da string e inverte
            index = random.randint(0, len(chromosome.value) - 1)
            chromosome.value = (
                chromosome.value[:index]
                + ("0" if chromosome.value[index] == "1" else "1")
                + chromosome.value[index + 1 :]
            )

        return chromosome

    @staticmethod
    def crossover(x: Chromosome, y: Chromosome) -> Chromosome:
        child = "".join([x.value[:2]]).join(y.value[2:])
        return Chromosome(child)

    @staticmethod
    def fitness(value: int):
        return (15 * value) - (value * value)
