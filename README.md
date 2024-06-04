# MountainCar-v0 Genetic Algorithm

This project implements a genetic algorithm to solve the classic reinforcement learning problem in the `MountainCar-v0` environment from OpenAI Gym. The goal is to train an agent to reach the flag at the top of the hill by applying the right force to the car.

## Approach

1. **Population Initialization**:
   - Generate a population of individuals (chromosomes), where each individual represents a sequence of actions (genes) for the car.
   - Each action corresponds to applying force to the car (e.g., push left, push right, or do nothing).
2. **Fitness Evaluation**:
   - Evaluate the fitness of each individual by running the simulation in the environment.
   - The fitness is based on how far the car reaches within a fixed number of time steps.
3. **Selection and Reproduction**:
   - Select the fittest individuals to be parents for the next generation.
   - Apply crossover (recombination) and mutation to create new individuals (offspring).
4. **Next Generation**:
   - Combine parents and offspring to form the next generation.
   - Repeat the process for a fixed number of generations.

## Usage

1. Clone this repository to your local machine.
2. Run the genetic algorithm by executing the provided Python script.
3. Observe how the population evolves over generations to improve the car’s performance.
