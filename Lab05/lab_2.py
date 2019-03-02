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
print("Hand calculations:")
print("P(C|t1^t2) = alpha*<P(-c)*P(t1|-c)*P(t2|-c), P(c)*P(t1|c)*P(t2|c)>\n\
           = alpha*<0.99*0.2*0.2, 0.01*0.9*0.9>\n\
           = alpha*<0.0396, 0.0081>\n\
           = <0.83, 0.17>")

print("\nP(Cancer | test1 ^ -test2):")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
print("Hand calculations:")
print("P(C|t1^-t2) = alpha*<P(-c)*P(t1|-c)*P(-t2|-c), P(c)*P(t1|c)*P(-t2|c)>\n\
            = alpha*<0.99*0.2*0.8, 0.01*0.9*0.1>\n\
            = alpha*<0.1584, 0.0009>\n\
            = <0.994, 0.00565>")

print("\nThe results make sense because the initial probability of\n\
having cancer is so low and false positives are likely.\n\
The effect of one failed test reduced the probability of\n\
having cancer by more than 16%.")

