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
print("The fact it is sunny does not change the given probability of a raise.\n\
This answer is given in the problem definition")

print("\nP(Raise | happy ^ sunny):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), sun).show_approx())
print("This result hinges on the difference between the probabilities\n\
of being happy when it is only sunny and when it is sunny and a raise\n\
has been given. Otherwise, it is very similar to the initial probability\n\
of a raise.\n\
Hand Calculations:\n\
P(R|h^s) = alpha*<P(-r)*P(h|s^-r), P(r)*P(h|s^r)>\n\
         = alpha*<0.99*0.7, 0.01*1.0>\n\
         = alpha*<0.693, 0.01>\n\
         = <0.986, 0.0142>")


print("\nP(Raise | happy):")
print(enumeration_ask('Raise', dict(Happy=T), sun).show_approx())
print("This probability is slightly higher than the previous because the\n\
possibility of happiness being caused by a raise alone is on the\n\
table.\n\
Hand Calculations:\n\
P(R|h) = alpha*<P(-r)*P(-s)*P(h|-s^-r) + P(-r)*P(s)*P(h|s^-r),\n\
                P(r)*P(-s)*P(h|-s^r) + P(r)*(P(s)*P(h|s^r)>\n\
       = alpha*<0.99*0.3*0.1 + 0.99*0.7*0.7, 0.01*0.3*0.9 + 0.01*0.7*1.0>\n\
       = alpha*<0.5148, 0.0097>\n\
       = <0.982, 0.0185>")

print("\nP(Raise | happy ^ -sunny):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), sun).show_approx())
print("The probability here is even higher because the possibility of\n\
the person being happy because it is sunny is eliminated, and the\n\
only cause could be a raise, or have no cause for happiness.\n\
P(R|h^-s) = alpha*<P(-r)*P(h|-s^-r), P(r)*P(h|-s^r)>\n\
          = alpha*<0.99*0.1, 0.01*0.9>\n\
          = alpha*<0.099, 0.009>\n\
          = <0.917, 0.0833>")
