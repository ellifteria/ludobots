from solution import Solution
import constants as Cnsts
import copy

class ParallelHillClimber:
    
    def __init__(self) -> None:
        self.parents = {}
        self.next_available_id = 0
        for i in range(Cnsts.population_size):
            self.parents[i] = Solution(solution_id=self.next_available_id)
            self.next_available_id += 1

    def evolve(self) -> None:
        for parent_key in self.parents:
            parent = self.parents[parent_key]
            parent.evaluate()
            # for i in range(Cnsts.num_generations):
            #     self.evolve_for_one_generation()
            parent.evaluate("GUI")
    
    def evolve_for_one_generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate("DIRECT")
        self.select()

    def spawn(self) -> None:
        self.child = copy.deepcopy(self.parent)

    def mutate(self) -> None:
        self.child.mutate()

    def select(self) -> None:
        print("\n{} \t\t {}\n".format(self.parent.fitness, self.child.fitness))
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
