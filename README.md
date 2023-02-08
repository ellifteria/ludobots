# FAERY Sims: simulated robot optimization using Family Aware EvolutionaRY (FAERY) Algorithms

Family Aware EvolutionaRY (FAERY) algorithms provide a method of optimizing phenotypic fitness through a genetic algorithm while maintaining diversity within the population.

## Motivation

Local optima are frequently problems in optimization searches since there is often no way to determine if a given configuration at an optimum reaches a local or global optimum.
To combat the while local optima are often unavoidable, maintaining diversity within the configuration population allows new designs to evolve and potentially reach other local optima or even the global optimum.

Towards this goal, here I present Family Aware EvolutionaRY (FAERY) algorithms, a set of genetic algorithms aimed at balancing optimization and diversity preservation.
FAERY algorithms are a set of genetic algorithms that attempt to achieve diversity by remembering the lineages of individual configurations and restricting the number of children that are passed on to the next generation from each lineage.
FAERY algorithms produce children by in some way mixing the genomes of parents and then mutating the child genomes to some degree.
Ideally, through this process of maintaining diversity while optimizing, promising genetic lines are retained and mixed as the optimization process progresses while poorly performing lines are dropped.
Additionally, randomly generated members are added to each generation of the FAERY algorithms to insert new genomes into the population.

## Simulated robot evolution

Two FAERY algorithms were used to optimize the design of a simulated robot's neural network weights using [pyrosim](https://github.com/jbongard/pyrosim) as part of the [ludobots](https://www.reddit.com/r/ludobots/) online course.

### Robot design

For the optimization, a simple quadrupedal robot was designed.

![quadruped image](/media/quadruped.png?raw=true)

The robot's neural network consisted of a set of sensor neurons on the feet of the robot and a set of motor neurons at each joint telling the motor to which angle to turn.
Additionally, a sinusoidally modulated sensation was input to the robot by overwriting the robot's torso's sensor neurons reading with a sine function, modelling the working of central pattern generators [CPGs](https://en.wikipedia.org/wiki/Central_pattern_generator) in biological nervous systems.

### Optimization algorithm 1: ludoFAE1

ludoFAE1 belongs to the classifications of **partial mating** and **gene averaging** FAERY algorithms.

As a partial mating FAERY algorithm, each member in a generation is only mated to a subset of the members in the generation for producing children.
In the case of ludoFAE1, this mating is chosen at random.
Each member of each generation in ludoFAE1 is randomly mated to a user-defined number of randomly chosen members.
There is an equally likely chance of the match being with any member of the generation.

As a gene averaging algorithm, ludoFAE1 produces child genomes by averaging the genomes of the parents in a match.
The average is computed as a randomly weighted average between the two parent genomes.
The formula for a child gene can be written as `gci = pi * gp1i + (1-pi) * gp2i` where

* `gci` is gene `i` in the child genome,
* `gp1` is gene `i` in the first parent's genome,
* `gp2i` is gene `i` in the second parent's genome, and
* `pi` is the randomly chosen weighting for gene `i`.

After this gene averaging, ludoFAE1 mutated a single random gene by a random amount as directed by user-provided mutation rate and mutation magnitude specifications.

### Optimization algorithm 2: ludoFAE2

ludoFAE2, like ludoFAE1 is a **gene averaging** algorithm using the same method of child gene production as ludoFAE1.
However, ludoFAE2 is a **full mating** algorithm.
Therefore, in ludoFAE2, every individual in a generation is mated with every other individual in the generation, including itself.

### Optimization results

Running ludoFAE1 and ludoFAE2 with the specifications found [here](/constants.py) demonstrated that both algorithms were capable of optimizing a simulated robot to achieve a desired goal.

[![ludoFAE2 optimization video](https://img.youtube.com/vi/oBoEBxVF9pE/0.jpg)](https://www.youtube.com/watch?v=oBoEBxVF9pE)

The above video demonstrates the ludoFAE2 algorithm; the ludoFAE1 algorithm produced similar results.
Statistical analysis would be required to evaluate which algorithm performs better.

## Future work

Future work on the FAERY algorithms includes:

* statistical analysis comparing FAERY algorithms and other optimization schemes
* the creation of more FAERY algorithms, including **weighted partial mating** FAERY algorithms
* the use of FAERY algorithms to optimize other objectives besides simple simulated robot neural network designs.

## Special thanks to

* [ludobots online course](https://www.reddit.com/r/ludobots/) by [Dr. Josh Bongard](https://jbongard.github.io)
* Artificial Life @ Northwestern University taught by [Dr. Sam Kriegman](https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/kriegman-sam.html)
