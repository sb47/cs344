'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: Sean Brouwer
@version Mar 1, 2019
'''

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
sun = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

print("P(Raise | sunny):")
print(enumeration_ask('Raise', dict(Sunny=T), sun).show_approx())
print("The fact it is sunny does not change the given probability of a raise.")

print("\nP(Raise | happy ^ sunny):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), sun).show_approx())
print("This result hinges on the difference between the probabilities of being")
print("happy when it is only sunny and when it is sunny and a raise has been")
print("given. Otherwise, it is very similar to the initial probability of a raise.")

print("\nP(Raise | happy):")
print(enumeration_ask('Raise', dict(Happy=T), sun).show_approx())
print("This probability is slightly higher than the previous because the possibility")
print("of happiness being caused by a raise alone is on the table.")

print("\nP(Raise | happy ^ -sunny):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), sun).show_approx())
print("The probability here is even higher because the possibility of the person")
print("being happy because it is sunny is eliminated, and the only cause could be")
print("a raise, or have no cause for happiness.")

