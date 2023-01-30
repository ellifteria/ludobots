from solution import Solution
import constants as Cnsts
import copy

class HillClimber:
    
    def __init__(self) -> None:
        self.parent = Solution()

    def evolve(self) -> None:
        self.parent.evaluate()
        for i in range(Cnsts.num_generations):
            self.evolve_for_one_generation()
        self.parent.evaluate("GUI")
    
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
