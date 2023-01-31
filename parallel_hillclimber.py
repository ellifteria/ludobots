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
        for parent_key in self.parents:
            parent = self.parents[parent_key]
            parent.start_simulation()
        
        for parent_key in self.parents:
            parent = self.parents[parent_key]
            print("\n\n" + str(parent.wait_for_simulation_to_end()))

        for i in range(Cnsts.num_generations):
            self.evolve_for_one_generation()
        
        for parent_key in self.parents:
            parent = self.parents[parent_key]
            parent.start_simulation("GUI")
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate("DIRECT")
        self.select()

    def spawn(self) -> None:
        self.children = {}
        for parent_key in self.parents:
            parent = self.parents[parent_key]
            self.children[parent] = copy.deepcopy(parent)

    def mutate(self) -> None:
        for child_key in self.parents:
            child = self.parents[child_key]
            child.mutate()

    def evaluate(self, solutions) -> None:

    def select(self) -> None:
        print("\n{} \t\t {}\n".format(self.parent.fitness, self.child.fitness))
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
