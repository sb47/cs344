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
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

print("P(Cancer | test1 ^ test2):")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

print("\nP(Cancer | test1 ^ -test2):")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

print("\nThe results make sense because the initial probability of having cancer is")
print("so low and false positives are likely. The effect of one failed test reduced")
print("the probability of having cancer by more than 16%.")

