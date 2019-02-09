"""
This module implements local search on a abs sine function for maximum values
(see the sine function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class SineVariant(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value which is the result of abs(x * sin(x))
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    bestHCInitial = 0
    bestHCSolution = 0
    bestHCTime = 0
    bestAnnealingInitial = 0
    bestAnnealingSolution = 0
    bestAnnealingTime = 0

    for i in range(0, 100):
        # Formulate a problem with the equation f(x) = abs(x * sin(x)).
        maximum = 30
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=0.1)
        print('Initial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              )

        # Solve the problem using hill-climbing.
        hcStartTime = time.time()
        hill_solution = hill_climbing(p)
        hcEndTime = time.time()
        if hill_solution > bestHCSolution:
            bestHCInitial = initial
            bestHCSolution = hill_solution
            bestHCTime = hcEndTime - hcStartTime
        print('Hill-climbing solution       x: ' + str(hill_solution)
              + '\tvalue: ' + str(p.value(hill_solution))
              + '\ttime: ' + str(hcEndTime - hcStartTime)
              )

        # Solve the problem using simulated annealing.
        annealingStartTime = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=800)
        )
        annealingEndTime = time.time()
        if annealing_solution > bestAnnealingSolution:
            bestAnnealingInitial = initial
            bestAnnealingSolution = annealing_solution
            bestAnnealingTime = annealingEndTime - annealingStartTime
        print('Simulated annealing solution x: ' + str(annealing_solution)
              + '\tvalue: ' + str(p.value(annealing_solution))
              + '\ttime: ' + str(annealingEndTime - annealingStartTime)
              )

    print('\nBest Case:')
    print('Hill-climbing initial        x: ' + str(bestHCInitial)
          + '\t\tvalue: ' + str(p.value(bestHCInitial))
          )
    print('Hill-climbing solution       x: ' + str(bestHCSolution)
          + '\tvalue: ' + str(p.value(bestHCSolution))
          + '\ttime: ' + str(bestHCTime)
          )
    print('Simulated annealing initial  x: ' + str(bestAnnealingInitial)
          + '\t\tvalue: ' + str(p.value(bestAnnealingInitial))
          )
    print('Simulated annealing solution x: ' + str(bestAnnealingSolution)
          + '\tvalue: ' + str(p.value(bestAnnealingSolution))
          + '\ttime: ' + str(bestAnnealingTime)
          )
