import os
from solution import Solution
import constants as Cnsts
import copy

class ParallelHillClimber:
    
    def __init__(self) -> None:
        os.system("rm ./data/robot/robot_fitness*.txt")
        os.system("rm ./data/robot/brain*.txt")
        self.parents = {}
        self.next_available_id = 0
        for i in range(Cnsts.population_size):
            self.parents[i] = Solution(solution_id=self.next_available_id)
            self.next_available_id += 1

    def evolve(self) -> None:
        self.evaluate(self.parents)

        for i in range(Cnsts.num_generations):
            os.system("rm ./data/robot/robot_fitness*.txt")
            os.system("rm ./data/robot/brain*.txt")
            self.evolve_for_one_generation()
        
        self.show_best()

    def evaluate(self, solutions) -> None:
        for key in solutions:
            solution = solutions[key]
            solution.start_simulation()
        
        for key in solutions:
            solution = solutions[key]
            solution.wait_for_simulation_to_end()
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.print()
        self.select()

    def spawn(self) -> None:
        self.children = {}
        for parent_key in self.parents:
            parent = self.parents[parent_key]
            self.children[parent_key] = copy.deepcopy(parent)

    def mutate(self) -> None:
        for child_key in self.children:
            child = self.children[child_key]
            child.mutate()

    def print(self) -> None:
        for key in self.parents:
            parent = self.parents[key]
            child = self.children[key]
            print("\np: {} \t\t c: {}\n".format(parent.fitness, child.fitness))

    def select(self) -> None:
        for key in self.parents:
            parent = self.parents[key]
            child = self.children[key]
            if parent.fitness > child.fitness:
                self.parents[key] = child

    def show_best(self) -> None:
        top_key = 0
        for key in self.parents:
            parent = self.parents[key]
            current_best = self.parents[top_key]
            if parent.fitness < current_best.fitness:
                top_key = key
        print(self.parents[top_key].fitness)
        self.parents[top_key].start_simulation("GUI")
