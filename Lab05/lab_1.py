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
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

print("P(Alarm | burglary ^ -earthquake):")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print("This result is given in the bayesian network probability tables.")

print("\nP(JohnCalls | burglary ^ -earthquake):")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print("This result takes into account that the alarm does not necessarily go off when")
print("the burglary occurs, John may not have called if the alarm went off, and John")
print("could call anyways even if the alarm does not go off.")

print("\nP(Burglary | alarm):")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
print("This result must calculate its probability based on all of the possible reasons")
print("the alarm could go off.")

print("\nP(Burglary | john_calls ^ mary_calls):")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
print("To calculate this probability one must take into account all of the possible")
print("scenarios that could cause john and mary to call.")
