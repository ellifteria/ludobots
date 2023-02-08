import os
import random

import numpy as np
import merge_sort
from solution import Solution
import constants as Cnsts

class ludoFAE1:
    
    def __init__(self) -> None:
        os.system("rm ./data/robot/robot_fitness*.txt")
        os.system("rm ./data/robot/brain*.nndf")
        os.system("rm ./data/robot/body*.urdf")
        self.parents = {}
        self.next_available_id = 0

        self.generation_size = Cnsts.generation_size
        self.number_of_children = Cnsts.number_of_children
        self.family_filter_size = Cnsts.family_filter_size
        self.random_members = Cnsts.random_members
        self.total_filter_size = self.generation_size - self.random_members

        for parent_num in range(Cnsts.generation_size):
            parent_id = "000" + f"{parent_num:03}" + f"{parent_num:03}" + "000"
            self.parents[parent_id] = Solution(solution_id=parent_id)
            self.next_available_id += 1

        self.genome_shape = self.parents["000000000000"].network_shape

    def evolve(self) -> None:
        self.evaluate(self.parents)

        for generation in range(Cnsts.num_generations):
            os.system("rm ./data/robot/robot_fitness*.txt")
            os.system("rm ./data/robot/brain*.nndf")
            os.system("rm ./data/robot/body*.urdf")
            self.evolve_for_one_generation(generation)
        
        self.show_best()

    def evaluate(self, solutions) -> None:
        for key in solutions:
            solution = solutions[key]
            solution.start_simulation()
        
        for key in solutions:
            solution = solutions[key]
            solution.wait_for_simulation_to_end()
    
    def evolve_for_one_generation(self, generation):
        self.produce_children(generation)
        self.mutate()
        self.evaluate(self.children)
        self.print()
        self.select(generation)

    def produce_children(self, generation):
        self.children = {}
        for parent1 in self.parents:
            for child_num in range(self.number_of_children):
                parent2 = random.choice(list(self.parents.keys()))
                percent_parent1 = np.random.rand(*self.genome_shape)
                percent_parent2 = 1 - percent_parent1

                parent1_genome = self.parents[parent1].weights
                parent2_genome = self.parents[parent2].weights

                child_id = f"{generation+1:03}" + parent1[3:6] + parent2[3:6] + f"{child_num:03}"

                child_genome = np.multiply(percent_parent1, parent1_genome) + np.multiply(percent_parent2, parent2_genome)

                self.children[child_id] = Solution(child_id, child_genome)


    def mutate(self) -> None:
        for child_key in self.children:
            child = self.children[child_key]
            child.mutate()

    def print(self) -> None:
        parent_fitnesses = []
        for key in self.parents:
            parent_fitnesses.append(self.parents[key].fitness)

        child_fitnesses = []
        for key in self.children:
            child_fitnesses.append(self.children[key].fitness)

        print("\np max: {} \t\t c max: {}".format(np.max(parent_fitnesses), np.max(child_fitnesses)))
        print("p mean: {} \t\t c mean: {}\n".format(np.mean(parent_fitnesses), np.mean(child_fitnesses)))

    def select(self, generation) -> None:
        individuals = self.children | self.parents
        sorted_individual_indices = self.sort_individuals(individuals)
        next_generation = {}
        family_counts = {}
        while len(next_generation) < self.total_filter_size:
            top_individual_index = sorted_individual_indices[0]
            top_individual = individuals[top_individual_index]
            top_individual_family1 = top_individual_index[3:6]
            top_individual_family2 = top_individual_index[6:9]
            if top_individual_family1 not in family_counts:
                family_counts[top_individual_family1] = 0
            if top_individual_family2 not in family_counts:
                family_counts[top_individual_family2] = 0
            if family_counts[top_individual_family1] > self.family_filter_size or family_counts[top_individual_family2] > self.family_filter_size:
                sorted_individual_indices.remove(top_individual_index)
            else:
                family_counts[top_individual_family1] += 1
                family_counts[top_individual_family2] += 1
                next_generation[top_individual_index] = top_individual
                sorted_individual_indices.remove(top_individual_index)
        new_members = {}
        for random_member_index in range(self.random_members):
            new_individual_key = self.generation_size + (generation * self.random_members) + random_member_index
            new_id = f"{generation:03}" + f"{new_individual_key:03}" + f"{new_individual_key:03}" + f"{random_member_index:03}"
            new_members[new_id] = Solution(solution_id=new_id)
        self.evaluate(new_members)
        self.parents = next_generation | new_members

    def show_best(self) -> None:
        top_key = list(self.parents.keys())[0]
        for key in self.parents:
            parent = self.parents[key]
            current_best = self.parents[top_key]
            if parent.fitness > current_best.fitness:
                top_key = key
        print(self.parents[top_key].fitness)
        self.parents[top_key].start_simulation("GUI")

    def sort_individuals(self, individuals):
        individual_fitness_dict = {}
        for individual in individuals:
            individual_fitness_dict[individual] = individuals[individual].fitness
        return merge_sort.merge_sort(individual_fitness_dict)
