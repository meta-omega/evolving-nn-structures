import math
import random
import numpy as np

# Let's say the goal is to output the next fibonnacci number.

random_nat = lambda mean, sd: math.floor(abs(random.gauss(mean, sd)))

class NeuralNet:
    def __init__(self):
        count = random_nat(0, 1)
        sizes = [random_nat(50, 2) for _ in range(count)]

        self.weights = []

def fitness(nn):
    return 0

def main():
    return 0

main()

'''

Nota para Dylan:
Me suena que tenés que aprender más acerca de redes neuronales,
ya que estás medio en cero y no te sentís cómodo jugando.

'''
